list = list(input("Please enter numbers with duplicates "))
print(list)
ans = []
for i in list:
    if i not in ans:
        ans.append(i)
print(ans)      