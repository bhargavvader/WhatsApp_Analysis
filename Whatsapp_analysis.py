# things to do :
# 1 ) better define conversation by adding context
# 2 ) find most used words
# 3 ) find most ignored person
# 4 ) find out who uses big words
# 5 ) find out who punctuates the most (percentage)
# 6 ) make it look fancy
# 7 ) heat map

dates={}
texts={}
names={}
times={}
dictWords={}
hour={}
time={}
minute={}
words=[]
i=0
# splitting data up
for line in open('tbf.txt'):
	if(line.split('-') == [line] or line.split(':')== [line]):
		continue
	dates[i], texts[i] = line.split('-',1)
	names[i], texts[i] = texts[i].split(':',1)
	dates[i], times[i] = dates[i].split(', ',1)
	hour[i], minute[i] = times[i].split(':',1)
	i = i+1

#splitting sentences up
for text in texts:
	for word in texts[text].split():
		if word.lower() in dictWords:
			dictWords[word.lower()] += 1
		else:
			dictWords[word.lower()] = 1
			words.append(word.lower())

# most used words
for w in sorted(dictWords,key=dictWords.get,reverse=True):
	print(w,dictWords[w])

# conversations list:
conversation = 0
countNames={}

for t in range(i):
	if t == 4355:
		break
	if (hour[t] == hour[t+1] and ((int(minute[t+1]) - int(minute[t])) > 25)) or (hour[t] != hour[t+1]):
		print(texts[t+1],t+2)
		conversation = conversation +1
		if names[t+1] in countNames:
			countNames[names[t+1]] += 1
		else:
			countNames[names[t+1]] = 1

# conversation starters:
print(countNames)


talkers={}
# # mostMessages
for name in names:
	if names[name] in talkers:
		talkers[names[name]] +=1
	else:
		talkers[names[name]] = 1

print(talkers)

# heatmap
hours={}
for h in hour:
	if hour[h] in hours:
		hours[hour[h]] += 1
	else:
		hours[hour[h]] = 1

for h in sorted(hours,key=hours.get,reverse=True):
	print(h,hours[h])

# # biggest words

#Find sentiment of conversation

