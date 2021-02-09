from pages.homepage.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    def test_validLogin(self):
        self.lp.login("TestAccountNG", "password!")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result1, "LoginFailed")
