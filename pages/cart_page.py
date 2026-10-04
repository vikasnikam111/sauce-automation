from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.check_out_button = page.locator("[data-test='checkout']")
        self.cart_items = page.locator("[data-test='cart-item']")

    def get_item_count(self):
        return self.cart_items.count()  
    def proceed_to_checkout(self):
        self.check_out_button.click()