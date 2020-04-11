import os
import platform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_pref
from selenium.webdriver.firefox.options import Options as firefox_pref


class BrowserFactory:

    def __init__(self):
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.full_path = self.cwd.split('/')
        self.root_dir = '/'.join(self.full_path[:-1])
        os.environ['PYTHONPATH'] = self.root_dir

    def get_browser(self, browser_name, browser_mode):
        current_os = platform.system()
        if browser_name == 'chrome':
            chrome_options = chrome_pref()
            chrome_options.add_argument("--window-size=1280x800")
            if browser_mode == 'headless':
                chrome_options.add_argument("--headless")
            if current_os == 'Linux':  # Linux based operating systems
                return webdriver.Chrome(executable_path=os.path.join(self.root_dir, 'resources/drivers/linux/chromedriver'), options=chrome_options)
            elif current_os == 'Windows':  # Microsoft Windows
                return webdriver.Chrome(os.path.join(self.root_dir, 'resources\drivers\windows\chromedriver.exe'), options=chrome_options)
            elif current_os == 'Darwin':  # Mac OS
                return webdriver.Chrome(os.path.join(self.root_dir, 'resources/drivers/mac/chromedriver'), options=chrome_options)
            else:
                raise Exception('"{}" is not a supported operating system'.format(current_os))
        elif browser_name == 'firefox':
            firefox_options = firefox_pref()
            firefox_options.add_argument("--window-size=1280x800")
            if browser_mode == 'headless':
                firefox_options.add_argument("-headless")
            if current_os == 'Linux':  # Linux based operating systems
                return webdriver.Chrome(os.path.join(self.root_dir, 'resources/drivers/linux/geckodriver'), options=firefox_options)
            elif current_os == 'Windows':  # Microsoft Windows
                return webdriver.Firefox(executable_path=os.path.join(self.root_dir, 'resources\drivers\windows\geckodriver.exe'), options=firefox_options)
            elif current_os == 'Darwin':  # Mac OS
                return webdriver.Chrome(os.path.join(self.root_dir, 'resources/drivers/mac/geckodriver'), options=firefox_options)
            else:
                raise Exception('"{}" is not a supported operating system'.format(current_os))
        else:
            raise Exception('"{}" is not a supported browser'.format(browser_name))
