def test_site_opens(page):
    page.goto("/")
    assert page.title() == "Swag Labs"


