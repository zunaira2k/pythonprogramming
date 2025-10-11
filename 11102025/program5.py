list1 = list(input("Please enter list 1 "))
list2 = list(input("Please enter list 2 "))

print("Elements common in both the lists ")
for i  in list1:
    if i in list2:
        print(i)

ul1 = []
print("Elements unique in list1: ")       
for i in list1:
    if i not in  ul1:
        ul1.append(i)
print(ul1)               

ul2 = []
print("Elements unique in list2: ")       
for i in list2:
    if i not in  ul2:
        ul2.append(i)   
print(ul2)
ans = []
i = j = 0
while(i < len(list1) and j < len(list2)):
    if list1[i]<list2[j]:
        if list1[i] not in ans:
            ans.append(list1[i])
            i = i+1
    else:
         if list2[j] not in ans:
            ans.append(list2[j])
            j = j+1
       
if(i < len(list1)):
    if list1[i] not in ans:
        ans.append(list1[i])
        i = i+1

if(j < len(list2)):
    if list2[j] not in ans:
        ans.append(list2[j])
        j = j+1 
print("Sorted list")
print(ans)