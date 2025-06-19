import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from playwright.sync_api import sync_playwright
from pageObjects.selectors import Selectors
from basepage import BasePage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=['--start-maximized'])
        yield browser      
        browser.close()



@pytest.fixture
def page(browser):
    from basepage import BasePage
    from pageObjects.selectors import Selectors
    context = browser.new_context()
    page = context.new_page()  
    yield page
    context.close()

@pytest.fixture
def base(page):
    from basepage import BasePage
    return BasePage(page)    

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")    

@pytest.fixture
def sel(page, base):
    from pageObjects.selectors import Selectors
    page.goto(BASE_URL)
    return Selectors(page)

