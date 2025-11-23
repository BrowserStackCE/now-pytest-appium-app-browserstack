import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions
import os

@pytest.fixture(scope='function')
def setWebdriver(request):
    remoteURL = "https://hub.browserstack.com/wd/hub"
    bstack_app = os.getenv("BROWSERSTACK_APP")
    print("Using BROWSERSTACK_APP:", bstack_app)
    capabilities = {
        "platformName": "iOS",
        "automationName": "XCUITest",
        "app": "\\" + bstack_app + "\\",
        "bstack:options": {
            "sessionName": request.node.name,
            "buildName": "iOS App Automation",
            "projectName": "Pytest Appium iOS",
        }
    }

    # Convert dict → XCUITestOptions
    options = XCUITestOptions().load_capabilities(capabilities)
    driver = webdriver.Remote(remoteURL, options=options)
    request.instance.driver = driver
    request.node._driver = driver
    yield driver
    driver.quit()
