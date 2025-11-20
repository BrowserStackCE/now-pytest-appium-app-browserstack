import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="function")
def setWebdriver(request):

    appium_server_url = 'http://localhost:4723/wd/hub'

    capabilities = {
        'platformName': 'Android',
        'appium:deviceName': 'emulator-5554',
        'appium:automationName': 'UiAutomator2',
        'appium:appPackage': 'com.android.settings',
        'appium:appActivity': '.Settings',
        # ... all other capabilities
    }

# 1. Create an Options object
    options = UiAutomator2Options() 

# 2. Load the capabilities into the Options object
    options.load_capabilities(capabilities)

# 3. Pass the Options object to the 'options' argument
    driver = webdriver.Remote(appium_server_url, options)

    yield driver
    driver.quit()
