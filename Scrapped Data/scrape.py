import requests,re
import pymysql.cursors
from bs4 import BeautifulSoup
from lxml import html
domain = "https://medlineplus.gov/ency/"
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='disease',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

for char in range(ord('A'),ord('Z')+1):
 r = requests.get('https://medlineplus.gov/ency/encyclopedia_'+str(chr(char))+'.htm')
 content = r.content;
 soup = BeautifulSoup(content,"lxml")
 prog = re.compile('article/.*')
 for link in soup.find_all("a"):
    temp = link.get("href")
    if(prog.match(str(temp))):
         print("Name: "+link.text+"\n\nLink:"+link.get("href"))
         tempr = requests.get(domain + link.get("href"))
         tcontent = tempr.content
         tsoup = BeautifulSoup(tcontent,"lxml")
         print("\n\nSummary:")
         tdefination = tsoup.find("div",{"id":"ency_summary"}) 
         print(tdefination.text)
         section1 = tsoup.find(id="section-1")
         if section1 is not None:
             print("\n\nCause:\n"+str(section1.text))
             treatment = section1.text
         else:
             treatment = ""
         section2 = tsoup.find(id="section-2")
         if section2 is not None:
             print("\n\nSymptoms:\n")
             i = 0
             for listitem in section2.find_all("li"):
                 i = i + 1
                 print (str(i)+":::"+str(listitem.text))
         section3 = tsoup.find(id="section-3")
         if section3 is not None:
             print("\n\nTreatment:\n")
             print(str(section3.text))
             cause = section3.text
         else:
             cause = ""
         print("Inerting in DB")
         with connection.cursor() as cursor:
         		sql = "INSERT INTO main (name,link,discription,cause,treatment) values (%s,%s,%s,%s,%s)"
         		cursor.execute(sql,(str(link.text),str(link.get("href")),str(tdefination.text),str(cause),str(treatment)))
         connection.commit()
         with connection.cursor() as cursor:
         		sql = "select id from main where link = %s"
         		cursor.execute(sql,str(link.get("href")))
         		result = cursor.fetchone()
         		did = result['id']
         if section2 is not None:
         	with connection.cursor() as cursor:
         		sql = "INSERT INTO symptoms (d_id,symptom) values (%s,%s)"
         		for listitem in section2.find_all("li"):
         			cursor.execute(sql,(int(did),str(listitem.text)))
         	connection.commit()
         print("----------------------------------------------")
         
                
         
         
         
