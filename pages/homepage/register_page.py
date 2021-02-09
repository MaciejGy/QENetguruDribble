from base.BasePage import BasePage
import utilities.custom_logger as cl
import logging


class RegisterPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _register_link = "//a[contains(text(), 'Sign up')]"
    _name_field = "user_name"
    _username_field = "user_login"
    _email_field = "user_email"
    _password_field = "user_password"
    _create_button = "//input[@value='Create Account']"
    _terms_button = "//label[contains(text(), 'Creating an account')]"
    _google_sign = "auth-google"
    _twitter_sign = "auth-twitter"
    _error_field = "errorExplanation"

    def clickRegisterLink(self):
        self.elementClick(self._register_link, "xpath")

    def enterName(self, name):
        self.sendKeys(name, self._name_field)

    def enterUsername(self, username):
        self.sendKeys(username, self._username_field)

    def acceptTerms(self):
        self.elementClick(self._terms_button, "xpath")

    def clickCreate(self):
        self.elementClick(self._create_button, "xpath")

    def googleSign(self):
        self.elementClick(self._google_sign, "class")

    def twitterSign(self):
        self.elementClick(self._twitter_sign, "class")

    def regularRegister(self, name="", username="", email="", password=""):
        self.clickRegisterLink()
        self.enterName(name)
        self.enterUsername(username)
        self.enterEmail(email, self._email_field)
        self.enterPassword(password, self._password_field)
        self.acceptTerms()
        self.clickCreate()

    def verifyRegisterFailed(self):
        result = self.isElementPresent(self._error_field)
        return result
