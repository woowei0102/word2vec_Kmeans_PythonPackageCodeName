from gensim.models import word2vec
from gensim import models
from sklearn.cluster import KMeans
import numpy as np
import joblib
import logging

def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model = models.Word2Vec.load('save/word2vec.model')
    # y1 = model.most_similar(positive=['ate', 'speak'], negative=['eat'], topn=5
    # print("y1:", y1)
    #print(len(model.wv.index2word))
    #print('詞表長度：', len(model.wv.vocab))
    ''' word2vec 關鍵字'''
    keys = model.wv.vocab.keys()
    ''' 每個關鍵字的詞向量'''
    wordvector = []
    for key in keys:
        wordvector.append(model[key])
    
    ''' 分類 '''
    classCount = 2 #分類数
    clf = KMeans(n_clusters=classCount)
    s = clf.fit(wordvector)

    ''' 儲存模型 '''
    joblib.dump(s, 'save/kmeans_' + str(classCount)+'.pkl')

    ''' 類別輸出 '''
    labels=clf.labels_
    print('類别：',labels)
    print(type(labels))
   
    arr = [0 for i in range(20)]
    for i in range(len(labels)):
        if labels[i] == 0:
            arr[0] += 1
        elif labels[i] == 1:
            arr[1] += 1
        elif labels[i] == 2:
            arr[2] += 1
        elif labels[i] == 3:
            arr[3] += 1
        elif labels[i] == 4:
            arr[4] += 1
        elif labels[i] == 5:
            arr[5] += 1
        elif labels[i] == 6:
            arr[6] += 1
        elif labels[i] == 7:
            arr[7] += 1
        elif labels[i] == 8:
            arr[8] += 1
        elif labels[i] == 9:
            arr[9] += 1
        elif labels[i] == 10:
            arr[10] += 1
        elif labels[i] == 11:
            arr[11] += 1
        elif labels[i] == 12:
            arr[12] += 1
        elif labels[i] == 13:
            arr[13] += 1
        elif labels[i] == 14:
            arr[14] += 1
        elif labels[i] == 15:
            arr[15] += 1
        elif labels[i] == 16:
            arr[16] += 1
        elif labels[i] == 17:
            arr[17] += 1
        elif labels[i] == 18:
            arr[18] += 1
        elif labels[i] == 19:
            arr[19] += 1   

    for i in range(classCount):
        print(str(i) + '群:', arr[i]) 

if __name__ == "__main__":
    main() 