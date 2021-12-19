pip install -r requirements.txt
cd ../TestCases
@echo off
set /p browser="Enter Browser: "
py.test --Browser=%browser% --html=../Reports/report.html