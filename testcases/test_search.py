import pytest
from pages.search_page import search_Page
from utilities.customLogger import LogGen


@pytest.mark.usefixtures("setup")
class Test_search:
    logger = LogGen.loggen()

    def test_search(self):
        self.logger.info("-----test_search-----")
        sp = search_Page(self.driver)
        sp.enter_search_key("adidas")
        self.logger.info("-----entered search keyword -----")
        sp.click_search()
        self.logger.info("-----Search submitted -----")
