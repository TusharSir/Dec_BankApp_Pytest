import time

from selenium.webdriver.common.by import By


class User_Search_Class:
    click_user_management_xpath = "//a[normalize-space()='User Management']"
    text_username_xpath = "//input[@id='username']"
    click_search_user_button_xpath = "//button[@type='submit']"
    get_searched_username_xpath= "//input[@id='username']"

    def __init__(self, driver):
        self.driver = driver

    def Click_User_management_Link(self):
        self.driver.find_element(By.XPATH, self.click_user_management_xpath).click()

    def Enter_UserName(self, name):
        username= self.driver.find_element(By.XPATH, self.text_username_xpath)
        username.clear()
        username.send_keys(name)

    def Click_SearchUser_Button(self):
        user_button = self.driver.find_element(By.XPATH, self.click_search_user_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", user_button)
        user_button.click()


    def Get_UserName_Search_Result(self):
        title = self.driver.title
        print(title)
        if title == "Edit User":
            username_result = self.driver.find_element(By.XPATH, self.get_searched_username_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();",username_result) # Your task
            time.sleep(1)
            print(f"username_result-->: {username_result.get_attribute('value')}") #print(username_result.get_attribute("value"))
            return "Pass"
        else:
            return "Fail"




        # try:
        #     username_result = self.driver.find_element(By.XPATH, self.get_searched_username_xpath)
        #     #self.driver.execute_script("arguments[0].scrollIntoView();", 54, 132  # Your task
        #     username_result.get_attribute("value")
        #     print(f"username_result: {username_result}")
        #     return username_result
        # except:
        #     print("get_searched_username_xpath is not found")