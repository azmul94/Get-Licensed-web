from selenium.webdriver.common.by import By

from Pages.BasePage import Common


class CCTV_Checkout(Common):
    # Locators
    CCTV_HomeButton = By.CSS_SELECTOR, ".btn.btn-lg.btn-danger-dark.text-white.btn-w-lg"
    View_date = By.CSS_SELECTOR, ".btn.btn-success.px-lg-4.px-3.me-lg-4.mb-3"
    Button_Book = By.XPATH, "//div[3]//div[1]//div[2]//div[1]//div[5]//a[1]"
    Select_Package = By.CSS_SELECTOR, ".btn.btn-lg.btn-block.btn-dark.mt-auto.silverPackage"
    Name_ID = By.ID, "floatingFullName"
    Email_ID = By.ID, "floatingEmailAddress"
    Mobile_ID = By.ID, "floatingMobileNumber"
    Next_Button = By.ID, "step1"

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods
    def get_CCTV_homeButton(self):
        return self.do_click(self.CCTV_HomeButton)

    def get_ViewDate(self):
        return self.do_click(self.View_date)

    def get_ButtonBook(self):
        return self.do_click(self.Button_Book)

    def get_select_package(self):
        return self.do_click(self.Select_Package)

    def get_Name(self):
        return self.do_send_keys(self.Name_ID, "Azmul Haq")

    def get_Email(self):
        return self.do_send_keys(self.Email_ID, "azmul@get-licensed.co.uk")

    def get_Mobile(self):
        return self.do_send_keys(self.Mobile_ID, "03343312836")

    def get_Next(self):
        return self.do_click(self.Next_Button)
