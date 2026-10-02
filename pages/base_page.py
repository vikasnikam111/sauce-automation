class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self,path=""):
        self.page.goto(f"/{path}")

    def take_screenshot(self, name):
        self.page.screenshot(path=f"screenshots/{name}.png") 