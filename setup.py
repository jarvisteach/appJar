from setuptools import setup, find_packages

__name__ =          "appJar"
__version__ =       "0.94.0"
__author__ =        "Richard Jarvis"
__desc__ =          "An easy-to-use, feature-rich GUI wrapper for tKinter. Designed specifically for use in the classroom, but powerful enough to be used anywhere."
__author_email__ =  "info@appjar.info"
__license__ =       "Apache 2.0"
__url__ =           "http://appJar.info"
__keywords__ =      ["python", "gui", "tkinter", "appJar", "interface"]
__packages__=       ["appJar"]
__classifiers__ = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Education',
    'Topic :: Software Development',
    'Topic :: Software Development :: User Interfaces',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: Apache Software License',
]
__long_description__ = """# appJar
Simple tKinter GUIs in Python.
"""

setup(
    name=__name__,
    packages=__packages__,
    version=__version__,
    description=__desc__,
    long_description=__long_description__,
    long_description_content_type="text/markdown",
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    keywords=__keywords__,
    license=__license__,
    classifiers=__classifiers__,
    package_data = {
        "appJar": ["lib/*.py", "lib/*.txt", "lib/tkdnd2.8/*.tcl", "lib/tkdnd2.8/tcl_files/*.tcl", "lib/tkdnd2.8/tcl_libs/*", "resources/icons/*", "examples/showcase.py", "PYPI.md"]
    }
)
