# This library is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library.  If not, see <http://www.gnu.org/licenses/> or <http://www.gnu.org/licenses/lgpl.txt>.

import urllib.request, urllib.error
import http.client, socket
from urllib.response import addinfourl
try:
    from . import ntlm
except ValueError:
    import ntlm
import re

class AbstractNtlmAuthHandler:
    
    def __init__(self, password_mgr=None):
        if password_mgr is None:
            password_mgr = HTTPPasswordMgr()
        self.passwd = password_mgr
        self.add_password = self.passwd.add_password

    def http_error_authentication_required(self, auth_header_field, req, fp, headers):
        auth_header_value_list = headers.get_all(auth_header_field)
        if auth_header_value_list:
            if any([hv.lower() == 'ntlm' for hv in auth_header_value_list]):
                fp.close()
                return self.retry_using_http_NTLM_auth(req, auth_header_field, None, headers)

    def retry_using_http_NTLM_auth(self, req, auth_header_field, realm, headers):
        user, pw = self.passwd.find_user_password(realm, req.get_full_url())
        if pw is not None:
            user_parts = user.split('\\', 1)
            if len(user_parts) == 1:
                UserName = user_parts[0]
                DomainName = ''
                type1_flags = ntlm.NTLM_TYPE1_FLAGS & ~ntlm.NTLM_NegotiateOemDomainSupplied
            else:
                DomainName = user_parts[0].upper()
                UserName = user_parts[1]
                type1_flags = ntlm.NTLM_TYPE1_FLAGS
            # ntlm secures a socket, so we must use the same socket for the complete handshake
            headers = dict(req.headers)
            headers.update(req.unredirected_hdrs)
            auth = 'NTLM %s' % ntlm.create_NTLM_NEGOTIATE_MESSAGE(user, type1_flags)
            if req.headers.get(self.auth_header, None) == auth:
                return None
            headers[self.auth_header] = auth
            
            host = req.host
            if not host:
                raise urllib.request.URLError('no host given')
            h = None
            if req.get_full_url().startswith('https://'):
                h = http.client.HTTPSConnection(host) # will parse host:port
            else:
                h = http.client.HTTPConnection(host) # will parse host:port
            # we must keep the connection because NTLM authenticates the connection, not single requests
            headers["Connection"] = "Keep-Alive"
            headers = dict((name.title(), val) for name, val in list(headers.items()))
            h.request(req.get_method(), req.selector, req.data, headers)
            r = h.getresponse()
            r.begin()
            r._safe_read(int(r.getheader('content-length')))
            try:
                if r.getheader('set-cookie'): 
                    # this is important for some web applications that store authentication-related info in cookies (it took a long time to figure out)
                    headers['Cookie'] = r.getheader('set-cookie')
            except TypeError:
                pass
            r.fp = None # remove the reference to the socket, so that it can not be closed by the response object (we want to keep the socket open)
            auth_header_value = r.getheader(auth_header_field, None)

            # some Exchange servers send two WWW-Authenticate headers, one with the NTLM challenge
            # and another with the 'Negotiate' keyword - make sure we operate on the right one
            m = re.match('(NTLM [A-Za-z0-9+\-/=]+)', auth_header_value)
            if m:
                auth_header_value, = m.groups()

            (ServerChallenge, NegotiateFlags) = ntlm.parse_NTLM_CHALLENGE_MESSAGE(auth_header_value[5:])
            auth = 'NTLM %s' % ntlm.create_NTLM_AUTHENTICATE_MESSAGE(ServerChallenge, UserName, DomainName, pw, NegotiateFlags)
            headers[self.auth_header] = auth
            headers["Connection"] = "Close"
            headers = dict((name.title(), val) for name, val in list(headers.items()))
            try:
                h.request(req.get_method(), req.selector, req.data, headers)
                # none of the configured handlers are triggered, for example redirect-responses are not handled!
                response = h.getresponse()
                def notimplemented():
                    raise NotImplementedError
                response.readline = notimplemented
                return addinfourl(response, response.msg, req.get_full_url(), response.code)
            except socket.error as err:
                raise urllib.request.URLError(err)
        else:  
            return None


class HTTPNtlmAuthHandler(AbstractNtlmAuthHandler, urllib.request.BaseHandler):

    auth_header = 'Authorization'

    def http_error_401(self, req, fp, code, msg, headers):
        return self.http_error_authentication_required('www-authenticate', req, fp, headers)


class ProxyNtlmAuthHandler(AbstractNtlmAuthHandler, urllib.request.BaseHandler):
    """ 
        CAUTION: this class has NOT been tested at all!!! 
        use at your own risk
    """
    auth_header = 'Proxy-authorization'

    def http_error_407(self, req, fp, code, msg, headers):
        return self.http_error_authentication_required('proxy-authenticate', req, fp, headers)


if __name__ == "__main__":
    url = "http://ntlmprotectedserver/securedfile.html"
    user = "DOMAIN\\User"
    password = "Password"
    passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, url, user , password)
    auth_basic = urllib.request.HTTPBasicAuthHandler(passman)
    auth_digest = urllib.request.HTTPDigestAuthHandler(passman)
    auth_NTLM = HTTPNtlmAuthHandler(passman)
    
    # disable proxies (just for testing)
    proxy_handler = urllib.request.ProxyHandler({}) 

    opener = urllib.request.build_opener(proxy_handler, auth_NTLM) #, auth_digest, auth_basic)
    
    urllib.request.install_opener(opener)
    
    response = urllib.request.urlopen(url)
    print((response.read()))
