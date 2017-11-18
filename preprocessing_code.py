import json
import pandas as pd

# json 객체 디코딩
json_data = list()

with open('bamboo.json', 'r', encoding='UTF-8') as data_file:
    for line in data_file:
        json_data.append(json.loads(line))


# 대숲 글만 filtering
message_data = list() # 글만 따로 저장하는 리스트
error_occured = list() # 에러가 발생한 인덱스에 있는 객체들 저장하는 리스트

for i in range(len(json_data)):
    try:
        temp_obj = json_data[i]
        message_data.append(temp_obj['message'])
        
    except:   
        error_occured.append(i) #불필요한 정보. 단순 예외처리

# 단어 별로 split하기
word_container = list() 

for text in message_data:
    temp = text.split()[8:]
    word_container.append(temp)

# 이차원 리스트를 일차원 리스트로 변환
word_list = []
for word_lst in word_container:
    for word in word_lst:
        word_list.append(word)

# csv 파일로 변환 및 저장
data = pd.DataFrame({'단어': word_list})
data.to_csv("word_data.csv")
