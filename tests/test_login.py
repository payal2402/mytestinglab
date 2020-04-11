
from utils.CommonActions import CommonActions


def test_login_status(driver):
    org_name = CommonActions(driver)
    assert org_name.get_logo_name() == 'MyTestingLabs'


