from distutils.core import setup
setup(
    name="appJar",
    packages=["appJar"],
    version="0.93.0",
    description="An easy-to-use, feature-rich GUI wrapper for tkinter. Designed specifically for use in the classroom, but powerful enough to be used anywhere.",
    author="Richard Jarvis",
    author_email="info@appjar.info",
    url="http://appJar.info",
    keywords=["python", "gui", "tkinter"],
    license="Apache 2.0",
    classifiers=[
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

    ],
    package_data = {
        "appJar": ["lib/*.py", "lib/*.txt", "lib/tkdnd2.8/*.tcl", "lib/tkdnd2.8/tcl_files/*.tcl", "lib/tkdnd2.8/tcl_libs/*", "resources/icons/*", "examples/showcase.py"]
    }
)
