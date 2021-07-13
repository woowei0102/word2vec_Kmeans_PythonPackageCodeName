# 透過K-means訓練Word2Vec(訓練Python知名Package中的變數命名)向量之分類模型

## 介紹

之前有透過新聞文章訓練出word2vec+k-means模型，並沒有產出不錯的模型，而這次透過程式中的人為命名，例如:變數、函式等，去作為該訓練集，希望針對各個命名在分類上期望有好的成果。

## gensim套件安裝

~~~python
pip install -U gensim
~~~

## skearn套件相關安裝
~~~python=
pip install numpy
pip install scipy
pip install sklearn
~~~
## 訓練過程

### word2vec 訓練過程
1. 我們已經在`train_data資料夾`中有準備訓練資料，如果要進行更換`train資料夾`裡的檔案便可
2. 整理訓練集
    ~~~
    py .\train_data\ast_data.py
    ~~~

3. 使用`gensim` 的 word2vec 模型進行訓練
    ~~~python
    py train.py
    ~~~

4. 測試訓練出的word2vec模型
    ~~~python
    py word2vec_demo.py
    ~~~

    其中，可透過similarity屬性找到兩個字詞之間的相似度。
    ~~~python
    # 從stack、pop、empty、size作為關鍵字找尋20個相似字詞
    model.most_similar(positive=['stack', 'pop','empty','size'],topn=20)
    ~~~
    ~~~python
    # 能queue作為關鍵字找尋30個相似字詞
    model.most_similar('queue', topn=30)
    ~~~
    ~~~python
    # sortList和temp之間的相似度數值，離1越近越相似
    model.similarity('sortList', 'temp')
    ~~~    
### K-means訓練過程


5. 透過word2vec的關鍵詞去訓練出K-means模型

    ~~~
    py w2v_to_Kmenas.py
    ~~~
    其中，w2v_to_Kmenas程式中有個classCount是需要進行多少分類。
    注意: 請在該檔案夾裡面新增一個`save資料夾`，不然恐會有問題。
6. 測試訓練出的K-means模型
    ~~~
    py kmeans_demo.py
    ~~~
    下方例子是將woman和man判斷是否有同一分類。
    ~~~Python
    Kmeans.predict(test_word) # 預測此單詞為哪一群
    ~~~

## 結論
由於K-means使用方法，無法產出較好的模型，可能要對每一個命名進行Label，並透過其他模型去做訓練，才有可能產出較好的模型。

## 相關文件
### 相關模型
* [透過K-means訓練Word2Vec(訓練英文新聞文章語句)單字向量之分類模型](https://github.com/woowei0102/word2vec_Kmeans_ENarticle)

### word2vec
* [以 gensim 訓練中文詞向量](http://zake7749.github.io/2016/08/28/word2vec-with-gensim/)
* [使用自己的语料训练word2vec模型](https://www.jianshu.com/p/0425bfe619c3)
* [NL2Bash](https://github.com/TellinaTool/nl2bash?fbclid=IwAR2DKk4-qRGEJKUOkcnbK1L8fWeLIKJBTiedyV-aQl7fh7q7OAbCwOKw734)
* [深入淺出Word2Vec原理解析](https://www.jishuwen.com/d/pVET/zh-tw)

### K-means
* [尝试word2vec结合k-means实现关键字聚类](https://www.cnblogs.com/birdmmxx/p/12532751.html)
* [Python-计算word2vec向量的分层聚类并将结果绘制为树状图](https://www.coder.work/article/385557)


