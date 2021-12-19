import inspect
import json
import logging

import pytest

from Utilities.Configuration import Configuration
from Utilities.JSONUtills import JSONUtils


@pytest.mark.usefixtures("setup")
class BaseTest:

    def init(self):
        configuration = Configuration()
        self.gui_url=configuration.getconfig()['GUI'][self.gui_url]
        self.api_url = configuration.getconfig()['API'][self.api_url]
        self.testname=inspect.stack()[1][3]
        jsonutils=JSONUtils()
        self.testdata=jsonutils.load_data_from_file(f'../TestData/JSON/TestCases/{self.testname}'+'.json')
        return self.get_logger(self.testname)


    def get_logger(self,loggerName):
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger