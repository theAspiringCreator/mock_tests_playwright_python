import pytest

class Selectors:
    def __init__(self, page):
        self.page = page
        self.input_username = page.locator("[data-test='username']")
        self.input_password = page.locator("[data-test='password']")                                    
        self.button_login = page.locator("[data-test='login-button']")
        
        
        self.msg_currentErrorMessage = page.locator("[data-test='error']")
        self.txt_expectedErrorMessage = "Epic sadface: Username and password do not match any user in this service"
        
        self.currentPageHeader = page.locator("#root")
        self.txt_expectedPageHeader="Swag Labs"
        
        self.txt_expectedloginBtnVal ="Login"

        self.button_menu = page.locator(".bm-burger-button")
        self.button_logout = page.get_by_text("Logout")

    def fillUsername(self, data_username):
        self.input_username.wait_for(state='visible')
        self.input_username.clear()
        self.input_username.fill(data_username)
    
    def fillPassword(self, data_password):
        self.input_password.wait_for(state='visible')
        self.input_password.clear()
        self.input_password.fill(data_password)
    
    def clickLoginBtn(self):
        self.button_login.click()

    def doLogin(self, data_username, data_password):
        self.fillUsername(data_username)
        self.fillPassword(data_password)
        self.clickLoginBtn()

    def clickMenu(self):
        self.button_menu.click()
    
    def clickLogoutBtn(self):
        self.button_logout.click()

    def doLogout(self):
        self.clickMenu()
        self.clickLogoutBtn()