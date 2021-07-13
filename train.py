import logging

from gensim.models import word2vec

def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.LineSentence("./train_data/data.txt")
    model = word2vec.Word2Vec(sentences, size=100, window=10, min_count=1, sg=1, negative=10)

    #保存模型，供日後使用
    model.save("./save/word2vec.model")

    #模型讀取方式
    # model = word2vec.Word2Vec.load("your_model_name")

if __name__ == "__main__":
    main()