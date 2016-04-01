#!/usr/bin/python
"""
Library with scraper functionality to be shared among all scraper instances.
"""
import os
import urllib2
import logging
import logging.handlers
# import selenium
from bs4 import BeautifulSoup


class ScrapeEnvironment:
    def __init__(self, url):
        self.url = url
        self.soup = None

        # Install default logger
        self.logger = None
        self._init_logging()

    def _init_logging(self):
        """Declaration of the logging mechanism"""
        try:
            # Set up a specific logger with our desired output level
            logfile = 'scrape.log'
            if not os.path.isfile(logfile):
                with open(logfile, 'w') as log_file:
                    pass
            # General logger
            self.logger = logging.getLogger('default-logger')
            self.logger.setLevel(logging.INFO)
            # Add the log message handler to the logger
            handler = logging.handlers.RotatingFileHandler(logfile, maxBytes=1048576, backupCount=5)  # size= 1MB
            _format = ("%(asctime)s " + "%(levelname)s -> %(message)s")
            _format = logging.Formatter(_format)
            handler.setFormatter(_format)
            self.logger.addHandler(handler)

        except:
            print "No logging"
            exit()

    def load(self, url):
        try:
            self.soup = BeautifulSoup(urllib2.urlopen(url).read(), "html.parser")
            return self.soup
        except:
            self.logger.exception("Can't open webpage for scraping")

    def pretty_print(self):
        """
        Prettify the webpage source with Beautifulsoup and print to stdout
        """
        print self.soup.prettify()


class WebPage:
    def __init__(self):
        pass
