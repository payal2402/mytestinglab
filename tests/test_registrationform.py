import pytest

from fixture.test_constraints import TestConstraints
from pages.Registrationformpage import RegistrationPage


@pytest.mark.sanity
@pytest.mark.registration
@pytest.mark.xfail


def test_registrationform(driver):
    reg_form_page = RegistrationPage(driver)
    reg_form_page.register(TestConstraints.email)