import pytest
from Tests.Mobile_Tests.Login_with_email import test_login_with_email


@pytest.mark.usefixtures('setWebdriver')
class TestSample:
    test_login_with_email()

    # def test_example(self):
    #     search_element = WebDriverWait(self.driver, 30).until(
    #         EC.element_to_be_clickable(
    #             (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
    #     )
    #
    #     search_element.click()
    #     search_input = WebDriverWait(self.driver, 30).until(
    #         EC.element_to_be_clickable(
    #             (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
    #     )
    #     search_input.send_keys("BrowserStack")
    #     time.sleep(5)
    #     search_results = self.driver.find_elements(
    #         AppiumBy.CLASS_NAME, "android.widget.TextView")
    #
    #     assert len(search_results) > 0
