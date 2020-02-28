import pytest

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


opts = Options()
opts.headless = True
assert opts.headless  # Operating in headless mode
driver = Firefox(options=opts)
PHRASE = 'real python'
driver.get("http://duckduckgo.com")

search_form = driver.find_element_by_id('search_form_input_homepage')
search_form.send_keys(PHRASE)
search_form.submit()

results = driver.find_elements_by_id('links')
for i in results: 
    print(i.text) 
print("Hello Python world!")
driver.save_screenshot('C:\\Users\\luisraul.ortega\\Downloads\\headless_chrome_test.png')
print(len(results))
link_divs = driver.find_elements_by_css_selector('#links > div')
assert len(link_divs) > 0
  
xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
results = driver.find_elements_by_xpath(xpath)
assert len(results) > 0
  
search_input = driver.find_element_by_id('search_form_input')
assert search_input.get_attribute('value') == PHRASE
driver.close()
quit()