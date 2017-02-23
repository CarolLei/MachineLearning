#-*- coding: UTF-8 -*-

from collections import Counter
import re
import codecs

in_file = codecs.open("data.txt","r",encoding = "utf-8")
wordlist = in_file.read()
#print wordlist
pattern = re.compile(u'[\u4e00-\u9fa5]+') #这个u加的太诡异了
wordlist_re = pattern.findall(wordlist)
#print wordlist_re
#for word in wordlist_re:
#    print word
#    print len(word)

dict = {}
for i in range(0,len(wordlist_re)-1):
    if len(wordlist_re[i]) >= 2 and len(wordlist_re[i+1]) >= 2:
        double_word = wordlist_re[i] + wordlist_re[i+1]
        if double_word not in dict:
            dict[double_word] = 1
        else:
            dict[double_word] = dict[double_word] + 1

dict_sort = sorted(dict.items(),key = lambda dict:dict[1],reverse = True)
for i in range(0,10):
    print "%s : %d" %(dict_sort[i][0],dict_sort[i][1])

in_file.close()

#输出结果
#这种情况 : 77
#没有什么 : 70
#这个问题 : 57
#因为他们 : 55
#如果我们 : 50
#所有这些 : 47
#这种观点 : 46
#这个世界 : 40
#但是如果 : 38
#他们自己 : 38