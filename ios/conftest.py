import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions

@pytest.fixture(scope='function')
def setWebdriver(request):
    remoteURL = "https://hub.browserstack.com/wd/hub"
    capabilities = {
        "platformName": "iOS",
        "deviceName": "iPhone 15",
        "platformVersion": "17",
        "automationName": "XCUITest",
        "app": "bs://<app-id-from-browserstack>",
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
