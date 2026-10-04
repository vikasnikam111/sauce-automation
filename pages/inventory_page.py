from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.cart_badge= page.locator("[data-test='shopping-cart-link']")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")

    def add_item_to_cart(self,data_test_suffix):
        self.page.locator(f"[data-test='add-to-cart-{data_test_suffix}']").click()
    def get_cart_count(self):
        return self.cart_badge.text_content()
        