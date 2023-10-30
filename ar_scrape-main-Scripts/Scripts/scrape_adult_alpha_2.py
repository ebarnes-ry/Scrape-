#!/bin/bash
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

path_output = "/home/administrator/adultresearch/output/alpha_items_April_2023.xlsx"

df = pd.DataFrame(columns=['State','name','address','phone','store_front_img','url','Imb_rating','tables_shower','tables_shower_fee','rate_30_minutes','rate_45_minutes','rate_60_minutes','rate_90_minutes','rate_120_minutes','Accep_credit_cards','location_details','Masseuse','List_credit_cards','services','4_Hand_Massage','imb_website','time_hours'])
url2 = "https://adultsearch.com"
req2 = requests.get(url2)
soup2 = BeautifulSoup(req2.content, "html.parser")
mydivs2 = soup2.find_all("div", {"class": "content-col"})
for j in range(0,51):
        mydivs3 = mydivs2[j].find("h5",{"class":"weight-600 p-b-10"})
        state2 = mydivs3.text.strip()
        link2 = mydivs3.find('a').get("href")
        state=state2
#New Section
        url3 = link2+"erotic-massage-parlor"
        req3 = requests.get(url3)
        soup3 = BeautifulSoup(req3.content, "html.parser")
        mydivs3 = soup3.find_all("ul", {"class": "m-b-15 p-0 list-position-inside list-custom-bullet"})
        mydivs4 = mydivs3[0].find_all("a")
        for k in range(len(mydivs4)):
            url4 = mydivs4[k].get("href")
            url5 = "https://adultsearch.com"+url4
            contador = 0
#End New section
            for t in range(5):
                url = url5+"/page/"+str(t)+"?ipp=90"
                req = requests.get(url)
                soup = BeautifulSoup(req.content, "html.parser")
#                mydivs = soup.find_all("div", {"class": "info"})
                mydivs = soup.find_all("div", {"class": "card-wrapper"})
                for i in range(len(mydivs)):
                    x1 = mydivs[i].find('a').get("href")
                    x2 = "https://adultsearch.com/"+x1
                    req5=requests.get(x2)
                    soup5 = BeautifulSoup(req5.content, "html.parser")
                    mydivs6 = soup5.find_all("div",{"class":"escort-popup-body place-details"})

                    name=''
                    extra=''
                    imb_tag=''
                    phone=''
                    address=''
                    imbweburl=''
                    imbrating=''

                    name = mydivs6[0].find('span').text.strip()

                    mydivs7=mydivs6[0].find("div",{"class":"details__card-body"})
                    address = str(mydivs7)
                    address = address.replace('<div class="details__card-body">', '')
                    address = address.replace('</div>','')
                    address = address.replace('<br/>',' ')
                    address = address.replace('\n',' ')
                    address2 = address.strip()
                    address2 = re.sub("[\<\[].*?[\>\]]","",address2)
                    regex = re.compile('details__card-phone')
                    mydivs8=mydivs6[0].find("div",{"class":regex})
                    phone = mydivs8.find("a").text.strip()

                    try:
                        mydivs9 = mydivs6[0].find("div",{"class":"countMedia countMedia-2 row col-12 col-xl-6"})
                        img1=mydivs9.find("a",{"class":"gallery"}).get("href")
                        img2="https:"+img1
                        img2
                    except:
                        img2=''

