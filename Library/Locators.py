# Cookie acceptance element
COOKIE_AGREEMENT = "xpath = //div[ @class ='cc-compliance']"

# Jobs by Location locators in footer
LOCATION_HELSINKI = "xpath=//a[@class='about-links' and text()= 'Jobs in Helsinki']"
LOCATION_ESPOO = "xpath=//a[@class='about-links' and text()= 'Jobs in Espoo']"
LOCATION_TAMPERE = "xpath=//a[@class='about-links' and text()= 'Jobs in Tampere']"
LOCATION_VANTAA = "xpath=//a[@class='about-links' and text()= 'Jobs in Vantaa']"
LOCATION_OULU = "xpath=//a[@class='about-links' and text()= 'Jobs in Oulu']"
LOCATION_TURKU = "xpath=//a[@class='about-links' and text()= 'Jobs in Turku']"
LOCATION_LAHTI = "xpath=//a[@class='about-links' and text()= 'Jobs in Lahti']"
LOCATION_KUOPIO = "xpath=//a[@class='about-links' and text()= 'Jobs in Kuopio']"

FOOTER_LOCATIONS_LIST = [LOCATION_HELSINKI, LOCATION_ESPOO, LOCATION_TAMPERE, LOCATION_VANTAA, LOCATION_OULU,
                         LOCATION_TURKU, LOCATION_LAHTI, LOCATION_KUOPIO]


# Jobs by Company locators in footer
COMPANY_NOKIA = "xpath=//a[@class='about-links' and text()= 'Jobs at Nokia']"
COMPANY_OP = "//a[@class='about-links' and text()= 'Jobs at OP']"
COMPANY_NORDEA = "xpath=//a[@class='about-links' and text()= 'Jobs at Nordea']"
COMPANY_VARJO = "//a[@class='about-links' and text()= 'Jobs at Varjo']"
COMPANY_TELIA = "xpath=//a[@class='about-links' and text()= 'Jobs at Telia']"
COMPANY_NORDCLOUD = "//a[@class='about-links' and text()= 'Jobs at Nordcloud']"
COMPANY_SIILI = "xpath=//a[@class='about-links' and text()= 'Jobs at Siili']"
COMPANY_ALL_OUR = "//a[@class='about-links' and text()= 'All our companies']"

FOOTER_COMPANY_LIST = [COMPANY_NOKIA, COMPANY_OP, COMPANY_NORDEA, COMPANY_VARJO, COMPANY_TELIA, COMPANY_NORDCLOUD,
                       COMPANY_SIILI, COMPANY_ALL_OUR]


# Jobs by Keywords locators in footer
PYTHON_JOBS = "xpath=//a[@class='about-links' and text()='Python jobs']"
JAVA_JOBS = "xpath=//a[@class='about-links' and text()='Java jobs']"
C_JOBS = "xpath=//a[@class='about-links' and text()='C jobs']"
JAVASCRIPT_JOBS = "xpath=//a[@class='about-links' and text()='JavaScript jobs']"
IOS_JOBS = "xpath=//a[@class='about-links' and text()='iOS jobs']"
ANDROID_JOBS = "xpath=//a[@class='about-links' and text()='Android jobs']"
SQL_JOBS = "xpath=//a[@class='about-links' and text()='SQL jobs']"
NODE_JOBS = "xpath=//a[@class='about-links' and text()='Node jobs']"

FOOTER_KEYWORDS_LIST = [PYTHON_JOBS, JAVA_JOBS, C_JOBS, JAVASCRIPT_JOBS, IOS_JOBS, ANDROID_JOBS,
                        SQL_JOBS, NODE_JOBS]
