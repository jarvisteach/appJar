#What's New?
---

* Version 0.05  
    * [Open Container](/pythonWidgetGrouping/#reopening-containers) - implemented issue 83, now possible to reopen a container, perform operations on it, and close it again.  
    * Changed disable entry to readonly, allows entries to be copied (#86)

* Version 0.041  
    * Continuous Integration - added [landscape.io](https://landscape.io/github/jarvisteach/appJar/) to monitor code quality
    * [Reload Image](/pythonImages/#change-images) - funciton to force a reload of an image, bypassing the cache (issue 87)  
    * Minor fixes based off landscape report
    * Issues Resolved:
        * 87 - reloadImage()
        * 84 - Removed requirement for appJar icon in Windows  

* Version 0.04  
    * [Internationalisation](/pythonInternationalisation) - it's now possible to support multiple languages, by adding simple config files.
    * [Splashscreen](/splash) - a simple splashscreen is now available.  
    * [AutoCompletion EntryBox](/pythonWidgets/#entry) - added a new widget, giving autocompletion in EntryBoxes  
    * [Function on change](/pythonEvents/#make-stuff-happen) in ListBox - now possible to call a function each time a ListBox changes  
    * [Python 3.6 Support](https://docs.python.org/3.6/whatsnew/3.6.html#idlelib-and-idle) - now supports python3.6 - fixed issue with renamed idelib files  
    * Continuous Integration - now uses [Travis-CI](https://travis-ci.org/jarvisteach/appJar) and [Coveralls](https://coveralls.io/github/jarvisteach/appJar) to check for errors on each commit
    * Updated documentation: Rearrangement of navigation bar, new pages for new features, minor modifications.  
    * Issues Resolved:
        * 81 - now allows negative numbers/decimals to be entered correctly in NumericEntries  
        * 80 - now support Python 3.6
        * 78 - fixed typo in documentation
        * 74 - SplashScreen
        * 72 - Unit testing
        * 71 - Internationalisation
        * 70 - AutoComplete EntryBox
