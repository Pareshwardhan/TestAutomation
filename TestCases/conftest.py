import pytest
import requests

from Utilities.BrowserFactory import BrowserFactory
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--Browser", action="store", default="chrome")
    parser.addoption("--APISite",action="store",default="accuweather")
    parser.addoption("--GUISite", action="store", default="accuweather")


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--Browser")
    driver = eval(BrowserFactory().get_browser(browser))
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.requests=requests
    request.cls.gui_url=request.config.getoption("--GUISite")
    request.cls.api_url = request.config.getoption("--APISite")
    yield
    driver.close()
