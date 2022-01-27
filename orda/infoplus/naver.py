import os
import sys
import urllib.request
import json

import socket
socket.getaddrinfo('localhost', 8080)

client_id = "paBDcU0DZghxI62TMFzl"
client_secret = "S2q1oaZ7kj"

# 이미지 저장 경로
# savePath = "C:/GIT/Orda/orda/infoplus/image/"
savePath = "C:/GIT/Orda/orda/infoplus/image_alpha/"

# 데이터

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
# iter = len(mountainlist)


# for j in range(1,iter):
# for j in range(95):
for j in range(1):
    
    # target = mountainlist[j]
    target = "관모산"
    encText = urllib.parse.quote(target)
    url = "https://openapi.naver.com/v1/search/image?query=" + encText

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()


    if(rescode==200):
        response_body = response.read()
        result = json.loads(response_body)
        img_list = result['items']

        for i, img_list in enumerate(img_list, 1):
            
            # 이미지링크 확인
            print(img_list['link'])

            # 저장 파일명 및 경로
            FileName = os.path.join(savePath, target + str(i) + '.jpg')
            
            # 파일명 출력 
            print('full name : {}'.format(FileName))
            
            # 이미지 다운로드 URL 요청
            urllib.request.urlretrieve(img_list['link'], FileName)

        # 다운로드 완료 시 출력
        print("--------download succeeded--------")

    else:
        print("Error Code:" + rescode)
        print("멈춘 index 값은 " + j + "입니다.")
    

