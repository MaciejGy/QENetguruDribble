from base.BasePage import BasePage
import utilities.custom_logger as cl
import logging


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "//a[contains(text(), 'Sign in')]"
    _email_field = "login"
    _password_field = "password"
    _login_button = "form-sub"
    _login_error = "//h2[contains(text(), 'try again')]"
    _login_success = "site-nav-avatar"
    _rate_limit = "/h1[contains(text(), 'rate limited')]"


    def clickLoginLink(self):
        self.elementClick(self._login_link, "xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, "class")

    def login(self, username="", password=""):
        self.clickLoginLink()
        self.enterEmail(username, self._email_field)
        self.enterPassword(password, self._password_field)
        self.clickLoginButton()

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._login_error, "xpath")
        return result

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._login_success, "class")
        return result

    def verifyRateLimit(self):
        result = self.isElementPresent(self._rate_limit, "xpath")
        return result

