grades = ('A','B','A','C','B','A','A','B','C')
dic = {}
for grade in grades:
      dic[grade] = dic.get(grade,0)+1

t = tuple(dic.items()) 
print(t)