# This file consists of Test Information like username, password, XPATH etc

# Python Class for Username and Password
class TestData:
    username = "Admin"
    password = "admin123"
    url = "https://opensource-demo.orangehrmlive.com"
    expected_error_message="Invalid credentials"
    expected_submenus=["User Management", "Job", "Organization", "Qualifications",
                             "Nationalities", "Corporate Banking", "Configuration"]
    expected_menus = ["Admin", "PIM", "Leave", "Time", "Recruitment",
                      "My Info", "Performance", "Dashboard", "Directory",
                      "Maintenance", "Buzz"]
# Python Class for Selenium Selectors
class TestSelectors:
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = "//button[@type='submit']"
    error_message='//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]'
    