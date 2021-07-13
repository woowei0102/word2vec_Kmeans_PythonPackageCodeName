from gensim.models import word2vec
from gensim import models
import logging

def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model = models.Word2Vec.load('word2vec.model')
    word1 = 'sortList'
    word2 = 'temp'
    s1 = model.most_similar(positive=['stack', 'pop','empty','size'],topn=20)
    s2 = model.most_similar('queue', topn=30)
    a1 = model.similarity(word1, word2)
    print(a1)
    # for index in word3:
    #     print(index[0],':',index[1])
    # a3 = model.similarity('animal', 'dog')
    #print(word1 + '和' + word2 + '的相似度:' + ' ' + str(a1))
    # print('math和add的相似度:'+ ' ' + str(a2))
    # print('animal和dog的相似度:' + ' ' + str(a3))
    
    #print(model.wv.vocab)

if __name__ == "__main__":
    main() 