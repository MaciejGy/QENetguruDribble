from selenium.webdriver.common.by import By
import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDriver:

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, result_message):
        file_name = result_message + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../screenshots/"
        relative_filename = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_filename)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot was saved to directory: " + destination_file)
        except:
            self.log.error("### Exception occured. Was not able to take screenshot")

    def getTitle(self):
        return self.driver.title

    def getByType(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "plink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.error("Locator type is not supported")
        return False

    def getElement(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            ByType = self.getByType(locator_type)
            element = self.driver.find_element(ByType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and locator type: " + locator_type)
        except:
            self.log.error("Unable to find an element with locator: " + locator +
                           " and locator type: " + locator_type)
        return element

    def elementClick(self, locator, locator_type):
        try:
            element = self.getElement(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locator_type)
        except:
            self.log.error("Cannot click on the element with locator: " + locator +
                           " locatorType: " + locator_type)

    def sendKeys(self, data, locator, locator_type="id"):
        try:
            element = self.getElement(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data to element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.error("Cannot send data to the element with locator: " + locator +
                           " locatorType: " + locator_type)

    def clearElement(self, locator, locator_type="id"):
        try:
            element = self.getElement(locator, locator_type)
            element.clear()
            self.log.info("Element content was cleared")
        except:
            self.log.error("Unable to clear the element")

    def isElementPresent(self, locator, locator_type="id"):
        try:
            element = self.getElement(locator, locator_type)
            if element:
                self.log.info("Element with locator: " + locator +
                              " and locator type: " + locator_type + " is present")
                return True
            return False
        except:
            self.log.error("Element not found")
            return False

    def switchingFrame(self, index):
        self.driver.switch_to.frame(index)
