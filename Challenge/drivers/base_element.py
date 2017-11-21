from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


default_time = 5


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def wait_component_to_load(self, by_locator, wait_time=default_time):
        element = WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(by_locator))
        return element
