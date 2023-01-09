import os
from collections import Counter
import matplotlib.pyplot as plt
#Load my file:
with open('t8.shakespeare.txt','r') as f:
    lines = f.readlines()

words=[]
for sentence in lines:
    for word in sentence.split():
        words.append(word)

#Count my word in a dictionnary
def dict_count(sentences):
    dict={}
    list=list()
    for word in sentences:
        if word in  list:
             dict[word]=dict[word]+1
        else:
                dict[word]=1
                list.append(word)
    return dict

#Count my word in a counter function
def counter_function(sentences):
    return Counter(sentences)

#Compute the time
def tim_func(function,text):
	time1 = time()
	result = function(text)
	time2 = time()
	return (time1-time2)

#Compute the time
print(tim_func(dict_count,words[1]))
print(tim_func(counter_function,words[1]))

#The counter_function() is quicker than the dict_count de différence is that the counter_function use less storage
#The dictionnary also use boucle so the computing is longer

dictionary=[]
counter=[]
for i in range(100):
    dictionary.append(tim_func(dict_count(),words[1]))
    counter.append(tim_func(counter_function,words[1]))

fig=plt.figure()
plt.plot(range(len(counter)),counter,label="counter")
plt.plot(range(len(dictionary)),dictionary,label="dictionary")

plt.show()
