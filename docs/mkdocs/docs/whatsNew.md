#Change-Log
---

## Version 0.9  
* Introduction of alternative [widget access functions](/simpleAppJar) ([#235](https://github.com/jarvisteach/appJar/issues/235))  - now possible to **ADD**, **SET** & **GET** widgets by just using their name.  
* Introduction of alternative [GUI properties](/simpleAppJar) ([#340](https://github.com/jarvisteach/appJar/issues/340)) - now possible to GET/SET properties with special property functions  
* Introduction of appJar [settings](/pythonSettings/) - can now save/load GUI state to/from file.  
* Big improvements to [grids](/pythonDevWidgets/#grid) - can add/remove/replace rows/columns, can sort data, can access a right-click menu, can connect to an sqlite database.  
* More [ttk](/pythonTtk) improvements - grouped widgets now work, introduced external themes.  

* Issues Resolved:
    * [#344](https://github.com/jarvisteach/appJar/issues/344) - [labels](/pythonWidgets/#add-labels) now display the title when no text is provided, instead of an empty label.  
    * [#343](https://github.com/jarvisteach/appJar/issues/343) - new parameter for appJar constructor: `showIcon` allows the icon to be ignored when running Wondows
    * [#340](https://github.com/jarvisteach/appJar/issues/340) - introduced [GUI properties](/simpleAppJar) for most settings  
    * [#339](https://github.com/jarvisteach/appJar/issues/339) - new functions to remove [toolbars](/pythonBars/#set-toolbars) and [statusbars](/pythonBars/#set-statusbars)    
    * [#335](https://github.com/jarvisteach/appJar/issues/335) - when setting functions for events, if no parameter is present in the function, no parameter will be passed by the event  
    * [#333](https://github.com/jarvisteach/appJar/issues/333) - started work on hide/show/delete [tabs](/pythonWidgetGrouping/#tabbed-frame)  
    * [#325](https://github.com/jarvisteach/appJar/issues/325) - fixed issue with [right-click menus](/pythonBars/#platform-specificcustom-menus)
    * [#324](https://github.com/jarvisteach/appJar/issues/324) - fixed issue with losing [file/directory Entry](/pythonWidgets/#entry) values  
    * [#317](https://github.com/jarvisteach/appJar/issues/317) - implemented fonts on [tabbed frames](/pythonWidgetGrouping/#tabbed-frame)  
    * [#316](https://github.com/jarvisteach/appJar/issues/316) - can now display compound images and text in [buttons](/pythonWidgets/#button)  
    * [#309](https://github.com/jarvisteach/appJar/issues/309) - cleaned up handling of [fonts](/pythonGuiOptions/#font)  
    * [#303](https://github.com/jarvisteach/appJar/issues/303) - added functions to [bind/unbind mutiple keys](/pythonEvents/#binding-keys) to a function  
    * [#298](https://github.com/jarvisteach/appJar/issues/298) - fixed issue in [menubar shortcuts](/pythonBars/#extra-features/) where numeric shortcuts didn't work.  
    * [#296](https://github.com/jarvisteach/appJar/issues/296) - two new widgets introduced [turtle](/pythonDevWidgets/#turtle) and [canvas](/pythonDevWidgets/#canvas)  
    * [#294](https://github.com/jarvisteach/appJar/issues/294) & [#292](https://github.com/jarvisteach/appJar/issues/292) - fixes on [entries](/pythonWidgets/#entry): better handle arrow key presses on mac, defaults work better on secret entries & file/directory entries  
    * [#290](https://github.com/jarvisteach/appJar/issues/290) - fixed issue showing [AutoEntries](/pythonWidgets/#entry) in [subWindows](/pythonSubWindows)  
    * [#289](https://github.com/jarvisteach/appJar/issues/289) - new functions to change list in [AutoEntries](/pythonWidgets/#entry) 
    * [#288](https://github.com/jarvisteach/appJar/issues/288) - fixed issue showing [dialogs](/pythonDialogs/#message-boxes) in [subWindows](/pythonSubWindows)  
    * [#286](https://github.com/jarvisteach/appJar/issues/286) - added new [threaded callback](/pythonThreads), contributed by [@mpmc](https://github.com/mpmc)
    * [#284](https://github.com/jarvisteach/appJar/issues/284) - new [dialogs](/pythonDialogs/#message-boxes) for strings, integers & floats  
    * [#283](https://github.com/jarvisteach/appJar/issues/283) - [questionBox](/pythonDialogs/#question-boxes) now returns Booleans instead of yes/no  
    * [#281](https://github.com/jarvisteach/appJar/issues/281) - resolved issues with [threads](/pythonThreads)  
    * [#279](https://github.com/jarvisteach/appJar/issues/279) - tidied up [remove all widgets](/pythonWidgetOptions/#widget-manipulation) - now leaves GUI looking better  
    * [#271](https://github.com/jarvisteach/appJar/issues/271), [#266](https://github.com/jarvisteach/appJar/issues/266), [#255](https://github.com/jarvisteach/appJar/issues/255) & [#232](https://github.com/jarvisteach/appJar/issues/232) - [Grid](/pythonDevWidgets/#grid) improvements  
    * [#242](https://github.com/jarvisteach/appJar/issues/242), [#259](https://github.com/jarvisteach/appJar/issues/259), [#267](https://github.com/jarvisteach/appJar/issues/267) - work on [MatPLotLib](/pythonDevWidgets/#matplotlib) now support multiple plot types, and retaining some settings  
    * [#250](https://github.com/jarvisteach/appJar/issues/250) - Can now add [compound images](/python/Images/#add-images) - images with a built in label  
    * [#236](https://github.com/jarvisteach/appJar/issues/236) - appJar can now save GUI [settings](/pythonSettings) and load them again  
    * [#233](https://github.com/jarvisteach/appJar/issues/233) - [NumericEntries](/pythonWidgets/#entry) return `None` when empty
    * [#218](https://github.com/jarvisteach/appJar/issues/218) - Can no longer set [NumericEntries](/pythonWidgets/#entry) to Strings  

## Version 0.82.1
* Issues Resolved:
    * [#275](https://github.com/jarvisteach/appJar/issues/275) - maps fix  

## Version 0.82
* Issues Resolved:
    * [#189](https://github.com/jarvisteach/appJar/issues/189) - some tweaks to [ttk support](/pythonTtk)  
    * Fixes to documentation

## Version 0.8  
* Changed versioning - PyPi difficulties, combined with close to a 1.0 release...
* Create a GUI in **TWO** lines using [context managers](/pythonContextManager/) - appJar now allows you to use `with` to create a GUI and [containers](/pythonWidgetGrouping)  
* [Events](/pythonEvents/), [Threads](/pythonThreads/), [Loops & Sleeps](/pythonLoopsAndSleeps/) have been improved. It's now possible to run background tasks (such as a download) and update the GUI safely.   
* [Command line arguments](/pythonCommandLine): appJar now supports command line arguments for [logging](/pythonLogging) and [internationalisation](/pythonInternationalisation/) as well as help & version information.  
* [Internationalisation](/pythonInternationalisation/) is now greatly improved - nearly everything supports multiple languages.  
* [ScrollPanes](/pythonWidgetGrouping/#scroll-pane) & [Grids](/pythonDevWidgets/#grid) greatly improved  
* Much more friendly [license](/License/)  

* Issues Resolved:
    * [#249](https://github.com/jarvisteach/appJar/issues/249) - Can now set a parent for [dialogs](/pythonDialogs/) so that if they are launched from a [SubWindow](/pythonWidgetGrouping/#sub-window) they behave properly.  
    * [#248](https://github.com/jarvisteach/appJar/issues/248) - Can now [add icons](/pythonImages/#add-images) and [iconButtons](/pythonWidgets/#add-buttons) using inbuilt icon set.  
    * [#246](https://github.com/jarvisteach/appJar/issues/246) - Can now hide titles on [labelFrames](/pythonWidgetGrouping/#label-frame)  
    * [#243](https://github.com/jarvisteach/appJar/issues/243) - Fixed bug in [ToggleFrames](/pythonWidgetGrouping/#toggle-frame)  
    * [#241](https://github.com/jarvisteach/appJar/issues/241) - Notes on installing on [linux](/Install/#single-user-set-up)  
    * [#234](https://github.com/jarvisteach/appJar/issues/234) - Support for [ContextManagers](/pythonContextManager/) throughout appJar  
    * [#228](https://github.com/jarvisteach/appJar/issues/228) - appJar prevents you from creating more than one gui at a time  
    * [#226](https://github.com/jarvisteach/appJar/issues/226) - fixed issues on [file/directory entries](/pythonWidgets/#entry)  
    * [#223](https://github.com/jarvisteach/appJar/issues/223) - fixed issues with [sound](/pythonSound/) import  
    * [#217](https://github.com/jarvisteach/appJar/issues/217) - Fixed issues with removing [BG images](/pythonImages/#set-background-images)  
    * [#216](https://github.com/jarvisteach/appJar/issues/216) - Improvements to [integrated testing](https://travis-ci.org/jarvisteach/appJar)  
    * [#215](https://github.com/jarvisteach/appJar/issues/215) - Changed [licensing](/License/)  
    * [#213](https://github.com/jarvisteach/appJar/issues/213) - Validation entries improved in [Internationalisation](/pythonInternationalisation)  
    * [#212](https://github.com/jarvisteach/appJar/issues/212) - Creating an empty [Tooltip](/pythonDialogs/#tooltips) now doesn't create anything  
    * [#211](https://github.com/jarvisteach/appJar/issues/211) - [Logging](/pythonLogging) now logs line number & function name  
    * [#209](https://github.com/jarvisteach/appJar/issues/209) - Additional testing for [ScrollPanes](/pythonWidgetGrouping/#scroll-pane) & [Grids](/pythonDevWidgets/#grid)  
    * [#207](https://github.com/jarvisteach/appJar/issues/207) - Now possible to change the title and anchor of a [LabelFrame](/pythonWidgetGrouping/#label-frame)  
    * [#206](https://github.com/jarvisteach/appJar/issues/206) - New method for [pausing functions](/pythonEvents/#user-actions) when stopping infinite loops  
    * [#205](https://github.com/jarvisteach/appJar/issues/205) - Now possible to [select](/pythonWidgets/#set-optionboxes) a disabled item in an OptionBox.  
    * [#204](https://github.com/jarvisteach/appJar/issues/204) - appJar now supports [Command line arguments](/pythonCommandLine)  
    * [#203](https://github.com/jarvisteach/appJar/issues/203) - updated docs on [LabelFrames](/pythonWidgetGrouping/#label-frame)  
    * [#202](https://github.com/jarvisteach/appJar/issues/202) - functions now provided to get or clear all values of a selected widget type  
    * [#200](https://github.com/jarvisteach/appJar/issues/200) - Switched [Grid](/pythonDevWidgets/#grid) to use a [ScrollPane](/pythonWidgetGrouping/#scroll-pane) & changed ScrollPane to use AutoScrollbars.  
    * [#196](https://github.com/jarvisteach/appJar/issues/196) - Resolved issue with configuing [ScrolledTextAreas](/pythonWidgets/#textarea)  
    * [#189](https://github.com/jarvisteach/appJar/issues/189) - More work on [ttk](/pythonTtk)  
    * [#177](https://github.com/jarvisteach/appJar/issues/177) - [setLocation](/pythonGuiOptions/#size-location) can now position windows in the center of the screen
    * [#162](https://github.com/jarvisteach/appJar/issues/162) - PhotoImage objects can now be passed directly when [adding/setting ImageData](/pythonImages/#add-images)  
    * [#132](https://github.com/jarvisteach/appJar/issues/132) - Now possible to [Delete and Rename](/pythonWidgets/#set-optionboxes) OptionBox items.
    * [#120](https://github.com/jarvisteach/appJar/issues/120) - Improvements to [events](/pythonEvents/) & introduction of [threading](/pythonEvents/)  
    * [#71](https://github.com/jarvisteach/appJar/issues/71) - More work on [Internationalisation](/pythonInternationalisation/) - now supports Images, LabelFrames, ToggleFrames, TabbedFrames, Properties, Grids, Toolbars, Tooltips, SubWindows, PagedWindows, SplashScreens & Titles  
    * [#69](https://github.com/jarvisteach/appJar/issues/69) - Changes to [TextAreas](/pythonWidgets/#textarea) - now, lines wrap on spaces & [setTextArea()](/pythonWidgets/#set-textareas) now appends to the text  


## Version 0.07  
* New widgets: [GoogleMaps](/pythonDevWidgets/#googlemaps) - a widget to show a GoogleMap tile & control widgets, [ImageMaps](/pythonImages/#image-maps) - clickable ImageMap with linked functions, [FileEntries](/pythonWidgets/#entry) - Entries linked with File/Directory dialogs  
* Widget enhancements: [Pinnable Toolbars](/pythonBars/#set-toolbars), [SelectableLabels](/pythonWidgets/#add-labels), better [Tooltips](/pythonDialogs/#tooltips), [NamedCheckBoxes](/pythonWidgets/#add-checkboxes) & settable [ListBoxes](/pythonWidgets/#set-listboxes)  
* Update to event model and [documentation](/pythonEvents) - now clearer how to perform different actions, and function names updated.  
* Switched to Python's [logging](/pythonLogging) feature


* Issues Resolved:
    * [#192](https://github.com/jarvisteach/appJar/issues/192) - Fixed PNG image support in python 2.7 - specifically for toolbars  
    * [#189](https://github.com/jarvisteach/appJar/issues/189) - **VERY** basic support for [ttk](/pythonDevWidgets/#ttk)
    * [#186](https://github.com/jarvisteach/appJar/issues/186) - Changes to [Unicode](/specialCharacters) support  
    * [#185](https://github.com/jarvisteach/appJar/issues/185) - All add functions now return the widget  
    * [#184](https://github.com/jarvisteach/appJar/issues/184) - [Groupable List Boxes](/pythonWidgets/#set-listboxes)
    * [#182](https://github.com/jarvisteach/appJar/issues/182) - Added a link to source for [GoogleMaps](/pythonDevWidgets/#googlemaps)
    * [#181](https://github.com/jarvisteach/appJar/issues/181) - [Disabling toolbars](/pythonBars/#set-toolbars) will also disable a pinned icon
    * [#180](https://github.com/jarvisteach/appJar/issues/180) - [SlowActions](/pythonEvents/#slow-actions)  
    * [#176](https://github.com/jarvisteach/appJar/issues/176) - Fixed issue with placing container in [containers](/pythonWidgetGrouping)  
    * [#173](https://github.com/jarvisteach/appJar/issues/173) - New functions to [Set ListBoxes](/pythonWidgets/#set-listboxes)  
    * [#161](https://github.com/jarvisteach/appJar/issues/161) - [NamedCheckBoxes](/pythonWidgets/#add-checkboxes)  
    * [#148](https://github.com/jarvisteach/appJar/issues/148) - Improved support for [MouseOver Events](/pythonEvents/#user-actions)  
    * [#151](https://github.com/jarvisteach/appJar/issues/151) & [#158](https://github.com/jarvisteach/appJar/issues/158) - Some fixes to [Grid Widget](/pythonDevWidgets/#grid)  
    * [#138](https://github.com/jarvisteach/appJar/issues/138) - Can now register a [Change Event](/pythonWidgets/#set-datepicker) on DatePicker  
    * [#137](https://github.com/jarvisteach/appJar/issues/137) - [File Entries](/pythonWidgets/#entry)  
    * [#136](https://github.com/jarvisteach/appJar/issues/136) - Simple [GoogleMaps](/pythonDevWidgets/#googlemaps) widget   
    * [#135](https://github.com/jarvisteach/appJar/issues/135) - A clickable [Image Map](/pythonImages/#image-maps)  
    * [#133](https://github.com/jarvisteach/appJar/issues/133) - Improvements to [Tooltips](/pythonDialogs/#tooltips)  
    * [#124](https://github.com/jarvisteach/appJar/issues/124) - Switched to Python's [logging](/pythonLogging) feature  
    * [#101](https://github.com/jarvisteach/appJar/issues/101) - More work implementing [Drag n'Drop](/pythonDnD)  
    * [#73](https://github.com/jarvisteach/appJar/issues/73) - Toolbars are now [pinnable](/pythonBars/#set-toolbars)  
    * [#59](https://github.com/jarvisteach/appJar/issues/59) - [SelectableLabels](/pythonWidgets/#add-labels)  
    * [#7](https://github.com/jarvisteach/appJar/issues/7) -  Can now [Set Foreground](/pythonGuiOptions/#colour) across the whole GUI  

## Version 0.061  

* Issues Resolved:  
    * [#154](https://github.com/jarvisteach/appJar/issues/154) - Fixed bug with AutoEntry not showing drop-down in right position, when placed in a container  

## Version 0.06  
* New widgets: [MicroBit](/pythonDevWidgets/#microbit-emulator), [Validation Entries](/pythonWidgets/#entry)  
* Widget enhancements: Can now set some rules for [entries](/pythonWidgets/#set-entries)  
* New documentation: [packaging](/packaging), [special characters](/specialCharacters), [events](/pythonEvents), [drag'n drop](/pythonDnD)  
* Work on events: [stopping event propagation](/pythonEvents/#breakdown), [drag/over events](/pythonEvents/#make-stuff-happen), [drag'n drop](/pythonDnD)  
* Issues Resolved:  
    * [#143](https://github.com/jarvisteach/appJar/issues/143) - Fixed bug with setting defaults on AutoEntries  
    * [#142](https://github.com/jarvisteach/appJar/issues/142) - Finished documentation for [popups](/pythonDialogs/#file=boxes)  
    * [#130](https://github.com/jarvisteach/appJar/issues/130) - Documented how to use [special characters](/specialCharacters)  
    * [#123](https://github.com/jarvisteach/appJar/issues/123) - New features for [setting entries](/pythonWidgets/#set-entries) - max length, auto uppercase/lowercase, validation  
    * [#119](https://github.com/jarvisteach/appJar/issues/119) - [MicroBit](/pythonDevWidgets/#microbit-emulator) widget added  
    * [#118](https://github.com/jarvisteach/appJar/issues/118) - dynamic library imports  
    * [#117](https://github.com/jarvisteach/appJar/issues/117) - introduced documentation on [packaging](/packaging/)  
    * [#116](https://github.com/jarvisteach/appJar/issues/116) - configurable trough [increments](/pythonWidgets/#set-scales) for a scale  
    * [#115](https://github.com/jarvisteach/appJar/issues/115) - fixed transparency in python 2.7  
    * [#114](https://github.com/jarvisteach/appJar/issues/114) - ability to stop events being propagated  
    * [#112](https://github.com/jarvisteach/appJar/issues/112) - now possible to start with a subWindow (specified in go()) as well as hide() & show() main window  
    * [#110](https://github.com/jarvisteach/appJar/issues/110) - can now configure the number of rows to [show](/pythonWidgets/#set-entries) in an AutoEntry  
    * [#108](https://github.com/jarvisteach/appJar/issues/108) - Fixed issue with modal [SubWindows](/pythonWidgetGrouping/#startstop-sub-windows)  
    * [#106](https://github.com/jarvisteach/appJar/issues/106) - Function to add an [image button](/pythonWidgets/#add-buttons)  
    * [#102](https://github.com/jarvisteach/appJar/issues/102) - Updates to drag/over [events](/pythonEvents/#make-stuff-happen)  
    * [#103](https://github.com/jarvisteach/appJar/issues/103) - Can now manage event calling when [widgets change](/pythonEvents/#make-stuff-happen)  
    * [#101](https://github.com/jarvisteach/appJar/issues/101) - [Drag n'Drop](/pythonDnD.md) beta support for dnd between applications  
    * [#92](https://github.com/jarvisteach/appJar/issues/92) - Function to [get all entries](/pythonWidgets/#get-entries)  
    * [#75](https://github.com/jarvisteach/appJar/issues/75) - Fix to [destroySubWindow](/pythonWidgetGrouping/#showhide-sub-windows)  
    * [#46](https://github.com/jarvisteach/appJar/issues/46) - Added version details to about box  
    * [#42](https://github.com/jarvisteach/appJar/issues/42) - Added functionality to [change TickOptionBoxes](/pythonWidgets/#set-optionboxes)  
    * [#33](https://github.com/jarvisteach/appJar/issues/33) - Added convenience function to [setTreeColours](/pythonDevWidgets/#tree)  

## Version 0.052  
* Issues Resolved:  
    * [#114](https://github.com/jarvisteach/appJar/issues/114) - ability to stop functions being called when a set method is activated

## Version 0.051  
* Issues Resolved:  
    * [#109](https://github.com/jarvisteach/appJar/issues/109) - Labelled Auto Entry, contributed by [jacobthetechy](https://github.com/jacobthetechy)

## Version 0.05  
* [Open Container](/pythonWidgetGrouping/#reopening-containers) - implemented issue [#83](https://github.com/jarvisteach/appJar/issues/83), can now reopen a container, perform operations on it, and close it.  
* Changed disable entry to readonly, allows entries to be copied ([#86](https://github.com/jarvisteach/appJar/issues/86))  
* Images now support [raw image data](/pythonImages/#add-images).  
* Setters now call any registered functions  
* Rewrite of [Meters](/pythonWidgets/#meter), proper inheritance, all use gradated fill, Dual/Split Meter swapped ([#65](https://github.com/jarvisteach/appJar/issues/65)).  
* Rewrite of [ScrollPane](/pythonWidgetGrouping/#scroll-pane), multi-platform scrolling...
* Added functions to [change the bg/fg](/pythonWidgets/#listbox) of ListBox items ([#97](https://github.com/jarvisteach/appJar/issues/97)).  
* Issues Resolved:  
    * [#101](https://github.com/jarvisteach/appJar/issues/101) & [#103](https://github.com/jarvisteach/appJar/issues/103) - updates to documentation
    * [#99](https://github.com/jarvisteach/appJar/issues/99) - ability to create empty containers  
    * [#97](https://github.com/jarvisteach/appJar/issues/97) - ability to set bg/fg colour of list items
    * [#94](https://github.com/jarvisteach/appJar/issues/94) - basic support for [MatPlotLib](/pythonDevWidgets/#matplotlib)  
    * [#90](https://github.com/jarvisteach/appJar/issues/90) - raw image data  
    * [#89](https://github.com/jarvisteach/appJar/issues/89) - minimum speed for animated image  
    * [#88](https://github.com/jarvisteach/appJar/issues/88) - preload mouse over images  
    * [#86](https://github.com/jarvisteach/appJar/issues/86) - disabled entry now readonly  
    * [#85](https://github.com/jarvisteach/appJar/issues/85) - setters now call function (if available)  
    * [#83](https://github.com/jarvisteach/appJar/issues/83) - can now reopen container  
    * [#65](https://github.com/jarvisteach/appJar/issues/65) - Meter rewrite  
    * [#34](https://github.com/jarvisteach/appJar/issues/34)/[#35](https://github.com/jarvisteach/appJar/issues/35) - ScrollPane rewrite

## Version 0.042  
* Issues Resolved:  
    * [#95](https://github.com/jarvisteach/appJar/issues/95) - fixed issue launching ShowCase under Python 2 (removed icons)  
    * [#93](https://github.com/jarvisteach/appJar/issues/93) - fixed issue with numDialog/textDialog under python 2  

## Version 0.041  
* Continuous Integration - added [landscape.io](https://landscape.io/github/jarvisteach/appJar/) to monitor code quality  
* [Reload Image](/pythonImages/#change-images) - function to force a reload of an image, bypassing the cache (issue [#87](https://github.com/jarvisteach/appJar/issues/87))  
* Minor fixes based off landscape report  
* Issues Resolved:  
    * [#87](https://github.com/jarvisteach/appJar/issues/87) - reloadImage()  
    * [#84](https://github.com/jarvisteach/appJar/issues/84) - Removed requirement for appJar icon in Windows  

## Version 0.04  
* [Internationalisation](/pythonInternationalisation) - it's now possible to support multiple languages, by adding simple config files.  
* [Splashscreen](/splash) - a simple splashscreen is now available.  
* [AutoCompletion EntryBox](/pythonWidgets/#entry) - added a new widget, giving autocompletion in EntryBoxes  
* [Function on change](/pythonEvents/#make-stuff-happen) in ListBox - now possible to call a function each time a ListBox changes  
* [Python 3.6 Support](https://docs.python.org/3.6/whatsnew/3.6.html#idlelib-and-idle) - now supports python3.6 - fixed issue with renamed idelib files  
* Continuous Integration - now uses [Travis-CI](https://travis-ci.org/jarvisteach/appJar) and [Coveralls](https://coveralls.io/github/jarvisteach/appJar) to check for errors on each commit  
* Updated documentation: Rearrangement of navigation bar, new pages for new features, minor modifications.  
* Issues Resolved:  
    * [#81](https://github.com/jarvisteach/appJar/issues/81) - now allows negative numbers/decimals to be entered correctly in NumericEntries  
    * [#80](https://github.com/jarvisteach/appJar/issues/80) - now support Python 3.6  
    * [#78](https://github.com/jarvisteach/appJar/issues/78) - fixed typo in documentation  
    * [#74](https://github.com/jarvisteach/appJar/issues/74) - SplashScreen  
    * [#72](https://github.com/jarvisteach/appJar/issues/72) - Unit testing  
    * [#71](https://github.com/jarvisteach/appJar/issues/71) - Internationalisation  
    * [#70](https://github.com/jarvisteach/appJar/issues/70) - AutoComplete EntryBox  
