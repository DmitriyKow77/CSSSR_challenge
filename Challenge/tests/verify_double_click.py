import time
from selenium import webdriver
from selenium.webdriver import ActionChains

chromedriver_path = "../components/chromedriver"
from drivers.info_sections import InfoSections
from drivers.time_graphs import TimeGraphs

driver = webdriver.Chrome(chromedriver_path)
driver.get("http://blog.csssr.ru/qa-engineer/")
driver.implicitly_wait(2)

time_graphs = TimeGraphs(driver)
section_link = time_graphs.get_details().get_link()

info_section = InfoSections(driver).get_details()

# Doubleclick on tab
actionChains = ActionChains(driver)
actionChains.double_click(section_link).perform()
time.sleep(1)  # wait for animation

# Verify section info visible
assert info_section.is_displayed(), "Section not visisble"
assert info_section.get_title().is_displayed(), "Title not visisble"
assert info_section.get_articles()[0].is_displayed(), "Title not visisble"

# Close driver
driver.close()
