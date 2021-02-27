import requests
import pandas as pd 
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
def fno_list():
    df = pd.read_csv("https://www1.nseindia.com/content/fo/fo_mktlots.csv")
    df.to_csv()
    df = df.drop(df.index[3])
    fno_list_data = df.iloc[:, 1].to_list()
    fno_list_data = [x.strip(' ') for x in fno_list_data]
    return fno_list_data
driver = webdriver.Chrome('/Users/premagrawal/Downloads/chromedriver')
driver.maximize_window()
driver.get('https://www.tradingview.com/#signin')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div[2]/div/div/div/div/div/div/div[1]/div[4]/div/span').click()
driver.find_element_by_name("username").send_keys('')
driver.find_element_by_name("password").send_keys('')
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)
driver.find_element_by_link_text('Chart').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/div[2]/div/div/div/div/div[1]/div[2]').click()
time.sleep(1)
#driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/div[1]/div[1]/div[1]/div[1]/div[1]/div/div[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/div[1]/div[1]/div[1]/div[1]/div[1]/div/div[2]/div[1]/span').click()
time.sleep(1)
for symbol in fno_list():
    symbol = symbol.replace('&','_')
    symbol = symbol.replace('-','_')
    symbol = 'NSE:' + str(symbol)
    try :
        driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[2]/div/input').send_keys(symbol)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[2]/div/input').send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/div[1]/div[1]/div[1]/div[1]/div[1]/div/div[2]/span').click()
    except :
        print(symbol)
        pass
time.sleep(5)
driver.quit()