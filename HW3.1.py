def hanoi(n, source, target, auxiliary, state):
    if n == 1:
        state[target].append(state[source].pop())
        print(f"Перемістити диск з {source} на {target}: {state[target][-1]}")
        print(f"Проміжний стан: {state}")
    else:
        hanoi(n - 1, source, auxiliary, target, state)
        hanoi(1, source, target, auxiliary, state)
        hanoi(n - 1, auxiliary, target, source, state)

def main():
    n = int(input("Введіть кількість дисків: "))
    state = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    
    print(f"Початковий стан: {state}")
    hanoi(n, 'A', 'C', 'B', state)
    print(f"Кінцевий стан: {state}")

if __name__ == "__main__":
    main()
