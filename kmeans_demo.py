from gensim.models import word2vec
from gensim import models
from sklearn.cluster import KMeans
import numpy as np
import joblib
import logging
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


def main():
  #  logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # 讀取Model
    classCount = 2 #分類数
    Kmeans = joblib.load('save/kmeans_'+ str(classCount) +'.pkl')
    w2v = models.Word2Vec.load('./save/word2vec.model')
    # print(Kmeans.predict(w2v['win']))

   # labels=Kmeans.labels_

    print(w2v)
    word = ['balance', 'name', 'format', 'show']
    arr = [0 for i in range(20)]
    for i in range(len(word)):
      print(word[i] + ':' + str(Kmeans.predict([w2v[word[i]]])))
      arr[int(Kmeans.predict([w2v[word[i]]]))] +=1

    for i in range(classCount):
          print(str(i) + '群:',arr[i])                                                                                                                       

if __name__ == "__main__":
    main() 