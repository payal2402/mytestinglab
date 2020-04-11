import os
import platform
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = '{}\config.json'.format(ROOT_DIR)
print(ROOT_DIR)
print(ROOT_DIR.split('/'))
print(CONFIG_PATH)
os.environ['WAIT_TIME'] = "10"
print(os.environ.get('WAIT_TIME'))
print(platform.system())  # Windows, Linux, Darwin
