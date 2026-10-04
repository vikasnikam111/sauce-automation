from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.postal_code = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.confirmation_header = page.locator("[data-test='complete-header']")

    def fill_details(self, first, last, zip_code):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(zip_code)
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()

    def get_confirmation_text(self):
        return self.confirmation_header.text_content()