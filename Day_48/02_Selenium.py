from selenium import webdriver

chrom_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrom_driver_path)
driver.get("https://www.amazon.com")

driver.get("https://www.amazon.com/SUNWILL-Tumbler-Stainless-Insulated-Durable/dp/B07YRRHB32/?_encoding=UTF8&smid=AM0CFX9ROYTX7&pd_rd_w=hpcfg&pf_rd_p=586f3389-8a5a-42ab-aa7a-ae76655b36e6&pf_rd_r=PJ7TA2V7KCDBSWKSFFVB&pd_rd_r=2ceee5a7-4450-4910-8dbf-349d80174c0d&pd_rd_wg=aqpkV&ref_=pd_gw_unk")
price = driver.find_element_by_id("priceblock_dealprice")
print(price.text)