# TestAutomation

## Introduction
-This Project is an implementation of hybrid test automation framework bases of page object design pattern for selenium-Python using pytest.
-It also has the implementation of API components driven by the principle of hybrid framework.

## Features
- There is a single test "test_compare_temps" in the file TestCases/test_CompareTemps.py which contains the logic to compare the temprature of the different cities from GUI layer and API Layer
- The data is maintained in json format for the testcase under TestData/JSON/TestCases/test_compare_temps.json.
- The ulitilies functions to read json,basic ui functions etc are placed under Ulitilies package.
- The Utlities/properties.ini contains the configuration for test execution
- The PageObject package contains the components of GUI in the form of page objects seggregated by page.
- The APIObject package conation the API layer components
- The Exe contains the ulilities required to execute the batch
- After the execution a report.html is generated under Report folder

## How to

- Clone the repo to the local
- Modify the cities and range (Optional) **
- Double click the Exe/Execute.bat
- After installing the dependencies it will prompt for Browser. Enter "chrome" or "firefox"
- The execution will begin.
- After the execution check the Report/report.html for the execution status

eg:
      "cities": ["New York, NY, US","London"],
      "range": "8"

** To modify the input data 
- open TestData/JSON/TestCases/test_compare_temps.json in notepad
 - modify the first element of the cities with city of your choice for GUI layer. make sure the city should contain state and country as taken by accuweather
 - modify the second element of the cities key with your choice for API layer temp.
 - Modify the value under range to provide your choice of range value

##Pre-requisite

- Operating System : Windows 10
- Browser: Chrome 96.0.4664.110 , Firefox 95.0.2  (Latest Version)
- Python : Python 39 or later



