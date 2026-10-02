from pages.login_page import LoginPage
from config.settings import USERS
from playwright.sync_api import expect

def test_standard_user_can_login(page):
    login_page=LoginPage(page)
    login_page.open()
    user = USERS["standard"]
    login_page.login(user["username"], user["password"])
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_wrong_password_shows_error(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "wrong_password")
    assert "Epic sadface: Username and password do not match any user in this service" in login_page.get_error_text()