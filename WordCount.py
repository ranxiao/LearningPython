import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list =[]
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code,'html.parser')
    for post_text in soup.findAll('a',{'class':'user-name'}):
        content = post_text.string
        words = content.lower().split()
        for word in words:
            if len(word)>0:
                word_list.append(word)
    clean_up(word_list)

def clean_up(word_list):
    clean_word_list = []
    symbol = "~!@#$%^&*()_+{}|:\"<>?`-=\;',./'"
    for word in word_list:
        for i in range(len(symbol)):
            word=word.replace(symbol[i],'')
        if len(word)>0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
    word_count ={}
    for word in clean_word_list:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    fs = open('test.txt','w')
    for key, value in sorted(word_count.items(), key= operator.itemgetter(1)):
        print(key, value)
        fs.write(key+'\t'+str(value)+'\n')
    fs.close()
    print(word_count)
start('https://thenewboston.com/search.php?type=1&sort=pop&page=1')

