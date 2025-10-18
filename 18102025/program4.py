students = {
    'Alice':{
        'M1':78,
        'M2':82
    },
    'Bob':{
        'M1':90,
        'M2':88
    },
    'Carol':{
        'M1':85,
        'M2':91
    }
}
max = 0.0
sMax = 0.0
print("Average Marks of Students: ")
for k,v in students.items():
    marks = 0
    for i in v.values():
        marks  = marks+i
    percentage = marks/2
    print(k, "Percentage: ",percentage)
    if(marks > sMax and marks < max):
        sMax = marks
        second = k
    elif(marks>max):
        max = marks
        first = k
print("Topper Student: ",first)
print("Second Topper Student: ",second)


