import pytest
from selenium import webdriver

from utilities.customLogger import LogGen
from utilities.readProperties import read_Config


@pytest.fixture(scope="class", autouse=True)
def setup(request, browser):
    logger = LogGen.loggen()
    if browser == "chrome":
        driver = webdriver.Chrome()
        logger.info("-----Running on Chrome Browser-----")
        # driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox()
        logger.info("-----Running on Firefox Browser-----")
        # driver = webdriver.Firefox(GeckoDriverManager().install())

    driver.get(read_Config.get_url())
    logger.info("-----Opening web url-----")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    logger.info("-----Closing webdriver-----\n")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")