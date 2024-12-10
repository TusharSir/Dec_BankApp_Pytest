import pytest
from selenium import webdriver

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