from selenium.webdriver.common.by import By

from PageObject.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)


    search_box=(By.XPATH,"//input[@name='query']")
    js_search_icon='document.getElementsByClassName("icon-search search-icon")[0]'

    def search_city(self,city_name):
        self.send_keys_ext(self.search_box,city_name)
        self.js_exuctor_click(self.js_search_icon)

    def goto(self,url):
        self.driver.get(url)





