from selenium.webdriver.common.by import By


class Login_Class:
    text_username_xpath = "//input[@id='username']"
    text_password_xpath = "//input[@id='password']"
    click_login_button_xpath = "//button[@id='loginButton']"
    click_logout_button_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver


    def EnterUserName(self, name):
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys(name)


    def EnterPassword(self, password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)


    def ClickLoginButton(self):
        self.driver.find_element(By.XPATH, self.click_login_button_xpath).click()

    def ClickLogoutButton(self):
        self.driver.find_element(By.XPATH, self.click_logout_button_xpath).click()


    def Verify_LoginButton(self):
        try:
            self.driver.find_element(By.XPATH, self.click_logout_button_xpath)
            return "login_pass"
        except:
            return "login_fail"

