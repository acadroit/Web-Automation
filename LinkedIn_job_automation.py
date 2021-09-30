from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver_path="F:\development\chromedriver.exe"
driver=webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

email=driver.find_element_by_xpath('//*[@id="username"]')
email.send_keys("EMAIL")
time.sleep(2)

password=driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("PASSWORD")
time.sleep(2)

sign_in=driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
sign_in.click()
# time.sleep(3)

driver.maximize_window()

jobs=driver.find_element_by_xpath('//*[@id="ember23"]/span')
jobs.click()


search=driver.find_element_by_xpath('//*[@id="global-nav-typeahead"]/input')
search.send_keys("Python Developer")
search.send_keys(Keys.ENTER)
time.sleep(3)

all_jobs=driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[2]/section/div/nav/div/ul/li[1]/button')
all_jobs.send_keys(Keys.ENTER)
time.sleep(5)

easy_apply_filter=driver.find_element_by_css_selector("#search-reusables__filters-bar > ul > li:nth-child(8) > div")
easy_apply_filter.click()
time.sleep(5)

PHONE=123456789

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)
        
        submit_button = driver.find_element_by_css_selector("footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)

driver.quit()
