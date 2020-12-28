 = [4,1,2,3]
 y = sorted(x)
 x.sort()

 #sort the list by absolute value from the largest to the smallest
 x = sorted([-4,1,-2,3],key =abs,reverse=True)

 wc= sorted(word_counts.items(),key = lambda word_and_count : word_and_count[1],reverse=True)