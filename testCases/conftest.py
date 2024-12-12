import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Login_Page import Login_Class
from utilities.Logger_utility import logger_class
from utilities.additional_utilities import additional_utilities_class
from utilities.readConfig_utility import ReadConfig_class


# step 1
# @pytest.fixture
# def setup():
#     driver = webdriver.Firefox()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", default = "chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_value = request.config.getoption("--browser")
    if browser_value == "chrome":
        print("""launching chrome browser""")
        driver = webdriver.Chrome()
    elif browser_value == "firefox":
        print("""launching firefox browser""")
        driver = webdriver.Firefox()
    elif browser_value == "edge":
        print("""launching edge browser""")
        driver = webdriver.Edge()
    elif browser_value == "headless":
        print("""launching headless browser""")
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    # else:
    #     print("""By default launching chrome browser""")
    #     driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(15)
    # Attaching the driver to class
    request.cls.driver = driver
    yield driver
    driver.quit()

username = ReadConfig_class.username_data()
password = ReadConfig_class.password_data()
base_url = ReadConfig_class.base_url()
login_url = ReadConfig_class.login_url()
sign_up_url = ReadConfig_class.signup_url()
log = logger_class.log_gen_method()
@pytest.fixture
def bankapp_login(setup):
    log.info(f"Opening the Bank Application URL-->{login_url} ")
    # Initialize the test case
    driver.get(login_url)
    # Enter the username and password
    lp = Login_Class(driver)
    log.info("Entering the Username")
    lp.EnterUserName(username)
    log.info("Entering the Password")
    lp.EnterPassword(password)
    log.info("Clicking the Login Button")
    additional_utilities_class.explicit_wait(driver, (By.XPATH, lp.click_login_button_xpath))
    lp.ClickLoginButton()



@pytest.fixture(params=[

    ("Admin", "Pass"),
    ("Tushar", "Pass"),
    ("qwert12", "Fail"),
    ("sheetal", "Pass")

])
def get_data_for_user_search(request):
    return request.param