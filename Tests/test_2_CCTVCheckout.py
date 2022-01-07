import time

from Pages.CCTVCheckout import CCTV_Checkout
from TestData.Data import Testdata
from Utilities.BaseClass import BaseClass


class Test_two(BaseClass):

    def test_CCTVCheckOut(self):
        log = self.getlogger()  # For log file
        CCTV = CCTV_Checkout(self.driver)  # Call the page class
        log.info("Click  CCTV menu button")
        CCTV.get_CCTV_homeButton()
        # CCTV.get_scroll()
        log.info("Click  CCTV View dates")
        CCTV.get_ViewDate()
        time.sleep(5)
        CCTV.get_scroll()
        time.sleep(5)
        log.info("Click  ON CCTV Book Button")
        CCTV.get_ButtonBook()
        time.sleep(9)
        CCTV.get_scroll()
        time.sleep(9)
        log.info("Click on CCTV Package")
        CCTV.get_select_package()
        CCTV.get_Name()
        CCTV.get_Email()
        CCTV.get_Mobile()
        log.info("Click on Next button for address")
        time.sleep(5)
        CCTV.get_Next()
        # CCTV.get_postcode()
        # CCTV.get_address()
        CCTV.get_city()
        time.sleep(3)
        CCTV.get_AutoList()
        time.sleep(5)
        CCTV.get_Next2()
        CCTV.get_stripe()
