import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('setWebdriver')
class TestSample:

    def test_example(self):
        page_source = self.driver.page_source
        print(f"Page Source Length: {len(page_source)}")
        # Assert that the page source length > 100
        assert len(page_source) > 100, "Page source length is not greater than 100!"
