from selenium.webdriver.common import by


class search_Page:
    id_search_textbox = "small-searchterms"
    xpath_search_button = '//*[@class="button-1 search-box-button"]'

    def __init__(self, driver):
        self.driver = driver

    def enter_search_key(self, search_key):
        self.driver.find_element(by.By.ID, self.id_search_textbox).send_keys(search_key)

    def click_search(self):
        self.driver.find_element(by.By.XPATH, self.xpath_search_button).click()
