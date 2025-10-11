word = input("Please enter a sentance ")
list = word.split(" ")
set = set(list)

for i in set:
    print(f"{i} : ", list.count(i))

 
    
 