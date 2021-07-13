import os
import re
import ast
import logging

data = open("data.txt",'w',encoding='utf-8')
yourPath = os.path.dirname(__file__) + '\\train\\'
text = set()
pattern = '([A-Z]?[a-z]+)'
texts_num = 0


def read_py(dir):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    global texts_num
    allFileList = os.listdir(dir)
    for file in allFileList:
        if os.path.isdir(os.path.join(dir,file)):
            read_py(dir + file + '\\')
        elif os.path.isfile(dir+file):   
            if os.path.splitext(dir+file)[1][1:].lower() == 'py':
                f = open(dir + file, "r", encoding='utf-8', errors='ignore')
                r_node = ast.parse(f.read()) 
                CodeReadability().visit(r_node)
                texts_num += 1
                logging.info("已處理 %d 個py檔" % texts_num)
            else:
                #print("其他檔案: " + dir + file)
                pass


class CodeReadability(ast.NodeVisitor):
    '''第一步'''
    def visit_Module(self, node):
        self.generic_visit(node)
    
    def visit_FunctionDef(self, node):
        if not(re.match('(__.*__)',node.name)):
            split_words = re.findall(pattern, node.name)
            for i in split_words :
                text.add(i)
            split_words.clear()

            for child in ast.walk(node):
                
                if isinstance(child, ast.Assign): 
                    for target in child.targets:
                        if isinstance(target, ast.Tuple):
                                for element in target.elts:
                                    if isinstance(element, ast.Name):
                                        split_words = re.findall(pattern, element.id)
                                        for i in split_words :
                                            text.add(i)
                        if isinstance(target, ast.Name): 
                                split_words = re.findall(pattern, target.id)
                                for i in split_words :
                                        text.add(i)

                if isinstance(child, ast.Attribute):
                        split_words = re.findall(pattern, child.attr)
                        for i in split_words :
                                text.add(i)
                split_words.clear()

        for index, t in enumerate(text):
            if len(t) > 0:
                for token in t:
                    data.write(str(token.lower()))
            if(index != len(text)-1):
                data.write(' ')
            else:
                data.write('\n')
        text.clear()

        self.generic_visit(node)

    def visit_ClassDef(self, node):
        split_words = re.findall(pattern, node.name)
        for i in split_words :
            text.add(i)
        split_words.clear()

        for child in ast.walk(node):
            if isinstance(child, ast.FunctionDef):
                if not(re.match('(__.*__)',child.name)):
                    split_words = re.findall(pattern, child.name)
                    for i in split_words :
                        text.add(i)
            split_words.clear()
        
        for index, t in enumerate(text):
            if len(t) > 0:
                for token in t:
                    data.write(str(token.lower()))
            if(index != len(text)-1):
                data.write(' ')
            else:
                data.write('\n')
        text.clear()

        self.generic_visit(node)



if __name__ == '__main__':
    # print(os.path.dirname(__file__))
    read_py(yourPath)
    data.close()