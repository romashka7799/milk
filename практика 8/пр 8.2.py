#8.2

B = [[1,2,3,4], [5,6,7,8]]
print('массив B[N][M]')

for i in range(len(B)):
    max_value = B[i][0]  
    min_value = B[i][0]  
    max_index = 0    
    min_index = 0 

    for j in range(len(B[i])):
        if B[i][j] > max_value:
            max_value = B[i][j]
            max_index = j
        if B[i][j] < min_value:
            min_value = B[i][j]
            min_index = j
            
   
B[i][max_index], B[i][0] = B[i][0], B[i][max_index] 
B[i][min_index], B[i][0] = B[i][0], B[i][min_index] 
   

print('Максимальный:',max_value , 'Минимальный:',min_value)
print('новый массив после перестановки:',B)