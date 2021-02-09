from pages.homepage.register_page import RegisterPage
import unittest
import pytest
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp")
class RegisterTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.rp = RegisterPage(self.driver)
        self.ts = TestStatus(self.driver)

    def test_accountExists(self):
        self.rp.regularRegister("Test", "TestAccountNG", "netguru@niepodam.pl", "password!")
        result1 = self.rp.verifyRegisterFailed()
        self.ts.markFinal("test_accountExists", result1, "RegisterProblem")
