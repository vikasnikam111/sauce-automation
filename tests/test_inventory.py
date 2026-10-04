
from pages.inventory_page import InventoryPage


def test_add_item_update_cart_count(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    assert inventory_page.get_cart_count() == "1"