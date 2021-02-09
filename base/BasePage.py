"""
@package base

Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
from base.selenium_driver import SeleniumDriver

class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver

    """
    Four below methods can be easily applied to both Login and Register pages
    """

    def enterEmail(self, email, locator):
        self.sendKeys(email, locator)

    def enterPassword(self, password, locator):
        self.sendKeys(password, locator)

    def verifyTitle(self, title):
        if title in self.getTitle():
            return True
        return False

    def clearFields(self, locator):
        self.clearElement(locator)
