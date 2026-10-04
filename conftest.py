import os
import pytest
from pages.login_page import LoginPage
from config.settings import USERS




@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):
    yield
    rep = getattr(request.node, "rep_call", None)
    if rep and rep.failed:
        os.makedirs("screenshots", exist_ok=True)
        page.screenshot(path=f"screenshots/{request.node.name}.png")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)

@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.open()
    user = USERS["standard"]
    login_page.login(user["username"], user["password"])
    return page