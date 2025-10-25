def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  
              numbers.append(float(line))  
    return numbers


def calculate_mean(numbers):
    if not numbers:
        return None  
    return sum(numbers) / len(numbers)

def merge_sort(numbers):
  
    if len(numbers) <= 1:
        return numbers


    mid = len(numbers) // 2
    left_half = merge_sort(numbers[:mid])
    right_half = merge_sort(numbers[mid:])


    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def calculate_median(numbers):
    numbers = merge_sort(numbers)
    length = len(numbers)
    mid = length // 2

    if length % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

def calculate_variance(mean, numbers):
    inner_value = 0
    for i in numbers:
        inner_value += (i - mean) ** 2
    return inner_value / len(numbers)

def calculate_standard_deviation(mean, numbers):
    inner_value = 0
    for i in numbers:
        inner_value += (i - mean) ** 2
    return (inner_value / len(numbers)) ** 0.5





filename = "C:/Users/Student/Desktop/zunaira/pythonprogramming/pythonprogramming/25102025/numbers.txt"
nums = read_numbers_from_file(filename)
mean =  calculate_mean(nums)
print("Numbers read from file: ", nums)
print("Mean of the Numbers: ", mean)
print("Mediun of the Numbers: ", calculate_median(nums))
print("Varience Numbers: ", calculate_variance(mean,nums))
print("Standard deviation: ",calculate_standard_deviation(mean,nums))



