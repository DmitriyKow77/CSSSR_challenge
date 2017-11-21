from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from drivers.base_element import BasePage
from drivers.graph_component import GraphComponent

wait_time = 5


class TimeGraphs(BasePage):

    def __init__(self, driver):
        super(TimeGraphs, self).__init__(driver)
        self.driver = driver

    def get_details(self):
        element = self.wait_component_to_load((By.CLASS_NAME, "graphs-details"))
        return GraphComponent(element)

    def get_errors(self):
        element = self.wait_component_to_load((By.CLASS_NAME, "graphs-errors"))
        return GraphComponent(element)

    def get_support(self):
        element = self.wait_component_to_load((By.CLASS_NAME, "graphs-support"))
        return GraphComponent(element)

    def get_files(self):
        element = self.wait_component_to_load((By.CLASS_NAME, "graphs-files"))
        return GraphComponent(element)

