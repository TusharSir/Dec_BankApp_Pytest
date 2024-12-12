import time

import pytest

from pageObjects.User_Search_Page import User_Search_Class


@pytest.mark.usefixtures("setup")
class Test_User_Search:
    driver = None

    def test_bankapp_user_search_params(self, bankapp_login, get_data_for_user_search):
        username = get_data_for_user_search[0]
        print(f"username--> {username}")
        expected_result = get_data_for_user_search[1]
        print(f"expected result-->{expected_result}")
        # again you have to take the methods for login inserted it we have to create one fixture for login at conftest
        us = User_Search_Class(self.driver)
        us.Click_User_management_Link()
        us.Enter_UserName(username)
        us.Click_SearchUser_Button()
        time.sleep(3)
        print(f"us.Get_UserName_Search_Result()--> {us.Get_UserName_Search_Result()}")
        if us.Get_UserName_Search_Result() == "Pass" and expected_result == "Pass":
            print("User Search Successful")
            assert True
        elif us.Get_UserName_Search_Result() == "Fail" and expected_result == "Fail":
            print("User Search Successful")
            assert True
        else:
            print("User Search Failed")
            assert False
        #assert "No results found" not in us.Get_Search_Result()
