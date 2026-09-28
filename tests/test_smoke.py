def test_site_opens(page):
    page.goto("https://www.saucedemo.com/")
    assert page.title() == "Swag Labs"
    