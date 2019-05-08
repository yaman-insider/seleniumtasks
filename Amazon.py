from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get('http://www.amazon.com')
driver.maximize_window()
time.sleep(2)

account = driver.find_element_by_id('nav-link-accountList')
account.click()

username = driver.find_element_by_id('ap_email')
username.send_keys('testsystemrules@gmail.com')

password = driver.find_element_by_id('ap_password')
password.send_keys('testtest')
time.sleep(2)
sign = driver.find_element_by_id('signInSubmit')
sign.click()
time.sleep(2)
search = driver.find_element_by_id('twotabsearchtextbox')
search.send_keys('samsung')
search.send_keys(Keys.ENTER)

driver.find_element_by_link_text('2')
time.sleep(2)

product = driver.find_element_by_css_selector('div[data-index="2"] a')

product.click()

time.sleep(3)

addtolist = driver.find_element_by_id('add-to-wishlist-button-submit')

addtolist.click()

time.sleep(2)

closss = driver.find_element_by_class_name('a-icon-close')
closss.click()

time.sleep(2)

listmenu = driver.find_element_by_id('nav-link-accountList')
action = ActionChains(driver)
action.move_to_element(listmenu).perform()

time.sleep(4)
wishl = driver.find_element_by_link_text('Wish List')
wishl.click()

deletep = driver.find_element_by_id('a-autoid-7')
deletep.click()

