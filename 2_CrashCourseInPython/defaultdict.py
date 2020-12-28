word_counts ={}
for word in document:
  if word in word_counts:
    word_count[word]+=1
  else:
    word_counts[word]=1

#Forgiveness is better than permission
word_counts ={}
for word in word_counts:
  try:
    word_counts[word]+=1
  except KeyError:
    word_counts[word]=1

word_counts ={}
for word in document:
  previous_count = word_counts.get(word,0)
  word_counts[word]=previous_count + 1

from collections import defaultdict

word_counts = defaultdict(int)
for word in document:
  word_counts[word]+=1

dd_list = defaultdict(list)
dd_list[2].append(1)

dd_dict = defaultdict(dict)
dd_dict["Joel"]["City"] ="seatle"
dd_pair = defaultdict(lambda:[0,0])

dd_pair[2][1]=1