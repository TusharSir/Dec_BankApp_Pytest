import time

import pytest

from pageObjects.User_Search_Page import User_Search_Class
from utilities import Excel_utility

@pytest.mark.usefixtures("setup")
class Test_User_Search:
    driver = None
    Excel_File = ".\\TestData\\Test_Data_File.xlsx"
    def test_bankapp_user_search_Excel(self, bankapp_login):

        # again you have to take the methods for login inserted it we have to create one fixture for login at conftest
        us = User_Search_Class(self.driver)
        us.Click_User_management_Link()
        row_count = Excel_utility.Max_Row_Count_Excel(self.Excel_File, "User_Search")
        print(f"Number of row in Excel-->{row_count}")
        testcase_status=[]
        for r in range(2, row_count+1):
            self.username = Excel_utility.Read_Data_From_Excel(self.Excel_File, "User_Search", r, 2)
            self.expected_result = Excel_utility.Read_Data_From_Excel(self.Excel_File, "User_Search", r, 3)
            print(f"User Name --> {self.username}")
            print(f"expected_result --> {self.expected_result}")
            us.Enter_UserName(self.username )
            us.Click_SearchUser_Button()
            time.sleep(1)

            if us.Get_UserName_Search_Result() == "Pass" and self.expected_result == "Pass":
                print("User Search Successful")
                testcase_status.append("Pass")
                Excel_utility.Write_Data_To_Excel(self.Excel_File, "User_Search", r, 4, "Pass")
                Excel_utility.Write_Data_To_Excel(self.Excel_File, "User_Search", r, 5, "Pass")
            elif us.Get_UserName_Search_Result() == "Fail" and self.expected_result == "Fail":
                print("User Search Successful")
                testcase_status.append("Pass")
                Excel_utility.Write_Data_To_Excel(self.Excel_File, "User_Search", r, 4, "Fail")
                Excel_utility.Write_Data_To_Excel(self.Excel_File, "User_Search", r, 5, "Pass")
            else:
                print("User Search Failed")
                testcase_status.append("Fail")
                Excel_utility.Write_Data_To_Excel(self.Excel_File, "User_Search", r, 4, "Fail")
                Excel_utility.Write_Data_To_Excel(self.Excel_File, "User_Search", r, 5, "Fail")

            self.driver.back()



        print(f"testcase_Status-->{testcase_status}")

        if "Fail" not in testcase_status:
            print("All Test Cases Passed")
            assert True
        else:
            print("Test Case Failed")
            assert False

