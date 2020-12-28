from collections import Counter
c = Counter([0,1,2,0])

#recall,document is a list of words 
word_counts = Counter(document)

for word,count in word_counts.most_common():
  print(word,count)