from playwright.sync_api import sync_playwright, expect
import pytest
import json
from basepage import BasePage


# Function to load test data
def load_test_data(json_file):
   with open(json_file, 'r') as f:
      return json.load(f)

# Load test data
test_data = load_test_data('../testData/badlogins.json')

@pytest.mark.parametrize("data", test_data)
def test_badlogins(sel, data):   
    print(f"Testing {data['description']}")
    sel.fillUsername(data['data_username'])
    sel.fillPassword(data['data_password'])
    sel.clickLoginBtn()
    expect(sel.msg_currentErrorMessage).to_be_visible()
    expect(sel.msg_currentErrorMessage).to_contain_text(sel.txt_expectedErrorMessage)