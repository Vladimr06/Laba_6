import random

# Создание матрицы (с петлями)
def create_matrix(size):
    G = [[0] * size for _ in range(size)]
    rnd = random.Random()

    for i in range(size):
        for j in range(i, size):
            value = rnd.randint(0, 1)  
            G[i][j] = value
            G[j][i] = value

    return G


# Вывод матрицы + списка смежности
def print_matrix(G):
    print("\nТекущая матрица:")
    for row in G:
        print(" ".join(str(x) for x in row))

    print("\nСписок смежности:")
    for i in range(len(G)):
        neighbors = [j for j in range(len(G)) if G[i][j] == 1]
        print(f"Вершина {i}: {neighbors}")

    print("-" * 40)

# 1. ОТОЖДЕСТВЛЕНИЕ ВЕРШИН
def identification(G, v1, v2):
    size = len(G)
    if size <= 1:
        print("❌ Ошибка: Матрица содержит только 1 вершину — отождествлять нечего.")
        return G

    print(f"\nОтождествление вершин {v1} и {v2}")

    result = [row[:] for row in G]

    for i in range(size):
        if result[v1][i] == 1 or result[v2][i] == 1:
            result[v1][i] = 1
            result[i][v1] = 1

    del result[v2]
    for row in result:
        del row[v2]

    return result

# 2. СТЯГИВАНИЕ ВЕРШИН
def contraction(G, v1, v2):
    size = len(G)
    if size <= 1:
        print("❌ Ошибка: Нельзя стягивать в матрице из 1 вершины.")
        return G

    print(f"\nСтягивание вершин {v1} и {v2}")
    return identification(G, v1, v2)

# 3. РАСЩЕПЛЕНИЕ ВЕРШИНЫ
def split_vertex(G, v):
    size = len(G)
    if v >= size:
        print("❌ Ошибка: такой вершины нет.")
        return G

    print(f"\nРасщепление вершины {v}")

    new_size = size + 1
    result = [[0] * new_size for _ in range(new_size)]

    for i in range(size):
        for j in range(size):
            result[i][j] = G[i][j]

    new_v = size

    for i in range(size):
        result[new_v][i] = G[v][i]
        result[i][new_v] = G[v][i]

    result[v][new_v] = 0
    result[new_v][v] = 0

    return result

# Основной цикл операций
def operations_loop(G):
    while True:
        print("""
Выберите операцию:
1 — Отождествление вершин
2 — Стягивание вершин
3 — Расщепление вершины
0 — Выход
""")

        op = input("Введите номер операции: ")

        if op == "0":
            print("Завершение работы...")
            return

        if op in ("1", "2"):
            if len(G) <= 1:
                print("❌ Недостаточно вершин для выполнения операции.")
                continue

            try:
                v1 = int(input("Введите первую вершину: "))
                v2 = int(input("Введите вторую вершину: "))
            except:
                print("❌ Ошибка ввода.")
                continue

            if v1 >= len(G) or v2 >= len(G) or v1 < 0 or v2 < 0:
                print("❌ Такой вершины нет.")
                continue

            if v1 == v2:
                print("❌ Вершины должны быть разными.")
                continue

            if op == "1":
                G = identification(G, v1, v2)
            else:
                G = contraction(G, v1, v2)

        elif op == "3":
            try:
                v = int(input("Введите вершину для расщепления: "))
            except:
                print("❌ Ошибка ввода.")
                continue

            if v >= len(G) or v < 0:
                print("❌ Такой вершины нет.")
                continue

            G = split_vertex(G, v)

        else:
            print("❌ Неверная команда.")
            continue

        print_matrix(G)

# Главная программа
def main():
    size = int(input("Введите размер матриц: "))

    print("\nМатрица 1:")
    G1 = create_matrix(size)
    print_matrix(G1)

    print("\nМатрица 2:")
    G2 = create_matrix(size)
    print_matrix(G2)

    while True:
        choice = input("С какой матрицей работать? (1/2): ")
        if choice in ("1", "2"):
            break

    G = G1 if choice == "1" else G2

    operations_loop(G)

main()

