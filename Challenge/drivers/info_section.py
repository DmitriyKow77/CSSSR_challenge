from selenium.webdriver.remote.webelement import WebElement

wait_time = 5


class InfoSection(WebElement):

    def __init__(self, element):
        super(InfoSection, self).__init__(element.parent, element.id)
        self.element = element  # type: WebElement

    def get_title(self):
        return self.element.find_element_by_tag_name("h1")

    def get_articles(self):
        return self.element.find_elements_by_tag_name("article")
