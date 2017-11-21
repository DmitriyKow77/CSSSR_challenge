from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from drivers.base_element import BasePage
from drivers.graph_component import GraphComponent
from drivers.info_section import InfoSection

wait_time = 5


class InfoSections(BasePage):

    def __init__(self, driver):
        super(InfoSections, self).__init__(driver)
        self.driver = driver # type: WebDriver

    def get_details(self):
        element = self.driver.find_element_by_class_name("info-details")
        return InfoSection(element)

    def get_errors(self):
        element = self.wait_component_to_load((By.CLASS_NAME, "info-errors"))
        return InfoSection(element)

    def get_support(self):
        element = self.wait_component_to_load((By.CLASS_NAME, "info-support"))
        return InfoSection(element)

    def get_files(self):
        element = self.wait_component_to_load((By.CLASS_NAME, "info-files"))
        return InfoSection(element)

