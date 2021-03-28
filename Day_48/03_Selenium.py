from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrom_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(chrom_driver_path)

driver.get("https://en.wikipedia.org/wiki/main_page")
article_count = driver.find_element_by_css_selector("#articlecount a")
# article_count.click()
all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()
search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)