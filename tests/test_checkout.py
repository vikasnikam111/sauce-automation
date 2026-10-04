
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import expect



def test_complete_purchase(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()

    cart_page = CartPage(logged_in_page)
    expect(cart_page.get_cart_items()).to_have_count(1)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.fill_details("Test", "User", "12345")
    checkout_page.finish_order()
    expect(checkout_page.get_confirmation_header()).to_contain_text("Thank you")