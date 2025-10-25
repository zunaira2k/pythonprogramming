def read_numbers_from_file(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  
                words = str(line).replace(",", "").replace(".", "").split(" ")
                lines.append(words)
    print(lines)  
    return lines

def total_words(lines):
  num = 0
  for i in lines:
      num = num +len(i)
  return num

def total_character(lines):
  num = 0
  for i in lines:
     for j in i:
        num = num+ len(j)
  return num

def longest_line(lines):
  max = 0
  for i in lines:
    if(max< len(i)):
       max = len(i)
       line = i
  return line



filePath = input("Please enter file Path: ")
lines= read_numbers_from_file(filePath)
longLine =  longest_line(lines)
words = total_words(lines)
character = total_character(lines)
print("Total Numbers of Lines:", len(lines))
print("Total Numbers of Words:",words)
print("Total Numbers of Characters:",character)
print("Longest Line: ",longLine)
print("Longest Line length:",len(longLine))
print("Avearge Word Count:",character/words)
