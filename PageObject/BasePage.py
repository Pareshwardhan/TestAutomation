from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self,driver):
        self.driver=driver


    def send_keys_ext(self,locator,text,timeout=8):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(expected_conditions.presence_of_element_located(locator))
            self.driver.find_element(*locator).send_keys(text)
        except TimeoutException as exception:
            assert False, exception.msg

    def get_element_text(self,locator,timeout=8):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(expected_conditions.presence_of_element_located(locator))
            return self.driver.find_element(*locator).text
        except TimeoutException as exception:
            assert False, exception.msg


    def js_exuctor_click(self,locator):
        try:
            element=self.driver.execute_script('return '+locator)
            element.click()
        except TimeoutException as exception:
            assert False, exception.msg




