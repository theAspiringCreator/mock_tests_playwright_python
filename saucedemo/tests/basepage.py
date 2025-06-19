import pytest
from playwright.sync_api import expect


class BasePage:
    def __init__(self, page):
        self.page = page
          
    
    def close(self):
        # Checks for Menu button (to log out) b4 closing:
        try:
            sel.button_menu.wait_for()
            expect(sel.button_menu).to_be_visible()
            sel.doLogout()
        except:
            pass
        finally:
            # Closes the page or browser
            self.page.close()
        