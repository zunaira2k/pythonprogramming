
n=int(input("Enter the number of Rows of matrices:- "))         # Taking the dimensions from the user
m=int(input("Enter the number of Columns of matrices:- "))

print("Enter the first Matrix")
A=[[int(input(f"A[{i}][{j}]: "))for j in range(m)] for i in range(n)]   # using list comprehension method for entering the matrices.
                                                                                                    # Format= ( Expresion for item in iterable)

print("Enter the second Matrix")
B=[[int(input(f"B[{i}][{j}]: "))for j in range(m)] for i in range(n)]

Addition= [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]       # Adding the matrices element using index and loops
print("Addition Matrix of Matrix A and Matrix B is ", Addition)