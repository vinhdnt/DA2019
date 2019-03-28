from pyvi import ViTokenizer
import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt
#Preprocessing data
stop_word = ['bị', 'bởi', 'cả', 'các', 'cái', 'cần', 'càng', 'chỉ', 'chiếc', 'cho', 'chứ', 'chưa', 'chuyện', 'có', 'có_thể', 'cứ', 'của', 'cùng', 'cũng', 'đã', 'đang', 'đây', 'để', 'đến_nỗi', 'đều', 'điều', 'do', 'đó', 'được', 'dưới', 'gì', 'khi', 'không', 'là', 'lại', 'lên', 'lúc', 'mà', 'mỗi', 'một_cách', 'này', 'nên', 'nếu', 'ngay', 'nhiều', 'như', 'nhưng', 'những', 'nơi', 'nữa', 'phải', 'qua', 'ra', 'rằng', 'rằng', 'rất', 'rất', 'rồi', 'sau', 'sẽ', 'so', 'sự', 'tại', 'theo', 'thì', 'trên', 'trước', 'từ', 'từng', 'và', 'vẫn', 'vào', 'vậy', 'vì', 'việc', 'với', 'vừa', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
data= pd.read_csv("/Users/admin/DA2019/Data/Data_Train.csv",error_bad_lines=False,encoding='utf-8')

comments = []
for text in data['Review'] :
        text_lower = text.lower()
        text_token = ViTokenizer.tokenize(text_lower)
        comments.append(text_token)
sentences = []
for comment in comments:
    sent = []
    for word in comment.split(" ") :
            if (word not in stop_word) :
                if ("_" in word) or (word.isalpha() == True):
                    sent.append(word)
    sentences.append(" ".join(sent))

rates=data["Rate"]

#Get Review length
data0= pd.read_csv("/Users/admin/DA2019/Data/Data_Train.csv",error_bad_lines=False,encoding='utf-8')
scraped_data=pd.DataFrame({'Review':sentences,'Rate':rates,'Device':data0['Device']})
scraped_data['Review_length']=scraped_data['Review'].apply(lambda x:len(x) - x.count(' '))

#Save data have been processed to csv file
scraped_data.to_csv('/Users/admin/DA2019/Data/Data_Processed', encoding='utf-8',index = False)
data= pd.read_csv("/Users/admin/DA2019/Data/Data_Processed",error_bad_lines=False,encoding='utf-8')

#Delete row with rate = 0 and save it again
indexZero=data[data['Rate'] == 0].index
data.drop(indexZero,inplace=True)
data.drop(data[data['Review'] == ''].index,inplace=True)
data.to_csv('/Users/admin/DA2019/Data/Data_Processed', encoding='utf-8')








