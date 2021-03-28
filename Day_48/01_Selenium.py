from selenium import webdriver

chrom_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrom_driver_path)
driver.get("https://www.amazon.com")


# driver.quit()
# driver.close()