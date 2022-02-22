import requests
from bs4 import BeautifulSoup
import json
import os
#from Project1.rankapp.models import TestData
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project1.settings')
import pandas as pd
import django
django.setup()
from rankapp.models import Data,jejusi_food,haeundae_food,seomyun_food,gyodong_food,chodangdong_food
from rankapp.models import seoguipo_rest,jejusi_rest,haeundae_rest,seomyun_rest,gyodong_rest,chodangdong_rest
from travelapp.models import *

#이미지 추가방법(맛집/숙소)
f= open('c:/Myexam/chodang_food.html',encoding='utf-8')

html_source=f.read()
f.close()

soup = BeautifulSoup(html_source, 'html.parser')

title_names = soup.select('div h2')
scores = soup.find_all(attrs={'class':'point'})
description = soup.find_all(attrs={'class':'etc'})
img = soup.select('figure > a > div > img')

rest_scores=[] #평점
desc=[] #설명
names=[] #가게이름
imgs=[] #이미지

for title_name in title_names:
        names.append(title_name.get_text())
            
for score in scores:
    rest_scores.append(score.get_text())
    if (score == None):
        rest_scores.append('평점없음')
    
for etc in description:
    desc.append(etc.get_text())
    
for image in img:
    imgs.append(image.get('data-original'))

#if __name__ == '__main__':   
#    for i in range(len(names)):
#        chodang(title=names[i], score=rest_scores[i], addr=desc[i], img=imgs[i]).save()

f= open('c:/Myexam/chodang_rest.html', encoding='utf-8')

html_source=f.read()
f.close()

soup = BeautifulSoup(html_source, 'html.parser')

names = soup.find_all(attrs={'class':'hotel-name'})
#//*[@id="search_results_table"]/div/div/div/div/div[6]/div[5]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/h3/a/div[1]
rates = soup.find_all(attrs={'class':'hotel-rating'})

addrs = soup.find_all(attrs={'class':'hotel-address'})

imgs = soup.find_all(attrs={'class':'hotel-img'})

r_name=[] #가게이름
rest_scores=[] #평점
desc=[] #설명
image=[] #이미지

for title_name in names:
    r_name.append(title_name.get_text())
            
for score in rates:
    rest_scores.append(score.get_text())
    if (score == None):
        rest_scores.append('평점없음')
    
for etc in addrs:
    desc.append(etc.get_text())
    
for img in imgs:
    image.append(img.get('style')[23:len(img)-3]) #이미지 크롤링->".jpg" 의 내용만 넣으면 크롤링 가능

