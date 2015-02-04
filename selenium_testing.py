from selenium import webdriver
YOUR_PAGE_URL = 'http://xxxxxx'

# from selenium.webdriver import Firefox
# browser = Firefox()

browser = webdriver.PhantomJS()

browser.get(YOUR_PAGE_URL)
browser.find_element_by_id('{id}').send_keys('sdasdas')
button = browser.find_element_by_id('fSubmit')
button.click()
