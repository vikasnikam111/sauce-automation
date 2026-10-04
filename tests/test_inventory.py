from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.settings import USERS

def test_add_item_update_cart_count(page):
    login_page = LoginPage(page)
    login_page.open()
    user=USERS["standard"]
    login_page.login(user["username"],user["password"]) 

    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    assert inventory_page.get_cart_count() == "1"