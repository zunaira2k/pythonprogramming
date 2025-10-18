data = (10,3.5,"AI",25,"ML",40.0,15)

sum = 0
len = 0

for x in data:
    if type(x) is int or type(x) is float:
     sum = sum+x
     len = len + 1

print("Average: ",sum/len)