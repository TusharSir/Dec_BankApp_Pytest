from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class additional_utilities_class:

    @staticmethod
    def take_screenshot(driver, testname,status):
        return driver.save_screenshot(f".\\Screenshots\\{testname}_{status}.png")

    @staticmethod
    def explicit_wait(driver, element, timeout=10):
        try:
            WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located(element))
        except:
            pass