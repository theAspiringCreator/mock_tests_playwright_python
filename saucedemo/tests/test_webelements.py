import pytest
import json
from basepage import BasePage
from playwright.sync_api import expect

def test_header(sel):
    sel.currentPageHeader.wait_for()
    expect(sel.currentPageHeader).to_contain_text(sel.txt_expectedPageHeader)


def test_username_input_visible(sel):
    selectors = [sel.input_username, sel.input_password, sel.button_login]

    for selector in selectors:
        selector.wait_for()
        expect(selector).to_be_visible()
        expect(selector).to_be_enabled()

def test_login_button_value(sel):
    expect(sel.button_login).to_have_value(sel.txt_expectedloginBtnVal)
    