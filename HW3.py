import os
import shutil
import argparse

def copy_files_recursively(src_dir, dest_dir='dist'):
    # Переконуємось, що шлях до директорії призначення існує
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            # Отримуємо шлях до файлу та його розширення
            file_path = os.path.join(root, file)
            file_extension = file.split('.')[-1]

            # Визначаємо новий шлях для файлу
            new_dir = os.path.join(dest_dir, file_extension)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)

            # Копіюємо файл у відповідну піддиректорію
            try:
                shutil.copy2(file_path, new_dir)
                print(f"Файл {file} скопійовано у {new_dir}")
            except Exception as e:
                print(f"Не вдалося скопіювати файл {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширенням")
    parser.add_argument("source", help="Вихідна директорія")
    parser.add_argument("destination", nargs='?', default="dist", help="Директорія призначення (за замовчуванням 'dist')")
    args = parser.parse_args()
    
    # Виводимо отримані аргументи для дебагу
    print(f"Отримані аргументи: source={args.source}, destination={args.destination}")

    # Викликаємо функцію копіювання файлів
    copy_files_recursively(args.source, args.destination)

if __name__ == "__main__":
    main()
    
    #/usr/bin/python3 /Users/a1234/goit-algo-hw-03/HW3.py /Users/a1234/Desktop/source_directory /Users/a1234/Desktop/destination_directory
    #/usr/bin/python3 /Users/a1234/goit-algo-hw-03/HW3.py /Users/a1234/Desktop/source_directory
