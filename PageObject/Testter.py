import json

from Utilities.Configuration import Configuration


with open('../TestData/JSON/TestCases/test_compare_temps.json') as f:
    jsontext=json.load(f)

print(jsontext['cities'])

