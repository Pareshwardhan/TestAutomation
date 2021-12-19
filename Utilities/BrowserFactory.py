class BrowserFactory():
    browsers = {}
    def __init__(self):

        self.browsers['chrome']="webdriver.Chrome(executable_path=\"..\Exe\chromedriver.exe\")"
        self.browsers['firefox']="webdriver.Firefox(executable_path=\"..\Exe\geckodriver.exe\")"

    def get_browser(self,browser):
        return self.browsers.get(browser)


