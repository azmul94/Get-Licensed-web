import time

from TestData.Data import Testdata
from Pages.DsCheckOut import DS_CheckOut
from Utilities.BaseClass import BaseClass


class Test_one(BaseClass):

    def test_dsCheckOut(self):
        log = self.getlogger()  # For log file
        Checkout = DS_CheckOut(self.driver)  # Call the page class
        log.info("Click  DS menu button")
        Checkout.get_DS()
        title = Checkout.get_title(Testdata.DSPageTitle)
        assert title == Testdata.DSPageTitle
        self.driver.refresh()
        Checkout.get_scroll()
        time.sleep(3)
        Checkout.get_book()
        course_title = Checkout.get_title(Testdata.DScoursefinder)
        assert course_title == Testdata.DScoursefinder
        self.driver.refresh()
        Checkout.get_scroll()
        time.sleep(5)
        Checkout.get_button_book()
        time.sleep(5)
        Checkout.get_scroll()
        time.sleep(4)
        Checkout.get_select_package()
        time.sleep(4)
        Checkout.get_modal()
        Checkout.get_select_radio()
