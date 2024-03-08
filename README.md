# Wigle-KML-Downloader
Downloads KML's for all of your Wigle runs. Drop your KML's into a Google Earth folder to map all of your discovered networks.

You will need a Wigle account and your 'Encoded for use API'.

I grabbed a beta version of chromedriver from https://googlechromelabs.github.io/chrome-for-testing/ and extracted it.

Put everything in one folder.

Edit the script to change the location of chromedriver and add your API.


Running the script will open a chrome window and gives you 60 seconds to login before continuing the script.
Login to Wigle

Scroll to bottom of your uploaded files and click the 'more results' a few times if your trying to download as many as possible.

The script will continue to download and close when finished.

Added Search_KML's.py
Drop in folder containing your KML's. Run it to search all of your files for a keyword. It will display all files and their
respective line numbers of your search term.

* Only tested on Windoze


Here's Wigle's https://wigle.net/jigle/kml_filter.py which may be of use.
Combines one or more KML files exported from your WiGLE.net uploads page
into a single, bucketed output KML file. Relies upon WiGLE description
strings for categorization (likely won't work with other KML export tools)
To install, you'll need fastkml and combined requirements - see:
   https://github.com/cleder/fastkml
Copyright (c) 2010-2021, Andrew Carra, Robert Hagemann, Hugh Kennedy
All rights reserved.
