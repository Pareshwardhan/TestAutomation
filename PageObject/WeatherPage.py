from selenium.webdriver.common.by import By

from PageObject.BasePage import BasePage


class WeatherPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    temp_text=(By.XPATH,"//div[@class='temp']")

    def get_city_temp(self):
        temp=self.get_element_text(self.temp_text)
        new_temp = ""
        for l in temp:
            if l.isdigit():
                new_temp = new_temp + l
        return float(new_temp)





