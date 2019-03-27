from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException 
import csv
%matplotlib inline
from selenium import webdriver
import time,re,json, numpy as np
import pandas as pd
from collections import defaultdict,Counter
import matplotlib.pyplot as plt



#################################################################################
#  This Cell Drives the browser to the Ralph's website, logs in, and drives     #
#  to the bakery page.                                                          #
#                                                                               #
#################################################################################



driver = webdriver.Chrome('/Users/alexali/Downloads/chromedriver')



WalmartUrl = "https://www.walmart.com/c/kp/bluetooth-speakers-with-usb-ports?cat_id=1230415&create_ids=water-speakers%2Cceiling-speaker-mounts%2Cbluetooth-home-theatre-systems%2Cbluetooth-speakers-with-usb-ports%2Cusb-audio-input-products%2Coutdoor-audio-speakers%2Cspeakers-with-optical-input%2Ctop-rated-speakers%2Chome-tower-speakers%2Chome-theater-tower-speakers%2Cmp3-speakers%2C5-1-speakers"
driver.get(WalmartUrl)


wait = WebDriverWait(driver, 60)


csvfile ='WalmartUrls.csv'
dfWalUrls = pd.read_csv(csvfile)




pL = pd.DataFrame(priceList)
pNL = pd.DataFrame(productNameList)


print(pL)
print(pNL)



writer = pd.ExcelWriter('walmartPriceProd110717.xlsx')
writerPrice = pd.ExcelWriter('walmartPrice110717.xlsx')
writerProduct = pd.ExcelWriter('walmartProd110717.xlsx')

pL.to_excel(writer,'Sheet1')
pNL.to_excel(writer,'Sheet2')
pL.to_excel(writerPrice,'Sheet1')
pNL.to_excel(writerProduct,'Sheet1')
writer.save()
writerPrice.save()
writerProduct.save()







