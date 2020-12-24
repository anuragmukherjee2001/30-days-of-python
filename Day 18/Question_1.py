from collections import Counter

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

split_to_list = paragraph.split()
count = Counter(split_to_list)
occured = count.most_common(22)

print(occured)