#!/bin/bash
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import math
from datetime import datetime


path_output = "/home/administrator/adultresearch/output/October_15_reviews.xlsx"

df = pd.DataFrame(columns=['State','name','address','phone','store_front_img','url','date_review','review','review_rating'])
lista_urls=[]
lista_restante=[]
url2 = "https://adultsearch.com"
req2 = requests.get(url2)
soup2 = BeautifulSoup(req2.content, "html.parser")
mydivs2 = soup2.find_all("div", {"class": "content-col"})
i=0
j=0
iteration =0
k=0
v=0
for j in range(51):
#for j in range(1):
        contador_ulrs=0
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
            contador_ulrs = contador_ulrs+1
            url4 = mydivs4[k].get("href")
            url5 = "https://adultsearch.com"+url4
            #print("ulr5 - ",url5)
            contador = 0
            lista_urls.append(url5)
            lista_restante.append(url5)
        print(state," ",contador_ulrs," urls scraped")
        
        
for iteration in range(len(lista_urls)):
    vfx = lista_urls[iteration]
    vfx1 = vfx.split("/")
    state = vfx1[4]
    req5_page=requests.get(vfx)
    soup5_page = BeautifulSoup(req5_page.content, "html.parser")
    mydivs6_page = soup5_page.find_all("div",{"class":"primary-pagination"})
    try:
        paginas = mydivs6_page[0].find_all('a',{'class':'item'})
        for v in range(1,len(paginas)):
            if paginas[v].text.strip() == 'pagination-next':
                break
            else:
                totalpaginas= int(paginas[v].text.strip())
    except:
          totalpaginas = 1
    print("total de paginas",totalpaginas)
    for t in range(0,int(totalpaginas)+1):
        url = lista_urls[iteration]+"/page/"+str(t)+"?ipp=90"
        print(url)
        value = str(lista_urls[iteration])
        req = requests.get(url)
        soup = BeautifulSoup(req.content, "html.parser")
    #                mydivs = soup.find_all("div", {"class": "info"})
    #    print(len(mydivs))
        mydivs = soup.find_all("div", {"class": "card-wrapper"})
        for i in range(len(mydivs)):
            x1 = mydivs[i].find('a').get("href")
            if "https://adultsearch.com/" in x1:
                x2 = x1
            else:
                x2 = "https://adultsearch.com"+x1
            print(x1)
            print(x2)
            try:
                print("getting imb")
                req5=requests.get(x2)
                soup5 = BeautifulSoup(req5.content, "html.parser")
                mydivs6 = soup5.find_all("div",{"class":"escort-popup-body place-details"})

                name=''
                extra=''
                imb_tag=''
                phone=''
                address=''
                number_reviews=''

                name = mydivs6[0].find('span').text.strip()
                print(name)
                mydivs7=mydivs6[0].find("div",{"class":"details__card-body"})
                address = str(mydivs7)
                address = address.replace('<div class="details__card-body">', '')
                address = address.replace('</div>','')
                address = address.replace('<br/>',' ')
                address = address.replace('\n',' ')
                address2 = address.strip()

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
                contador = contador + 1
        #                    name=mydivs[i].find('h6').text.strip()
        #                    extra=mydivs[i].find_all('p')
        #                    imb_tag = extra[0].text.strip()
        #                    phone = extra[1].text.strip()
        #                    address = extra[2].text.strip()
                final_review='fail 1'
                date_review=''

                req5_page_review=requests.get(x2)
                soup5_page_review = BeautifulSoup(req5_page_review.content, "html.parser")
                mydivs6_page_review = soup5_page_review.find_all("div",{"class":"escort-popup-body place-details"})
                regex10_page_review = re.compile('primary-pagination')
                try:
                    mydivs10_page_review = mydivs6_page_review[0].find('div',{'class':regex10_page_review})
                    paginas_review = mydivs10_page_review.find_all('a',{'class':'item'})
                    for v_review in range(1,len(paginas_review)):
                        if paginas_review[v_review].text.strip() == 'pagination-next':
                            break
                        else:
                            totalpaginas_review= int(paginas_review[v_review].text.strip())
                except:
                    totalpaginas_review = 1
                print("total de paginas",totalpaginas_review)                      
                for k in range(0,int(totalpaginas_review)+1):
                    x3 = str(x2) + "/page/" + str(k)
                    print(x3)
                    req5=requests.get(x3)
                    soup5 = BeautifulSoup(req5.content, "html.parser")
                    mydivs6 = soup5.find_all("div",{"class":"escort-popup-body place-details"})
                    regex3 = re.compile('details__card-body review')
                    mydivs12 = mydivs6[0].find_all('div',{'class':regex3})
                    #print("do we pass?")
                    regex2 = re.compile('d-flex align-items-start')
                    mydivs11=mydivs6[0].find_all('div',{'class':regex2})
                    #print(mydivs11)
                    if mydivs11 == []:
                        final_review = '*No-reviews*'
                        date_review=''
                        rating_reviews=''
                        df = df.append({'State': state,'name': name, 'address': address2, 'phone': phone , 'store_front_img' : img2, 'url' : x2 ,'date_review': date_review,'review': final_review,'review_rating' : rating_reviews},ignore_index=True)
                    else :
                        for g in range(len(mydivs12)):
                            date_review = mydivs11[g].find('p').text.strip()
                            date_review = str(date_review).replace('Reviewed ',"")
                            date_review = datetime.strptime(date_review, '%m-%d-%Y').date()
                            regex_rating = re.compile('primary-rating')
                            rating_reviews =mydivs11[g].find('div',{'class':regex_rating}).get("data-rating")
                            regex4 = re.compile('content')
                            mydivs13 =mydivs12[g].find('div',{'class':regex4})
                            mydivs14 = mydivs13.find('p').text.strip()
                            review = str(mydivs14)
                            final_review = " ".join(review.split())
                            df = df.append({'State': state,'name': name, 'address': address2, 'phone': phone , 'store_front_img' : img2, 'url' : x2 ,'date_review': date_review,'review': final_review,'review_rating' : rating_reviews},ignore_index=True)
            except:
                print("Error, Jumping Url - ",x2)
    lista_restante.remove(value)
    print("page :",iteration," done of : /", len(lista_urls))
    
df['unique_code']=df['name'].astype(str) + '_' + df['address'].astype(str) + '_' + df['phone'].astype(str)
df['unique_code2']=df['name'].astype(str) + '_' + df['address'].astype(str) + '_' + df['phone'].astype(str) + '_' + df['review']
df = df.drop_duplicates(subset=['unique_code2'])
df = df.drop(columns=['unique_code2'])
df.to_excel(path_output)
print("+++!!!/// Scrape DONE ////!!!!+++++")
