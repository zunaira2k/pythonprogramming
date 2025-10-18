data = (
    ("Electronics",1000),
    ("Clothing",700),
    ("Electronics",1200),
    ("Toys",400),
    ("Clothing",600)
)
dic = {}
for k,v in data :
    dic[k] = dic.get(k,0)+v


t  = tuple(dic.items())
print(t)