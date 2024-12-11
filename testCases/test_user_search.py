import pytest

from pageObjects.User_Search_Page import User_Search_Class


@pytest.mark.usefixtures("setup")
class Test_User_Search:
    driver = None

    def test_bankapp_user_search(self, bankapp_login):

        # again you have to take the methods for login inserted it we have to create one fixture for login at conftest
        us = User_Search_Class(self.driver)
        us.Click_User_management_Link()
        us.Enter_UserName("Admin")
        us.Click_SearchUser_Button()
        #assert "No results found" not in us.Get_Search_Result()
