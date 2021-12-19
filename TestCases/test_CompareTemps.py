from APIObjects.GetAPI import GetAPI
from PageObject.HomePage import HomePage
from PageObject.WeatherPage import WeatherPage
from Utilities.BaseTest import BaseTest
from Utilities.TempExceedsRangeError import TempExceedsRangeError


class TestCompareTemps(BaseTest):

    def test_compare_temps(self):
        driver = self.driver
        logger = self.init()
        requests = self.requests

        """-----------------------------GUI Layer ______________________________________"""
        """home page operations"""
        """getting the object of home page"""
        homepage = HomePage(driver)
        """launching the accuweather website """
        homepage.goto(self.gui_url)
        logger.info("Launched the home page of accuweather")
        """fetching the city value from json testdata"""
        city1=self.testdata["cities"][0]
        """performing the search operation """
        homepage.search_city(city1)
        logger.info(f"Entered the text in the search textbox as {city1} and clicked on the search icon")

        """search result weather page operations"""

        """Creating the object of the weather page"""
        weatherpage = WeatherPage(driver)
        """fetching the current temperature of the city city1"""
        temp = weatherpage.get_city_temp()
        logger.info(f"Got the temperature from GUI layer as  {temp} degree celsius for the city {city1}")



        """-----------------------API Layer-------------------------------------------"""
        """Creating the HetAPI object"""
        getapi = GetAPI(requests, self.api_url)
        """ fetching the city form json testdata"""
        city2=self.testdata["cities"][1]
        """Fetching the tempetaure from  response data obtained after performing the get operation"""
        temp1 = getapi.get_temp_by_city(city2)

        logger.info(f"Got the temperature from API layer as {temp1} degree celsius for teh city {city2}")

        """Comparator and Variance logic """
        if abs(temp1-temp)>float(self.testdata["range"]):
            raise TempExceedsRangeError("temp exceeded")


