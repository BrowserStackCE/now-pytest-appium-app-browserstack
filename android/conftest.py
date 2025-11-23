import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import os

@pytest.fixture(scope='function')
def setWebdriver(request):
    remoteURL = "https://hub.browserstack.com/wd/hub"
     # Default Android caps (same as NOW Android sample)
     
    bstack_app = os.getenv("BROWSERSTACK_APP")
    print("Using BROWSERSTACK_APP:", bstack_app)
    capabilities = {
        "platformName": "Android",
        "deviceName": "Google Pixel 7",
        "platformVersion": "14.0",
        "automationName": "UiAutomator2",
        "app": bstack_app,
        "bstack:options": {
            "sessionName": request.node.name,
            "buildName": "Pytest App Automate",
            "projectName": "Sample App",
        }
    }

    # Convert to options:
    
    options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote(remoteURL, options=options)
    request.instance.driver = driver
    request.node._driver = driver
    yield driver
    driver.quit()
