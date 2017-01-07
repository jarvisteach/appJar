brew update
brew install python3
virtualenv venv -p python3
source venv/bin/activate

mkdir -p /opt/mports
cd /opt/mports
svn checkout https://svn.macports.org/repository/macports/trunk

cd /opt/mports/trunk/base
./configure --enable-readline
make
sudo make install
make distclean

export PATH=/opt/local/bin:/opt/local/sbin:$PATH

sudo port install firefox-x11

sudo launchctl load -w /Library/LaunchDaemons/org.freedesktop.dbus-system.plist
sudo launchctl load -w /Library/LaunchAgents/org.freedesktop.dbus-session.plist
launchctl load -w /Library/LaunchDaemons/org.freedesktop.dbus-system.plist
launchctl load -w /Library/LaunchAgents/org.freedesktop.dbus-session.plist
