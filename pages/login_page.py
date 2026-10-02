from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.locator("[data-test='login-button']")
        self.errormessage_input = page.get_by_role("alert")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_text(self):
        return self.errormessage_input.text_content()