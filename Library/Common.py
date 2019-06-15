from robot.libraries.BuiltIn import BuiltIn
from Library import Locators


class Common:
    HOME_PAGE = "https://www.jobsportal.fi"

    def __init__(self):
        self.builtin_lib = BuiltIn()
        self.selenium_lib = self.builtin_lib.get_library_instance("SeleniumLibrary")

    def accept_cookie(self):
        self.selenium_lib.click_element(Locators.COOKIE_AGREEMENT)
        self.builtin_lib.sleep(1)

    def end_web_test(self):
        self.selenium_lib.close_browser()

    def open_browser_and_load_homepage(self):
        self.selenium_lib.open_browser(url=Common.HOME_PAGE, browser="chrome")
        self.selenium_lib.maximize_browser_window()
        self.selenium_lib.wait_until_page_contains("Contact us")
