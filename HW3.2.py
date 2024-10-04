import turtle

def koch_snowflake(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)
        t.right(120)
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)

def draw_snowflake(t, length, level):
    for _ in range(3):
        koch_snowflake(t, length, level)
        t.right(120)

def main():
    # Введення рівня рекурсії від користувача
    level = int(input("Введіть рівень рекурсії: "))

    # Налаштування вікна turtle
    window = turtle.Screen()
    window.title("Сніжинка Коха")

    # Налаштування черепашки turtle
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 90)  # Початкове положення для сніжинки
    t.pendown()

    # Малювання сніжинки Коха
    draw_snowflake(t, 300, level)

    # Завершення малювання
    window.mainloop()

if __name__ == "__main__":
    main()
