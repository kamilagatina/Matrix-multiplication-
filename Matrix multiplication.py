#На вход программе подаются два натуральных числа n и m
#m — количество строк и столбцов в первой матрице, затем элементы первой матрицы, затем пустая строка. Далее следуют числа 
#m и k, k — количество строк и столбцов второй матрицы затем элементы второй матрицы.
#Программа выводит результирующую матрицу, разделяя элементы символом пробела
n,m = [int(i) for i in input().split()]
matrix1 = [[int(i) for i in input().split()] for _ in range(n)]
pusto = input()
m,k = [int(i) for i in input().split()]
matrix2 = [[int(i) for i in input().split()] for _ in range(m)]
matrix = [[] for _ in range(n)]
s = []
for z in range(n):
    for i in range(n):
        element = 0
        for j in range(m):
            element = element + matrix1[z][j]*matrix2[j][i]
        matrix[z].append(element)
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end = ' ')
    print()
#The input to the program is two natural numbers n and m
#m is the number of rows and columns in the first matrix, then the elements of the first matrix, then the empty string. Numbers follow
#m and k, k is the number of rows and columns of the second matrix, then the elements of the second matrix.
#The program displays the resulting matrix, separating the elements with a space character