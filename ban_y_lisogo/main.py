from typing import Counter
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://www.twitch.tv/'
url_channel = 'https://www.twitch.tv/general_hs_'


driver = webdriver.Chrome(executable_path='/Users/aleksandrtulakov/Documents/ban_y_lisogo/chromedriver/chromedriver')

counter = 0

name = 'silenium_framework'

passo = '14881337322aboba'



try:

    driver.get( url = url ) 
    time.sleep(1)
    
    find_sign_in  = driver.find_element( By.XPATH, '/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button/div/div' )
    find_sign_in.click()
    time.sleep(1)

    # data_input1  = driver.find_element_by_tag_name('input')
    choose1  = driver.find_element( By.XPATH,'/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[1]/div/div[2]/input')
    
    choose1.send_keys( name )
    time.sleep(1)

    choose2  = driver.find_element( By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[2]/div/div[1]/div[2]/div[1]/input' )
    choose2.send_keys( passo )
    time.sleep(1)

    button = driver.find_element( By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/button/div/div' )
    button.click()

    time.sleep(25)

    driver.get( url = url_channel ) 
    time.sleep(1)

    for i in range(5):
        
        time.sleep(5)
        if counter == 0:

            data_input1 = driver.find_element_by_tag_name('textarea')
            # choose  = driver.find_element( By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div/section/div/div[5]/div[2]/div[1]/div[2]/div/div/div[1]/div/textarea' )
            data_input1.send_keys( 'Гена что за дичь где лига PoroSad Гена что за дичь где лига PoroSad Гена что за дичь где лига PoroSad Гена что за дичь где лига PoroSad Гена что за дичь где лига PoroSad' + Keys.ENTER )
            time.sleep(7)
            counter += 1

        else:
            data_input0  = driver.find_element_by_tag_name('input')
            data_input0.click()
            
            data_input1 = driver.find_element_by_tag_name('textarea')
            data_input1.send_keys( 'Basedge' + Keys.ENTER )
            time.sleep(7)

except Exception as Ex:
    print(Ex)



