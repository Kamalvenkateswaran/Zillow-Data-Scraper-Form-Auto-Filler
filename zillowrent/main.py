import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

target="https://appbrewery.github.io/Zillow-Clone/"


response=requests.get(url=target)
response=response.text


soup=BeautifulSoup(response,'html.parser')

Link=[]
for link in soup.find_all('a',class_='property-card-link'):
    Link.append(link.get('href'))

#print(Link)

Price=[]
for price in soup.find_all('span',class_='PropertyCardWrapper__StyledPriceLine'):
    Price.append(price.text)

#print(Price)


def is_valid_address(text):
    return text and any(char.isdigit() for char in text) and "," in text

Address= [img.get('alt', '') for img in soup.find_all('img') if is_valid_address(img.get('alt', ''))]

# Print the filtered alt attributes



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)



R=len(Address)
n=0
for _ in range(R):

    time.sleep(2)
    sheet=driver = webdriver.Chrome(options=chrome_options)
    sheet=driver.get('https://docs.google.com/forms/d/e/1FAIpQLSc8RziC_a9VqUDENAeT67pWte6bfhF3p8Kbi44sO_xg5EiRTw/viewform?usp=header')
    time.sleep(5)
    Add=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Add.send_keys(Address[n])

    time.sleep(2)
    Pr=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Pr.send_keys(Price[n])

    time.sleep(2)
    Li=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Li.send_keys(Link[n])

    time.sleep(2)
    submit=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    n+=1
    time.sleep(2)
    driver.quit()



