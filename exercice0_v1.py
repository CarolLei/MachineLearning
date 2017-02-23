#-*- coding: UTF-8 -*-


from collections import Counter
import codecs
in_file = open("data.txt","r")
wordlist = in_file.read().split(" ")


dict = {}
for i in range(0,len(wordlist)-1):
    if len(wordlist[i]) >= 6 and len(wordlist[i+1]) >= 6:
        double_word = wordlist[i] + wordlist[i+1]
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
#这个问题 : 56
#因为他们 : 54
#如果我们 : 47
#这种观点 : 46
#所有这些 : 44
#这个世界 : 40
#他们自己 : 38
#我们可以 : 37
