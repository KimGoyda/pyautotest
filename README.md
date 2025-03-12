# pyautotest

Chrome Driver install
1. Download ChromeDriver https://storage.googleapis.com/chrome-for-testing-public/133.0.6943.141/win64/chromedriver-win64.zip
2. Extract ChromeDriver in your folder
3. Add rout driver to system var PATH

Command for start autotests
pytest -v --tb=line --reruns 1 --browser=chrome test_rerun.py