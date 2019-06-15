from robot.libraries.BuiltIn import BuiltIn
from Library import Locators
from Library.Common import Common


class WebLibrary:

    def __init__(self):
        self.builtin_lib = BuiltIn()
        self.selenium_lib = self.builtin_lib.get_library_instance("SeleniumLibrary")
        self.common = Common()

    def verify_user_can_access_jobs_by_all_locations_in_footer(self):
        for footer_location in Locators.FOOTER_LOCATIONS_LIST:
            self.selenium_lib.click_element(footer_location)

    def verify_user_can_access_jobs_by_all_companies_in_footer(self,):
        for footer_company in Locators.FOOTER_COMPANY_LIST:
            self.selenium_lib.click_element(footer_company)

    def verify_user_can_access_jobs_by_all_keywords_in_footer(self,):
        for footer_keywords in Locators.FOOTER_KEYWORDS_LIST:
            self.selenium_lib.click_element(footer_keywords)
