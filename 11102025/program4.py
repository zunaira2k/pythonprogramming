
n=int(input("Enter the number of Rows of matrices:- "))        
m=int(input("Enter the number of Columns of matrices:- "))

print("Enter the first Matrix")
A=[[int(input(f"A[{i}][{j}]: "))for j in range(m)] for i in range(n)]  
print("Enter the second Matrix")
B=[[int(input(f"B[{i}][{j}]: "))for j in range(m)] for i in range(n)]

Addition= [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]     
print("Addition Matrix of Matrix A and Matrix B is ", Addition)