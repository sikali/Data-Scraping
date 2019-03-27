from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import math
import pandas as pd
from time import sleep
from random import randint
from openpyxl import Workbook
import datetime
import requests
from lxml.html import fromstring



CITY = "San_Diego"
STATE = "CA"
#url = 'https://www.yelp.com/search?find_desc=vape%20shop&find_loc=Irvine%2C+CA&ns=1'
MAX_SLEEP = 12000 # in milliseconds

#178.237.208.78

CITYLIST = [ 'San_Luis_Obispo_County', 'San_Mateo_County', 'Santa_Barbara_County', 'Santa_Clara_County', 'Santa_Cruz_County', 'Shasta_County', 'Sierra_County', 'Siskiyou_County', 'Solano_County', 'Sonoma_County', 'Stanislaus_County', 'Sutter_County', 'Tehama_County', 'Trinity_County', 'Tulare_County', 'Tuolumne_County', 'Ventura_County', 'Yolo_County', 'Yuba_County']



'''
create_containers makes a request and parses the page. It takes in a URL as a parameter
from build_yelp_url2 and it returns the container of the page.
The container of the page has Telephone info, Address, and Store Name
'''


def create_containers(url):
    

    #Makes request
    uClient = uReq(url)
    yelp_html = uClient.read()
    uClient.close()


#    FOR ROTATING PROXIES   ##################################################
#
#     proxies = {
#         "http": 'http://159.65.187.217', 
#         "https": 'http://159.65.187.217'
#         }
#     response = requests.get(url,proxies=proxies)
#     print(response)
#     yelp_html = (response.text)
#
##############################################################################


    #html parser
    yelp_soup = soup(yelp_html,"html.parser")

    #Creates and Returns the Container  
                                                   #lemon--div__373c0__1mboc arrange__373c0__UHqhV border-color--default__373c0__2oFDT
    containers = yelp_soup.findAll("div",{"class":"lemon--div__373c0__1mboc largerScrollablePhotos__373c0__3FEIJ arrange__373c0__UHqhV border-color--default__373c0__2oFDT"})
    return containers                             
                  
'''
get_soup makes a request and returns the html of the whole yelp page

I am using this to get the total number of pages as this gets passed
in as a parameter in  get_num_pages
'''
def get_soup(url):
    


    uClient = uReq(url)
    yelp_html = uClient.read()
    uClient.close()






#    FOR ROTATING PROXIES   ##################################################
#
#     proxies = {
#         "http": 'http://159.65.187.217', 
#         "https": 'http://159.65.187.217'
#         }
#     response = requests.get(url,proxies=proxies)
#     print(response)
#     yelp_html = (response.text)
#
##############################################################################





    



    #html parser
    yelp_soup = soup(yelp_html,"html.parser")

    return yelp_soup
'''
get_num_pages takes in yelp_soup as a parameter and this function finds the total
number of pages a specific search result and city has
'''
def get_num_pages(yelp_soup):        
                                                #lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7
    num_pages = yelp_soup.findAll("p",{"class":"lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7"})
    page_len = (len(num_pages))                
    
    if(page_len>0):
        page_amt = num_pages[0]
        page_amt = page_amt.text
        x = (page_amt.find('of'))
        x = x+3
        page_amt = page_amt[x:]
        page_amt = int(page_amt)
        page_amt = math.ceil(page_amt/10)
        print("Page Length is:",page_len)
    else:
        page_amt = 0
        print("Page Amount is:",page_amt)
    return page_amt



'''
page_to_index transforms page number into start index for YelpURL
'''

def page_to_index(page_num):
    ''' Transforms page number into start index to be written in Yelp URL '''
    return (page_num - 1)*10
'''
build_yelp_url builds the url 

'''

def build_yelp_url(page):
    ''' Builds Yelp URL for the given page and cflt to be parsed according to
    config variables '''
    

    url2 = "http://www.yelp.com/search?find_desc=cbd".format(page_to_index(page))
    if CITY:
        url2 += "&find_loc={0}".format(CITY)
    url2 +="%2C%20{0}".format(STATE)
    url2 +="&start={0}".format(page_to_index(page))
    
    print(url2)
    return url2

'''
build_yelp_url2 builds the url with a list of cities as its parameter
'''
def build_yelp_url2(page,cityname):
    ''' Builds Yelp URL for the given page and cflt to be parsed according to
    config variables '''
    

    url2 = "http://www.yelp.com/search?find_desc=cbd".format(page_to_index(page))
    
    
    if CITY:
        url2 += "&find_loc={0}".format(cityname)
        
    url2 +="%2C%20{0}".format(STATE)
    url2 +="&start={0}".format(page_to_index(page))
    
    print(url2)
    return url2

'''
create_file creates the file and returns the filename
You declare the filename in the bottom code
'''

def create_file(name):
    filename = name
    f = open(filename,"w")
    headers = "Shop, Address, Phone Number\n"
    f.write(headers)
    
    return filename

'''
create_dataset iterates through all of the containers given and the saves and appends
shop, address and telephone into a file
'''
def create_dataset(containers,filename):

    f = open(filename,"a")
    
        
    for cont in containers:
    
        shop_container = cont
        shop = shop_container.div.div.div.a.text 
        #print(shop)
        
    
        address_container = cont.findAll("address")
        add_length = (len(address_container))
        if(add_length > 0):
            address = address_container[0]
            address = address.span.text
            #print(address)
        else:
            address = "No Address"
        

                                               #class="lemon--div__373c0__1mboc display--inline-block__373c0__2de_K u-space-b1 border-color--default__373c0__2oFDT"         
        phone_container = cont.findAll("div",{"class":"lemon--div__373c0__1mboc display--inline-block__373c0__2de_K u-space-b1 border-color--default__373c0__2oFDT"})
        phone_length = (len(phone_container))
        print(phone_length)
        if(phone_length > 0):
            phone = phone_container[0]
            phone  = phone.text.strip()
            
        else:
            phone = "No Number"
        
        
        

        
        
        f.write(shop + "," + address + "," + phone + "\n")
    
    f.close()   
    return 0;

'''
mylog Personalized print() tool, used for dummy logging

'''
def mylog(msg):
    ''' Personalized print() tool, used for dummy logging '''
    print("-- " + msg)

'''
r_sleep generates a random sleep between 2.000 and MAX_SLEEP seconds
'''
def r_sleep():
    ''' generates a random sleep between 2.000 and MAX_SLEEP seconds '''

    length = float(randint(2000, MAX_SLEEP)) / 1000
    mylog("Safety Random Sleep has started for {0} sec".format(length))
    sleep(length)
    mylog("Safety Random Sleep is over")   
    



csvname = "CBDCaliforniaList.csv"

filename = create_file(csvname)

num = 1
print(datetime.datetime.now())
for cityName in CITYLIST:
    #  
    x = build_yelp_url2(num,cityName) #Starts at first city then proceeds to hit all the pages
    print("Link: ",x)
    yelp_soup = get_soup(x)
    
    page_num = get_num_pages(yelp_soup)
    print(page_num)
    r_sleep()
    
    
    f = open(filename,"a")
    f.write(" "+ "\n" + "\n")
    f.write(cityName + "\n"+ "\n")
    f.write(" "+ "\n" + "\n")
    f.close()
    
    
    if(page_num > 0):
        
        for i in range(page_num):
            i += 1
            #print(i)
            x = build_yelp_url2(i,cityName)
            containers = create_containers(x)
            create_dataset(containers,filename)
            r_sleep()
    

    num =1
print(datetime.datetime.now())
    

