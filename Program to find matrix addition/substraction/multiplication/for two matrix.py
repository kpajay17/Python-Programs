mat1=[]
mat2=[]
r1,c1=[int(r) for r in (input("enter the value of row and column for  first R x C matrix : ").split())]
print("Enter first matrix in row order : ")
for i in range(1,r1+1):
    print("enter",c1,"elements of",i,"row :")
    mat1.append([int(x) for x in input().split()])

r2,c2=[int(r) for r in (input("enter the value of row and column for second R x C matrix : ").split())]
print("Enter Second matrix in row order : ")
for i in range(1,r2+1):
    print("enter",c2,"elements of",i,"row :")
    mat2.append([int(x) for x in input().split()])

if r1!=r2 or c1!=c2:
    print("Sorry......Additionand Substraction is not possible....!")
else:
    print("Addition of Two Matrix is :")
    mat4=[]
    for i in range(0,r1):
        mat3=[]
        for j in range(0,c1):
            mat3.append(mat1[i][j]+mat2[i][j])
        mat4.append(mat3)
    for k in mat4:
        print(k)

    print("Substraction of Two Matrix is :")
    mat4=[]
    for i in range(0,r1):
        mat3=[]
        for j in range(0,c1):
            mat3.append(mat1[i][j]-mat2[i][j])
        mat4.append(mat3)
    for k in mat4:
        print(k)
if c1!=r2:
    print("Sorry....Multiplication is not possible")
else:
    print("Multiplication of Two Matrix is :")
    mat4=[]
    for i in range(0,r1):
        mat3=[]
        for j in range(0,c2):
            sum=0
            for k in range(0,c1):
                sum+=(mat1[i][k]*mat2[k][j])
            mat3.append(sum)
        mat4.append(mat3)
    for k in mat4:
        print(k)
