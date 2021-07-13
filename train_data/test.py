import os
import re
import ast

yourPath = os.path.dirname(__file__) + '\\train\\'


def read_py(dir):
    allFileList = os.listdir(dir)
    for file in allFileList:
        if os.path.isdir(os.path.join(dir,file)):
            read_py(dir + file +'\\')
        elif os.path.isfile(dir+file):   
            if os.path.splitext(dir+file)[1][1:].lower() == 'py':
                print("py檔案: " + dir + file)
            else:
                #print("其他檔案: " + dir + file)
                pass





if __name__ == '__main__':
    read_py(yourPath)