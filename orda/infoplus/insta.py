import urllib.request 
from urllib import parse 
from urllib.request import urlopen 
from bs4 import BeautifulSoup 
from selenium import webdriver 
import time 
import ssl 
# import subprocess
# from selenium.webdriver.chrome.options import Options

# options = webdriver.ChromeOptions()
# options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")

# mountainlist=['개화산',
# '관악산',
# '구룡산',
# '궁산',
# '대모산',
# '도봉산(자운봉)',
# '망우산',
# '백련산',
# '봉제산',
# '북악산',
# '개좌산',
# '거문산',
# '구덕산',
# '굴암산',
# '금련산',
# '금정산',
# '달음산',
# '대운산',
# '배산',
# '백양산',
# '금계산',
# '금산',
# '능천산',
# '대덕산',
# '두리봉',
# '마천산',
# '무학산',
# '뱀산',
# '비슬산',
# '산성산',
# '가현산',
# '거마산',
# '거머리산',
# '고려산',
# '구봉산',
# '국사봉',
# '금마산',
# '낙가산',
# '마니산',
# '문학산',
# '갈미봉',
# '금당산',
# '깃대봉',
# '마집봉',
# '무등산',
# '바랑산',
# '어등산',
# '갑하산',
# '개머리산',
# '계룡산',
# '계족산',
# '구봉산',
# '금병산',
# '금수봉',
# '도덕봉 (흑룡산)',
# '만인산',
# '보문산',
# '가지산',
# '간월산',
# '고헌산',
# '고헌산',
# '고헌산',
# '국수봉',
# '남암산',
# '능동산',
# '대운산',
# '문수산',
# '가덕산',
# '가리산',
# '가현산',
# '각흘봉',
# '갈기산',
# '감악산',
# '강씨봉',
# '개이빨산',
# '거문봉',
# '검단산',
# '가덕산',
# '가리봉',
# '가리산',
# '가리왕산',
# '가마봉',
# '가칠봉',
# '각흘봉',
# '각희산',
# '간대산',
# '간현봉',
# '가령산',
# '가은산',
# '각호산',
# '갈기산',
# '갈기산',
# '갈모봉',
# '갈미봉',
# '것대산',
# '것대산',
# '계명산',
# '가마봉',
# '가야산',
# '가야산',
# '갑하산',
# '계룡산',
# '관모산',
# '관모산',
# '광덕산',
# '광덕산',
# '국사봉',
# '강천산',
# '견두산',
# '견두산',
# '경각산',
# '경각산',
# '경수산',
# '고덕산',
# '고덕산',
# '고리봉(두리봉)',
# '고봉산',
# '가야산',
# '가야산',
# '가지산',
# '가학산',
# '갈두산',
# '감방산',
# '강천산',
# '개천산',
# '격자봉',
# '견두산',
# '가산',
# '가야산',
# '가지산',
# '각화산',
# '갈모봉',
# '갈미봉',
# '갑장산',
# '갓바위',
# '갓산',
# '건지산',
# '가라산',
# '가래봉',
# '가래봉',
# '가야산',
# '가지산',
# '각산',
# '갈전산',
# '감악산',
# '감암산',
# '감투봉',
# '고근산',
# '고내봉',
# '군산',
# '단산',
# '따라비',
# '사라봉',
# '산방산',
# '성산 일출봉',
# '영천악',
# '원당봉(삼양)']


def imgcollector(whichmountain):
    # subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')
    context = ssl._create_unverified_context() 
    search= whichmountain
    url = "https://www.instagram.com/explore/tags/" 
    newUrl = url+parse.quote_plus(search) 
    # driver = webdriver.Chrome(options=option) #크롬을 이용 
    driver = webdriver.Chrome() #크롬을 이용 
    driver.get(newUrl) 
    time.sleep(3) #여기서 3초를 기다린 다음에 아래꺼를 실행 
    html = driver.page_source #driver의 페이지 소스를 가져와서 html 에 담음 
    soup =BeautifulSoup(html) 

    insta = soup.select('.v1Nh3.kIKUG._bz0w') #이미지 파일이 들어있는 클래스(.으로 구분해준다) 
    n=1 
    for i in insta : 
        print('https://www.instagram.com'+i.a['href']) #누르면 나오는 주소 
        imgUrl = i.select_one('.KL4Bh').img['src'] #이미지가 들어있는 태그의 실질적 img 
        with urlopen(imgUrl) as f: 
            with open(search+str(n)+'.jpg','wb') as h : 
                img = f.read() 
                h.write(img) 
        n += 1 
        print(imgUrl) 

    print() 
    driver.close() 
    time.sleep(1) 
    print("End")
imgcollector('관모산')
# for i in range(len(mountainlist)):
#     imgcollector(mountainlist[i])
