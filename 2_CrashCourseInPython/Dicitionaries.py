empty_dict ={}
emprty_dict2 = ()
grades = {"Joel":80,"Tim":95}
joels_grade = grades["Joel"]

try:
  kates_grade =grades["Kate"]
except KeyError:
  print("no grade for Kate!")

joel_has_grade = "Joel" in grades
kate_has_grade = "Kate" in grades

joels_grade = grades.get("Joel",0) #equals 80
kates_grade = grades.get("Kate",0) #equals 0
no_ones_grade = grades.get("No one") #default is none

grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)

tweet ={
  "user":"joelgrus",
  "text":"Data Science is Awesome",
  "retweet_count":100,
  "hashtags" :["#data","#science","#datascience","#awesome","yolo"]
}
tweet_keys = tweet_keys()
tweet_values= tweet.values()
tweet_items = tweet_items()

c1 ="user" in tweet_keys #NOT PYTHONIC
c2 = "user" in tweet #PYTHONIC WAY OF CHECKING
c3 = "joelgurs" in tweet_values #TRUE (Slow but the only way to check)