### NEW SECTION
                    try:
                        regexweb = re.compile("details__card-website")
                        mydivweb=mydivs6[0].find("div",{"class":regexweb})
                        imbweburl = mydivweb.find('a').get("href")
                    except:
                        imbweburl='NA'
                    try:
                        regexrating = re.compile("details__heading")
                        mydivrating = mydivs6[0].find("div",{"class":regexrating})
                        regexreating2 = re.compile("primary-rating")
                        mydivrating2 = mydivrating.find("div",{"class":regexreating2})
                        imbrating = mydivrating2.get("data-rating")
                    except:
                        imbrating = 0

                    value1_1=''
                    value2_2=''
                    value3_3=''
                    value1_1_1=''
                    accepted_cards=0
                    accepted_cards_value=''

                    tableshower=''
                    tableshowerfee=''
                    rate30=''
                    rate60=''
                    rate90=''
                    
                    #New
                    rate45=''
                    rate120=''
                    #####
                    
                    acceptcc=''
                    locationdetail=''
                    Masseuse=''
                    listcc=''
                    imbservices=''
                    hand4massage=''
                    fulltimehours=''
                    try:
                        time_hours = mydivs6[0].find("div",{"class":'hours-open'})
                        time_hours2 = time_hours.find_all("div",{"class":"item"})
                        for time in range(len(time_hours2)):
                            day_w = time_hours2[time].find('h5').text.strip()
                            time_w = time_hours2[time].find('p').text.strip()
                            fulltimehours = fulltimehours + day_w +" "+ time_w + " "
                    except:
                        fulltimehours=''
                    try:
                        facilities = mydivs6[0].find("div",{"class":'details__card-body facilities'})
                        facilities2 = facilities.find_all("p")
                        for items_f in range(len(facilities2)):
                            value1_1 = facilities2[items_f].find('span').text.strip()
                            value2_2 = facilities2[items_f].text.strip()
                            value3_3 = value2_2.replace(value1_1,"").strip()
                            if str(value3_3) == 'Accepted Cards':
                                #print(items_f)
                                value1_1_1 = facilities2[items_f].find_all('img')
                                accepted_cards_value =''
                                for accepted_cards in range(len(value1_1_1)):
                                    value1_1 = value1_1 + str(value1_1_1[accepted_cards].get('alt')) + ", "
                            if str(value3_3) == 'Table Shower':
                                tableshower = value1_1
                            if str(value3_3) == 'Table Shower Fee':
                                tableshowerfee = value1_1
                            if str(value3_3) == 'Rate for 30 minutes':
                                rate30 = value1_1
                            if str(value3_3) == 'Rate for 60 minutes':
                                rate60 = value1_1
                            if str(value3_3) == 'Rate for 90 minutes':
                                rate90 = value1_1
                            
                            #New
                            if str(value3_3) == 'Rate for 45 minutes':
                                rate45 = value1_1
                            if str(value3_3) == 'Rate for 120 minutes':
                                rate120 = value1_1
                            #####
                            
                            if str(value3_3) == 'Accepts Credit Cards':
                                acceptcc = value1_1
                            if str(value3_3) == 'Location Detail':
                                locationdetail = value1_1
                            if str(value3_3) == 'Masseuse':
                                Masseuse = value1_1
                            if str(value3_3) == 'Accepted Cards':
                                listcc = value1_1
                            if str(value3_3) == 'Services':
                                imbservices = value1_1
                            if str(value3_3) == '4 Hand Massage Avaiable':
                                hand4massage = value1_1
                    except:
                        accepted_cards_value=''
                        tableshower=''
                        tableshowerfee=''
                        rate30=''
                        rate60=''
                        rate90=''
                        rate45=''
                        rate120=''
                        acceptcc=''
                        locationdetail=''
                        Masseuse=''
                        listcc=''
                        imbservices=''
                        hand4massage=''

### END SECTION
                        
                    contador = contador + 1
#                    name=mydivs[i].find('h6').text.strip()
#                    extra=mydivs[i].find_all('p')
#                    imb_tag = extra[0].text.strip()
#                    phone = extra[1].text.strip()
#                    address = extra[2].text.strip()
                    df = df.append({'State': state,'name': name, 'address': address2, 'phone': phone , 
                                    'store_front_img' : img2, 'url' : x2 , 'Imb_rating' : imbrating, 'tables_shower' : tableshower,
                                   'tables_shower_fee' : tableshowerfee,'rate_30_minutes' : rate30,'rate_45_minutes' : rate45,'rate_60_minutes' : rate60,
                                   'rate_90_minutes' : rate90,'rate_120_minutes' : rate120, 'Accep_credit_cards' : acceptcc, 'location_details' : locationdetail,
                                   'Masseuse' : Masseuse, 'List_credit_cards' : listcc, 'services' : imbservices, '4_Hand_Massage' : hand4massage,
                                   'imb_website' : imbweburl, 'time_hours' : fulltimehours },ignore_index=True)
            contador = contador/2
            print(state2," ",url5," scrape done //",)
        print("page :",j,"done")
df['unique_code']=df['name'].astype(str) + '_' + df['address'].astype(str) + '_' + df['phone'].astype(str)
df = df.drop_duplicates(subset=['unique_code'])
df.to_excel(path_output = "/home/administrator/adultresearch/output/alpha_items_April_2023.xlsx")
print("+++!!!/// Scrape DONE ////!!!!+++++")

