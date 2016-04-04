#!/usr/bin/python
"""
Experimental scraper module
"""
import time
from utils.scrape_environment import StaticEnvironment
from utils.scrape_environment import DynamicEnvironment


class BeautifulSoupExample(StaticEnvironment):
    def __init__(self, url):
        StaticEnvironment.__init__(self, url)
        self.base_url = 'http://buienradar.nl/'

    def get_5_day_forecast(self):
        url = self.base_url + 'weerbericht-nederland'
        self.logger.info("About to fetch weather data from {0}".format(url))
        start_time = time.time()
        soup = self.load(url)
        try:
            content = soup.find('div', {"id": "content"})  # narrow down to content
            weather_section = content.findAll("div", {"class": "fs_weatherday"})  # extract weather section
            for day in weather_section:
                text_day = day.find('span', {"class": "fs_daytext"}).text
                text_min_temp = day.find('span', {"class": "fs_mintemp"}).text
                text_min_temp = ''.join([i if ord(i) < 128 else '' for i in text_min_temp])  # strip non-ASCII
                text_max_temp = day.find('span', {"class": "fs_maxtemp"}).text
                text_max_temp = ''.join([i if ord(i) < 128 else '' for i in text_max_temp])  # strip non-ASCII

                scraper.logger.info("{0} is de minimum temperatuur {1} graden en maximum temperatuur {2} graden".format(
                    text_day, text_min_temp, text_max_temp))
        except:
            self.logger.exception("Can't find element")
        else:
            self.logger.info("Successfully fetched weather information from {0}".format(url))
        finally:
            self.logger.info("Beautifulsoup took {0:d} ms".format(int((time.time()-start_time)*1000)))


class PythonSeleniumExample(DynamicEnvironment):
    def __init__(self, url):
        DynamicEnvironment.__init__(self)

    def run(self):
        start_time = time.time()
        self.load("http://www.python.org")
        self.logger.info("Selenium took {0:d} ms".format(int((time.time() - start_time) * 1000)))


if __name__ != 'main':
    scraper = BeautifulSoupExample('http://buienradar.nl/weerbericht-nederland')
    try:
        scraper.get_5_day_forecast()
    except:
        scraper.logger.exception("Can't fetch 5 day forecast, see log")

    scraper = PythonSeleniumExample("http://www.python.org")
    try:
        scraper.run()
    except:
        scraper.logger.exception("Exception running selenium on python.org")