#if __name__ == '__main__':   
#    for i in range(40):
#        chodangrest(title=r_name[i], score=rest_scores[i], addr=desc[i], img=image[i]).save()
'''
f= open('c:/Myexam/haeundae_rest.html', encoding='utf-8')

html_source=f.read()
f.close()

soup = BeautifulSoup(html_source, 'html.parser')

names = soup.find_all(attrs={'class':'hotel-name'})
#//*[@id="search_results_table"]/div/div/div/div/div[6]/div[5]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/h3/a/div[1]
rates = soup.find_all(attrs={'class':'hotel-rating'})

addrs = soup.find_all(attrs={'class':'hotel-address'})

r_name=[] #가게이름
rest_scores=[] #평점
desc=[] #설명

for title_name in names:
    r_name.append(title_name.get_text())
            
for score in rates:
    rest_scores.append(score.get_text())
    if (score == None):
        rest_scores.append('평점없음')
    
for etc in addrs:
    desc.append(etc.get_text())

if __name__ == '__main__':   
    for i in range(30):
        haeundae_rest(title=r_name[i], score=rest_scores[i], addr=desc[i]).save()
        
       
f= open('c:/Myexam/seomun_rest.html',encoding='utf-8')

html_source=f.read()
f.close()

soup = BeautifulSoup(html_source, 'html.parser')

names = soup.find_all(attrs={'class':'hotel-name'})
#//*[@id="search_results_table"]/div/div/div/div/div[6]/div[5]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/h3/a/div[1]
rates = soup.find_all(attrs={'class':'hotel-rating'})

addrs = soup.find_all(attrs={'class':'hotel-address'})

r_name=[] #가게이름
rest_scores=[] #평점
desc=[] #설명

for title_name in names:
    r_name.append(title_name.get_text())
            
for score in rates:
    rest_scores.append(score.get_text())
    if (score == None):
        rest_scores.append('평점없음')
    
for etc in addrs:
    desc.append(etc.get_text())

if __name__ == '__main__':   
    for i in range(30):
        seomyun_rest(title=r_name[i], score=rest_scores[i], addr=desc[i]).save()
        
f= open('c:/Myexam/gyodong_rest.html',encoding='utf-8')

html_source=f.read()
f.close()

soup = BeautifulSoup(html_source, 'html.parser')

names = soup.find_all(attrs={'class':'hotel-name'})
#//*[@id="search_results_table"]/div/div/div/div/div[6]/div[5]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/h3/a/div[1]
rates = soup.find_all(attrs={'class':'hotel-rating'})

addrs = soup.find_all(attrs={'class':'hotel-address'})

r_name=[] #가게이름
rest_scores=[] #평점
desc=[] #설명

for title_name in names:
    r_name.append(title_name.get_text())
            
for score in rates:
    rest_scores.append(score.get_text())
    if (score == None):
        rest_scores.append('평점없음')
    
for etc in addrs:
    desc.append(etc.get_text())

if __name__ == '__main__':   
    for i in range(30):
        gyodong_rest(title=r_name[i], score=rest_scores[i], addr=desc[i]).save()
        
f= open('c:/Myexam/chodang_rest.html',encoding='utf-8')

html_source=f.read()
f.close()

soup = BeautifulSoup(html_source, 'html.parser')

names = soup.find_all(attrs={'class':'hotel-name'})
#//*[@id="search_results_table"]/div/div/div/div/div[6]/div[5]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/h3/a/div[1]
rates = soup.find_all(attrs={'class':'hotel-rating'})

addrs = soup.find_all(attrs={'class':'hotel-address'})

r_name=[] #가게이름
rest_scores=[] #평점
desc=[] #설명

for title_name in names:
    r_name.append(title_name.get_text())
            
for score in rates:
    rest_scores.append(score.get_text())
    if (score == None):
        rest_scores.append('평점없음')
    
for etc in addrs:
    desc.append(etc.get_text())

if __name__ == '__main__':   
    for i in range(30):
        chodangdong_rest(title=r_name[i], score=rest_scores[i], addr=desc[i]).save()

f= open('c:/Myexam/seoquipo_rest.html',encoding='utf-8')

html_source=f.read()
f.close()

soup = BeautifulSoup(html_source, 'html.parser')

names = soup.find_all(attrs={'class':'hotel-name'})
#//*[@id="search_results_table"]/div/div/div/div/div[6]/div[5]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/h3/a/div[1]
rates = soup.find_all(attrs={'class':'hotel-rating'})

addrs = soup.find_all(attrs={'class':'hotel-address'})

r_name=[] #가게이름
rest_scores=[] #평점
desc=[] #설명

for title_name in names:
    r_name.append(title_name.get_text())
            
for score in rates:
    rest_scores.append(score.get_text())
    if (score == None):
        rest_scores.append('평점없음')
    
for etc in addrs:
    desc.append(etc.get_text())

if __name__ == '__main__':   
    for i in range(30):
        seoguipo_rest(title=r_name[i], score=rest_scores[i], addr=desc[i]).save()

f= open('c:/Myexam/jejusi_rest.html',encoding='utf-8')

html_source=f.read()
f.close()

soup = BeautifulSoup(html_source, 'html.parser')

names = soup.find_all(attrs={'class':'hotel-name'})
#//*[@id="search_results_table"]/div/div/div/div/div[6]/div[5]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/h3/a/div[1]
rates = soup.find_all(attrs={'class':'hotel-rating'})

addrs = soup.find_all(attrs={'class':'hotel-address'})

r_name=[] #가게이름
rest_scores=[] #평점
desc=[] #설명

for title_name in names:
    r_name.append(title_name.get_text())
            
for score in rates:
    rest_scores.append(score.get_text())
    if (score == None):
        rest_scores.append('평점없음')
    
for etc in addrs:
    desc.append(etc.get_text())

if __name__ == '__main__':   
    for i in range(30):
        jejusi_rest(title=r_name[i], score=rest_scores[i], addr=desc[i]).save()

#돌려본것
'''
'''
f= open('c:/Myexam/haeundae_food.html',encoding='utf-8')

html_source=f.read()
f.close()

soup = BeautifulSoup(html_source, 'html.parser')

title_names = soup.select('div h2')
scores = soup.find_all(attrs={'class':'point'})
description = soup.find_all(attrs={'class':'etc'})

rest_scores=[] #평점
desc=[] #설명
names=[] #가게이름

for title_name in title_names:
        names.append(title_name.get_text())
            
for score in scores:
    rest_scores.append(score.get_text())
    if (score == None):
        rest_scores.append('평점없음')
    
for etc in description:
    desc.append(etc.get_text())

if __name__ == '__main__':   
    for i in range(len(names)):
        haeundae_food(title=names[i], score=rest_scores[i], addr=desc[i]).save()
        
f= open('c:/Myexam/seomun_food.html',encoding='utf-8')

html_source=f.read()
f.close()

soup = BeautifulSoup(html_source, 'html.parser')

title_names = soup.select('div h2')
scores = soup.find_all(attrs={'class':'point'})
description = soup.find_all(attrs={'class':'etc'})

rest_scores=[] #평점
desc=[] #설명
names=[] #가게이름

for title_name in title_names:
        names.append(title_name.get_text())
            
for score in scores:
    rest_scores.append(score.get_text())
    if (score == None):
        rest_scores.append('평점없음')
    
for etc in description:
    desc.append(etc.get_text())

if __name__ == '__main__':   
    for i in range(len(names)):
        seomyun_food(title=names[i], score=rest_scores[i], addr=desc[i]).save()

f= open('c:/Myexam/gyodong_food.html',encoding='utf-8')

html_source=f.read()
f.close()

soup = BeautifulSoup(html_source, 'html.parser')

title_names = soup.select('div h2')
scores = soup.find_all(attrs={'class':'point'})
description = soup.find_all(attrs={'class':'etc'})

rest_scores=[] #평점
desc=[] #설명
names=[] #가게이름

for title_name in title_names:
        names.append(title_name.get_text())
            
for score in scores:
    rest_scores.append(score.get_text())
    if (score == None):
        rest_scores.append('평점없음')
    
for etc in description:
    desc.append(etc.get_text())

if __name__ == '__main__':   
    for i in range(len(names)):
        gyodong_food(title=names[i], score=rest_scores[i], addr=desc[i]).save()

f= open('c:/Myexam/chodang_food.html',encoding='utf-8')

html_source=f.read()
f.close()

soup = BeautifulSoup(html_source, 'html.parser')

title_names = soup.select('div h2')
scores = soup.find_all(attrs={'class':'point'})
description = soup.find_all(attrs={'class':'etc'})

rest_scores=[] #평점
desc=[] #설명
names=[] #가게이름

for title_name in title_names:
        names.append(title_name.get_text())
            
for score in scores:
    rest_scores.append(score.get_text())
    if (score == None):
        rest_scores.append('평점없음')
    
for etc in description:
    desc.append(etc.get_text())

if __name__ == '__main__':   
    for i in range(len(names)):
        chodangdong_food(title=names[i], score=rest_scores[i], addr=desc[i]).save()

f= open('c:/Myexam/seoquipo_food.html',encoding='utf-8')

html_source=f.read()
f.close()

soup = BeautifulSoup(html_source, 'html.parser')

title_names = soup.select('div h2')
scores = soup.find_all(attrs={'class':'point'})
description = soup.find_all(attrs={'class':'etc'})

rest_scores=[] #평점
desc=[] #설명
names=[] #가게이름

for title_name in title_names:
        names.append(title_name.get_text())
            
for score in scores:
    rest_scores.append(score.get_text())
    if (score == None):
        rest_scores.append('평점없음')
    
for etc in description:
    desc.append(etc.get_text())

if __name__ == '__main__':   
    for i in range(len(names)):
        Data(title=names[i], score=rest_scores[i], addr=desc[i]).save()

f= open('c:/Myexam/jejusi_food.html',encoding='utf-8')

html_source=f.read()
f.close()

soup = BeautifulSoup(html_source, 'html.parser')

title_names = soup.select('div h2')
scores = soup.find_all(attrs={'class':'point'})
description = soup.find_all(attrs={'class':'etc'})

rest_scores=[] #평점
desc=[] #설명
names=[] #가게이름

for title_name in title_names:
        names.append(title_name.get_text())
            
for score in scores:
    rest_scores.append(score.get_text())
    if (score == None):
        rest_scores.append('평점없음')
    
for etc in description:
    desc.append(etc.get_text())

if __name__ == '__main__':   
    for i in range(len(names)):
        jejusi_food(title=names[i], score=rest_scores[i], addr=desc[i]).save()

#데이터 출력 저장 가능함(admin 확인완료)
f= open('c:/Myexam/alexa_list_test.html',encoding='utf-8')

html_source=f.read()
f.close()

soup = BeautifulSoup(html_source, 'html.parser')

rank = soup.select('a')
want_rank6 = rank[12:18]
sites=[]

for site_name in want_rank6:
    sites.append(site_name.get_text())

if __name__=='__main__':
    for i in range(len(sites)):
        Data(title=sites[i]).save()
'''
'''

def food_list():
#셀리니움 장고에서 사용 하는 방법 찾아보기
    req = requests.get('https://www.mangoplate.com/search/서귀포')
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    title_names = soup.select('figure > figcaption > div > a > span')
    scores = soup.select('figure > figcaption > div.info > strong.point.search_point')
    description = soup.select('figure > figcaption > div > p.etc > span') 

    rest_scores=[] #평점
    desc=[] #설명
    names=[] #가게이름
    
    for title_name in title_names:
        names.append(title_name.get_text())
            
    for score in scores:
        rest_scores.append(score.get_text())
    
    for etc in description:
        desc.append(etc.get_text())
    
    f_list = {'이름': names,'평점': rest_scores[0:len(names)],'특징': desc}
    #columns_list = ['이름','평점','특징']
    #food_list = pd.DataFrame(f_list, columns = columns_list)
    food_ls = pd.DataFrame(f_list)
    #return [names, rest_scores, desc]
    
    if __name__=='__main__':
    #data_dict = food_list
    #for n, s, e in data_dict.values():
        #Data(title=f_list('이름'), score=f_list('평점'), addr=f_list('특징')).save()
        for i in range(len(names)):
            Data(title = names[i], score = rest_scores[i], addr = desc[i]).save()
        #Data(, score=rest_scores[0:len(names)], addr=desc).save()
    #Data(title = food_list(names), score = food_list(rest_scores), addr = food_list(desc)).save()

food_list()
'''