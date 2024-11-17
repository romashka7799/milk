with open('C:\\Users\\Борис\\Desktop\\универ\\практика 10\\ЕАБ_уб-42_vvod.txt', 'r') as file:
    # читаем размер матрицы
    rows, cols = map(int, file.readline().split())
    N = []
    for _ in range(rows):
        row = list(map(int, file.readline().split()))
        N.append(row)
        
with open('C:\\Users\\Борис\\Desktop\\универ\\практика 10\\ЕАБ_уб-42_vivod.txt', 'w',encoding='utf-8') as file:
    file.write("массив a[N][N]\n")
    for row in N:
        file.write(" ".join(map(str, row)) + "\n")
    #сумма элементов на главной диагонали
    s = 0
    for i in range(len(N)):
        for j in range(len(N)):
            if i == j:
                s += N[i][j]
    file.write(f"сумма элементов {s}\n")
    # Считаем количество положительных элементов
    count = 0
    for row in N:
        for elem in row:
            if elem > 0:
                count += 1
    file.write(f"положительные {count}\n")# открываем файл для записи
    
