from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "C:/code_development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3548431366&f_AL=true&f_E=1%2C2&f_WT=2&geoId=92000000&keywords=python%20developer%20intern&location=Worldwide&refresh=true')
time.sleep(1)
try:
    login_button = driver.find_element('xpath','/html/body/div[1]/header/nav/div/a[2]')
    login_button.click()
    time.sleep(1)
    user=driver.find_element('xpath','//*[@id="username"]')
    user.send_keys('kashifalikhan093@gmail.com')
    password=driver.find_element('xpath','//*[@id="password"]')
    password.send_keys('Aquatype1')
    login=driver.find_element('xpath','//*[@id="organic-div"]/form/div[3]/button')
    login.click()
    time.sleep(3)
    # job_post=driver.find_element('xpath','//*[@id="ember501"]')
    # job_post.click()
    apply=driver.find_element('xpath','/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/button')
    apply.click()
    time.sleep(2)
    next_button=driver.find_element('xpath','/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button')
    next_button.click()
    for i in range(0,2):
        time.sleep(1)
        #For city--------
        # if i==0:
        #     data_entry=driver.find_element('xpath','//*[@id="single-typeahead-entity-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3568837368-7419546742754252222-city-HOME-CITY"]')
        #     data_entry.send_keys('Kanpur, Uttar Pradesh, India')
        #     temp=driver.find_element('xpath','/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[1]/div/div/div[1]/div/input')
        #     temp.click()
        #     time.sleep(1)
        next_button=driver.find_element('xpath','/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
        next_button.click()
    time.sleep(1)
    review_radio=driver.find_element('xpath','/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div/div/fieldset/div/label')
    review_radio.click()
    review_button=driver.find_element('xpath','/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
    review_button.click()
    time.sleep(1)
    submit=driver.find_element('xpath','/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]')
    submit.click()
    time.sleep(2)
except NoSuchElementException:
        print("No application button, skipped.")
# a_tag_element = driver.find_elements('css',"a.disabled.ember-view.job-card-container__link.job-card-list__title")
# print(a_tag_element)
# for a in a_tag_element:
#     print(a_tag_element.text)
# Find the "class" attribute of the "a" tag element
