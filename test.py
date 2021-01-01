from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

choice = input('Choose gender: (Type "M" for Male, and "F" for Female): ')
driver = webdriver.Chrome('chromedriver.exe')

if choice=='F':
    driver.get('https://generated.photos/faces/white-race/female')
elif choice=='M':
    driver.get('https://generated.photos/faces/white-race/male')
else:
    driver.get('https://generated.photos/faces/white-race/female')

sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/a[1]').click()
driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div/main/div[2]/div/button/span').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div/main/div[2]/div/button/span').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div/main/div[2]/div/button/span').click()
grid = [driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div/main/div[1]/div['+str(x)+']/a/img') for x in range(1, 101)]

for iter, x in enumerate(grid):
    with open('pict/pict'+str(iter)+'.png', 'wb') as f:
        f.write(x.screenshot_as_png)
        # sleep(2)

# for iter, x in enumerate(grid):
#     print(iter, '\t', type(x))