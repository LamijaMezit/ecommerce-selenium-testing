from asyncio import wait
import random
from ssl import Options
from requests import options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains




def test_correct_page():
 
 option = webdriver.ChromeOptions()
 driver = webdriver.Chrome(options = option)
 wait = WebDriverWait(driver, timeout=10)

 driver.get("https://tutorialsninja.com/demo/")
 driver.maximize_window()
 time.sleep(5)

 title_page= driver.title
 assert title_page == "Your Store"

#cameras_link
 cameras_locator=(By.XPATH, '//a[text()="Cameras"]')
 wait_cameras= wait.until(EC.presence_of_element_located(cameras_locator))

 wait_cameras.click()

 time.sleep(5)
    
#cameras_click
 camera = (By.XPATH, '//a[text()="Nikon D300"]')
 wait_camera= wait.until(EC.element_to_be_clickable(camera))
 wait_camera.click()
 time.sleep(2)

#first picture
 first_pic= driver.find_element(By.XPATH, '//a[@class="thumbnail"]')
 first_pic.click()
 time.sleep(2)

#next_picture
 next_picture=driver.find_element(By.XPATH,'//button[@title="Next (Right arrow key)"]')
 for i in range(0,5):
        next_picture.click()
 time.sleep(2)


#screenshot
#driver.save_screenshot('screenshot_pic' + str(random.randint(0,101)) + '.png')


#close_button

 c_button=driver.find_element(By.XPATH,'//button[@title="Close (Esc)"]')
 c_button.click()
 time.sleep(1)


#quantity
 quantity=driver.find_element(By.ID,'input-quantity')
 quantity.click()
 time.sleep(1)
 

 quantity.clear()
 time.sleep(1)
 quantity.send_keys('3')
 time.sleep(1)

#add to cart button
 add_button=driver.find_element(By.ID,'button-cart')
 add_button.click()
 time.sleep(2)

#move to Desktops


 desktops = driver.find_element(By.XPATH, '//a[text()="Desktops"]')
 action = ActionChains(driver)
 action.move_to_element(desktops).perform()

 time.sleep(2)

 desktop = driver.find_element(By.XPATH, "//a[@class='see-all']")
 desktop.click()

 time.sleep(1)


#click on the Apple Cinema

 AC= driver.find_element(By.XPATH, "//a[contains(@href, 'product_id=42')]")
 AC.click()

 time.sleep(2)


#scroll
 add_button_2=driver.find_element(By.XPATH, '//button[@id="button-cart"]')
 add_button_2.location_once_scrolled_into_view
 time.sleep(1)


#calendar
 calendar=driver.find_element(By.XPATH, '//i[@class="fa fa-calendar"]')
 calendar.click()
 time.sleep(1)

 next_click=driver.find_element(By.XPATH, '//th[@class="next"]')
 month_year=driver.find_element(By.XPATH, '//th[@class="picker-switch"]')


#year:2022 month:december
 while month_year.text != 'June 2011':
  next_click.click()
  time.sleep(2)

#day 31
 calendar_date = driver.find_element(By.XPATH, '//td[text()="31"]')
 calendar_date.click()
 time.sleep(2)

#add to button
 add_button_2.click()
 time.sleep(1)

 driver.quit()

 #checkout process
 cart = driver.find_element(By.ID, 'cart-total')

 cart.click()
 driver.quit() 



 