from selenium.webdriver.common.by import By


class User_Search_Class:
    click_user_management_xpath = "//a[normalize-space()='User Management']"
    text_username_xpath = "//input[@id='username']"
    click_search_user_button_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def Click_User_management_Link(self):
        self.driver.find_elements(By.XPATH, self.click_user_management_xpath).click()

    def Enter_UserName(self, username):
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys(username)

    def Click_SearchUser_Button(self):
        self.driver.find_element(By.XPATH, self.click_search_user_button_xpath).click()