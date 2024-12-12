import random
import string
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Login_Page import Login_Class
from pageObjects.SignUp_Page import SignUp_Class
from utilities.Logger_utility import logger_class
from utilities.additional_utilities import additional_utilities_class
from utilities.readConfig_utility import ReadConfig_class


@pytest.mark.usefixtures("setup")
class Test_Login01:
    username = ReadConfig_class.username_data()
    password = ReadConfig_class.password_data()
    base_url = ReadConfig_class.base_url()
    login_url = ReadConfig_class.login_url()
    sign_up_url = ReadConfig_class.signup_url()
    log = logger_class.log_gen_method()



    driver = None

    @pytest.mark.sanity
    @pytest.mark.userprofile
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    @pytest.mark.depedency(name="test_bankapp_url_001")
    def test_bankapp_url_001(self):
        self.log.info("Testcase test_bankapp_url_001 is started")
        self.log.info(f"Opening the Bank Application URL-->{self.base_url} ")
        self.driver.get(self.base_url)
        # Initialize the test case
        self.log.info(f"Checking the Bank Application Title-->{self.driver.title}")
        if self.driver.title== "Bank Application":
            print("Test Case Passed: Bank Application URL Opened")
            self.log.info("Taking screenshot")
           # self.driver.save_screenshot(".\\Screenshots\\test_bankapp_url_001_pass.png")
            additional_utilities_class.take_screenshot(self.driver, "test_bankapp_url_001", "Pass")
            time.sleep(3)
            allure.attach.file(".\\Screnshots\\test_bankapp_url_001_pass.png", attachment_type=allure.attachment_type.PNG)

            self.log.info("Testcase test_bankapp_url_001 is passed\n")
            assert True
        else:
            self.log.info("Taking screenshot")
            additional_utilities_class.take_screenshot(self.driver, "test_bankapp_url_001", "Pass")
            #self.driver.save_screenshot(".\\Screenshots\\test_bankapp_url_001_fail.png")
            print("Test Case Failed: Bank Application URL Not Opened")
            self.log.info("Testcase test_bankapp_url_001 is failed\n")
            assert False

    @pytest.mark.sanity
    @pytest.mark.userprofile
    #@pytest.mark.xfail
    @pytest.mark.depedency(depends=["test_bankapp_url_001"])
    def test_bankapp_login_002(self):
        self.log.info("Testcase test_bankapp_login_002 is started")
        self.log.info(f"Opening the Bank Application URL-->{self.login_url} ")
        # Initialize the test case
        self.driver.get(self.login_url)
        # Enter the username and password
        lp = Login_Class(self.driver)
        self.log.info("Entering the Username")
        lp.EnterUserName(self.username)
        self.log.info("Entering the Password")
        lp.EnterPassword(self.password)
        self.log.info("Clicking the Login Button")
        additional_utilities_class.explicit_wait(self.driver, (By.XPATH, lp.click_login_button_xpath))
        lp.ClickLoginButton()
        time.sleep(3)
        self.log.info("Verify Page Title")
        if self.driver.title== "Dashboard":
            self.log.info("Testcase test_bankapp_login_002 is Pass")
            print("Test Case Passed: Login Successful")
            self.log.info("Taking the screenshot")
            #self.driver.save_screenshot(".\\Screenshots\\test_bankapp_login_002_pass.png")
            additional_utilities_class.take_screenshot(self.driver, "test_bankapp_login_002", "Pass")
            self.log.info("Testcase test_bankapp_login_002 is Passed")
            assert True
        else:
            self.log.info("Taking the screenshot")
            #self.driver.save_screenshot(".\\Screenshots\\test_bankapp_login_002_fail.png")
            additional_utilities_class.take_screenshot(self.driver, "test_bankapp_login_002", "Fail")
            print("Test Case Failed: Login Failed")
            self.log.info("Testcase test_bankapp_login_002 is Failed")
            assert False

    @pytest.mark.group1
    @pytest.mark.userprofile
    @pytest.mark.skip
    @pytest.mark.flaky(reruns= 2,reruns_delay =1)
    @pytest.mark.depedency(depends=["test_bankapp_url_001"])
    def test_bankapp_signup_003(self, faker):
        self.driver.get(self.sign_up_url)
        sp = SignUp_Class(self.driver)
        username = faker.name()
        print(f"Username: {username}")
        sp.EnterUserName(username)
        sp.EnterPassword("Admin@123")
        phone_number = faker.phone_number()
        print(f"phone_number: {faker.phone_number()}")
        print(f"Number generated by function {generate_random_phone_number()}")
        sp.EnterPhone(phone_number)
        email = faker.email()
        print(f"email: {email}")
        sp.EnterEmail(email)
         # scroll into view
        sp.ClickCreateUserButton()
        additional_utilities_class.explicit_wait(driver=self.driver,element= (By.XPATH, sp.success_message_xpath), timeout=7)
        if sp.Verify_SuccessMessage() == "signup_pass":
            print("Test Case Passed: User Created Successfully")
            #self.driver.save_screenshot(".\\Screenshots\\test_bankapp_signup_003_pass.png")
            additional_utilities_class.take_screenshot(self.driver, "test_bankapp_signup_003", "Pass")
            assert True
        else:
            #self.driver.save_screenshot(".\\Screenshots\\test_bankapp_signup_003_fail.png")
            additional_utilities_class.take_screenshot(self.driver, "test_bankapp_signup_003", "Fail")
            print("Test Case Failed: User Not Created Successfully")
            assert False


def generate_random_phone_number():
    return ''.join(random.choices(string.digits, k= 10))




"pytest -v -s --html=Report/my_report.html -n auto --browser chrome --reruns= 2"


