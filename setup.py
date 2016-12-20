from distutils.core import setup
setup(
    name="appJar",
    packages=["appJar"],
    version="0.02",
    description="A GUI wrapper for tkinter",
    author="Richard Jarvis",
    author_email="info@appjar.info",
    url="http://appJar.info",
    keywords=["python", "gui", "tkinter"],
    classifiers=[],
    package_data = {
        "appJar": ["lib/*", "resources/icons/*", "examples/*"]
    }
)
