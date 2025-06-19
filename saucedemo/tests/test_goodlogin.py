from playwright.sync_api import sync_playwright, expect
import pytest
import json
from basepage import BasePage
from conftest import BASE_URL

# Function to load test data
def load_test_data(json_file):
   with open(json_file, 'r') as f:
            return json.load(f)

# Load test data
test_data = load_test_data('../testData/goodlogin.json')


@pytest.mark.parametrize("data", test_data)
def test_page_has_exp_url(page, sel, data):
   sel.doLogin(data['data_username'], data['data_password'])
   sel.button_menu.wait_for()
   expect(page).to_have_url(BASE_URL + "inventory.html")

@pytest.mark.parametrize("data", test_data)
def test_menu_button_visible(sel, data):
      sel.doLogin(data['data_username'], data['data_password'])
      sel.button_menu.wait_for()
      expect(sel.button_menu).to_be_visible()


@pytest.mark.parametrize("data", test_data)
def test_logout_btn_visible(sel, data):
   sel.doLogin(data['data_username'], data['data_password'])
   sel.clickMenu()
   expect(sel.button_logout).to_be_visible()
   

@pytest.mark.parametrize("data", test_data)
def test_logout_btn_not_visible(sel, data):
   sel.doLogin(data['data_username'], data['data_password'])
   print("Testing Logout functionality")
   sel.button_menu.wait_for()
   sel.doLogout()
   expect(sel.button_logout).not_to_be_visible()