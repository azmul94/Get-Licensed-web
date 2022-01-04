from selenium.webdriver.common.by import By
from Pages.BasePage import Common


class DS_CheckOut(Common):
    # by Locators
    DS = By.CSS_SELECTOR, ".btn.btn-lg.btn-warning.text-white.btn-w-lg"
    Book_now = By.XPATH, "//a[normalize-space()='View Dates & Prices']"
    Button_Book = By.CSS_SELECTOR, "div:nth-child(3) div:nth-child(1) div:nth-child(2) div:nth-child(1)"\
                                   " div:nth-child(5) a:nth-child(1)"
    Select_Package = By.CSS_SELECTOR, ".btn.btn-lg.btn-block.btn-dark.mt-auto.goldPackage"
    modal = By.CSS_SELECTOR, ".selectEfaw.d-md-flex"
    Select_radio = By.CSS_SELECTOR, "input.addRemoveEFAW#haveEfaw"

    # Constructor of the class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods
    def get_DS(self):
        return self.do_click(self.DS)

    def get_book(self):
        return self.do_click(self.Book_now)

    def get_button_book(self):
        return self.do_click(self.Button_Book)

    def get_select_package(self):
        return self.do_click(self.Select_Package)

    def get_modal(self):
        return self.do_click(self.modal)

    def get_select_radio(self):
        self.get_element_clickable(self.Select_radio)
