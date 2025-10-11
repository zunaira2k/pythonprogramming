print("Please enter ten 10 numbers")
list = []
max = -99999
min = 99999
for i in range(10):
   num =  int(input("Enter Number"))
   list.append(num)
   if(num<min):
      min = num
   if(num> max):
      max = num   


print("Max number: ",max)
print("Min number: ",min)
print("Reverse list: ",list[::-1])