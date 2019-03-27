from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import csv
import xlrd
%matplotlib inline
from selenium import webdriver
import time,re,json, numpy as np
import pandas as pd
from collections import defaultdict,Counter
import matplotlib.pyplot as plt
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


#################################################################################
#  This Cell Drives the browser to the Ralph's website, logs in, and drives     #
#  to the bakery page.                                                          #
#                                                                               #
#################################################################################



driver = webdriver.Chrome('/Users/alexali/Downloads/chromedriver')

AmazonUrl = "https://www.amazon.com/b/ref=s9_acss_bw_cg_BBCT_5d1_w?node=3731911&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-5&pf_rd_r=6HKTJE36CV50BK18JK0W&pf_rd_t=101&pf_rd_p=c378aff1-d60f-4319-af58-5cddf2382367&pf_rd_i=1057792"
driver.get(AmazonUrl)



wait = WebDriverWait(driver, 60)




driver.implicitly_wait(10)



#################################################################################
#  This Cell scrapes product names (breads) and product prices in numerical     #
#  order.                                                                       #
#                                                                               #
#################################################################################


productNameList = ([productName.text for productName in driver.find_elements_by_class_name('s-color-twister-title-link') if productName.text])
priceList = ([price.text for price in driver.find_elements_by_class_name('sx-price') if price.text])
#asinList = ([asin.text for asin in driver.find_elements_by_xpath('//*[@id="result_9"]/div/div[6]/span') if asin.text])
clickNextButton = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="pagnNextLink"]/span[2]')))
clickNextButton.click()

#while('//*[@id="pagnNextString"]'):
x=0
while(x<400):    

    productNameList = productNameList + ([productName.text for productName in driver.find_elements_by_class_name('s-color-twister-title-link') if productName.text])
    priceList = priceList + ([price.text for price in driver.find_elements_by_class_name('sx-price') if price.text])
    #asinList =  asinList + ([asin.text for asin in driver.find_elements_by_xpath('//*[@id="result_9"]/div/div[6]/span') if asin.text])
    


    clickNextButton = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="pagnNextLink"]/span[2]')))
    clickNextButton.click()

    x = x + 1
    print(x)
    

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import csv
%matplotlib inline
from selenium import webdriver
import time,re,json, numpy as np
import pandas as pd
from collections import defaultdict,Counter
import matplotlib.pyplot as plt
import xlrd
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

#################################################################################
#  This Cell put price and product into 2 diff DF's and writes it to excel      #
#################################################################################
priceList = ([s.replace(' ', '') for s in priceList])


pL = pd.DataFrame(priceList)
pNL = pd.DataFrame(productNameList)
#aL = pd.DataFrame(asinList)

writer = pd.ExcelWriter('AmazonBBAPriceProd.xlsx')
writerPrice = pd.ExcelWriter('amazonBBAPrice11417.xlsx')
writerProduct = pd.ExcelWriter('amazonBBAProd11417.xlsx')
#writerAsin = pd.ExcelWriter('amazonBBAAsin.xlsx')



pL.to_excel(writer,'Sheet1')
pNL.to_excel(writer,'Sheet2')
#aL.to_excel(writer,'Sheet3')

pL.to_excel(writerPrice,'Sheet1')
pNL.to_excel(writerProduct,'Sheet1')
#aL.to_excel(writerAsin,'Sheet1')

writer.save()
writerPrice.save()
writerProduct.save()
#writerAsin.save()










