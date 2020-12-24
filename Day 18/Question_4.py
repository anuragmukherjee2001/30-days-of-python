import re
from collections import Counter

sentence = "%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"

clean_1 = re.sub('%', '', sentence)
clean_2 = re.sub('@', '', clean_1)
clean_3 = re.sub('$', '', clean_2)
clean_4 = re.sub('&', '', clean_3)
clean_5 = re.sub(';', '', clean_4)
clean_6 = re.sub('#', '', clean_5)


print(clean_6)


split_to_list = clean_6.split()
count = Counter(split_to_list)
occured = count.most_common(3)

print(occured)

