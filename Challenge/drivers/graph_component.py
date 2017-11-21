from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from drivers.base_element import BasePage

wait_time = 5


class GraphComponent(WebElement):

    def __init__(self, element):
        super(GraphComponent, self).__init__(element.parent, element.id)
        self.element = element  # type: WebElement

    def get_link(self):
        return self.element.find_element_by_tag_name("a")



