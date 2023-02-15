from itertools import product
import string
import random

print("\t******* Word List Oluşturucu *******\n")
minimum_count = int(input("En küçük karakter sayısı:"))
maximum_count = int(input("En büyük karakter sayısı:"))
count = 0
password = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits

file_open = open("WordList.txt","w")

for i in range(minimum_count,maximum_count+1):
    for j in product(password,repeat=i):
        word = "".join(j)
        file_open.write(word)
        file_open.write("\n")
        count += 1
print("Wordlist of {} passwords created".format(count))


