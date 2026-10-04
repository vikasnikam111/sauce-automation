from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.settings import USERS


def test_complete_purchase(page):
    login_page = LoginPage(page)
    login_page.open()
    user = USERS["standard"]
    login_page.login(user["username"], user["password"])

    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()

    cart_page = CartPage(page)
    print(page.locator("#cart_contents_container").inner_html())
    assert cart_page.get_item_count() == 1
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.fill_details("Test", "User", "12345")
    checkout_page.finish_order()
    assert "Thank you" in checkout_page.get_confirmation_text()