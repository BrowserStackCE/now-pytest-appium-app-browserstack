import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('setWebdriver')
class TestSample:

    def test_example(setWebdriver):
        driver = setWebdriver
        # Example: open app or check activity
        print(driver.session_id)
        page_source = driver.page_source
        print(f"Page Source Length: {len(page_source)}")
        # Assert that the page source length > 100
        assert len(page_source) > 100, "Page source length is not greater than 100!"
        
