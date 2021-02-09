import pytest
from base.webdriverfactory import WebDriverFactory
from utilities.teststatus import TestStatus

TestStatus.__test__ = False

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls:
        request.cls.driver = driver

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
