import os
import json
import pytest
import parser

from pages import BrowserFactory, LoginPage

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # project folder
CONFIG_PATH = '{}/config.json'.format(ROOT_DIR)  # inside my project folder file->config.json


def pytest_addoption(parser):
    parser.addoption('--TEST_URL', action='store', default='http://mytestinglabs.in', help='Test Enviroment URL')
    parser.addoption('--BROWSER', action='store', default="chrome")
    parser.addoption('--BROWSER_MODE', action='store', default=None)  # head mode/ headless mode

@pytest.fixture(scope='session')
def config():
    # Read the JSON config file and returns it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def driver(config, pytestconfig):
    # Validate and return the wait time choice from the system properties/ config data
    print('IMPLICITLY WAIT TIME: ', os.environ.get('WAIT_TIME'))
    if os.environ.get('WAIT_TIME') is None:   # Jenkins
        implicit_wait = config['wait_time']
        os.environ['WAIT_TIME'] = str(implicit_wait)
    else:
        implicit_wait = os.environ.get('WAIT_TIME')
        config['wait_time'] = implicit_wait

    print('BASE URL: ', pytestconfig.getoption('TEST_URL'))
    base_url = pytestconfig.getoption('TEST_URL')

    # Initialize WebDriver
    browser_factory = BrowserFactory.BrowserFactory()
    driver = browser_factory.get_browser(pytestconfig.getoption('BROWSER'),pytestconfig.getoption('BROWSER_MODE'))

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(implicit_wait)
    driver.get(pytestconfig.getoption('TEST_URL'))
    login = LoginPage.LoginPage(driver)
    login.login()
    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()