from selenium import webdriver

chrom_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(chrom_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fname")
first_name.send_keys("Shahram")

last_name = driver.find_element_by_name("lname")
last_name.send_keys("Darbandi")

email = driver.find_element_by_name("email")
email.send_keys("shahram.darbandi@yahoo.com")

submit = driver.find_element_by_css_selector("form button")
submit.click()