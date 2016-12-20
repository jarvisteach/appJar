from distutils.core import setup
setup(
    name="appJar",
    packages=["appJar"],
    version="0.19",
    description="A GUI wrapper for tkinter",
    author="Richard Jarvis",
    author_email="info@appjar.info",
    url="https://github.com/jarvisteach/appJar",
    download_url="http://github.com/jarvisteach/appJar/tarball/0.19",
    keywords=["python", "gui", "tkinter"],
    classifiers=[],
    include_package_date = True,
    package_data = {
        "appJar": ["lib/*", "resources/icons/*"]
    }
)
