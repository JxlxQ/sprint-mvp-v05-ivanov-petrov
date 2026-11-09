# База данных для хранения записей автосервиса
# Каждая запись: {"time": "ЧЧ:ММ", "name": "Имя", "car": "Марка"}
appointments = []

def get_free_time():
    print("\n--- Доступные слоты для записи ---")
    # Генерируем рабочие часы с 9:00 до 18:00
    all_slots = [f"{hour}:00" for hour in range(9, 19)]
    
    # Находим слоты, которые уже заняты
    booked_slots = [app["time"] for app in appointments]
    
    # Выводим только свободные слоты
    has_free = False
    for slot in all_slots:
        if slot not in booked_slots:
            print(f"[ ] {slot}")
            has_free = True
            
    if not has_free:
        print("К сожалению, все слоты на сегодня заняты.")

def main():
    while True:
        print("\n=== Автосервис: запись ===")
        print("1. Показать свободное время")
        print("2. Записать клиента")
        print("3. Список всех записей на день")
        print("4. Отменить запись")
        print("5. Поиск записи по имени")
        print("0. Выход из программы")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == "1":
            get_free_time()
        elif choice == "2":
            print("Выбран пункт: Записать клиента (Функция в разработке)")
        elif choice == "3":
            print("Выбран пункт: Список всех записей на день (Функция в разработке)")
        elif choice == "4":
            print("Выбран пункт: Отменить запись (Функция в разработке)")
        elif choice == "5":
            print("Выбран пункт: Поиск записи по имени (Функция в разработке)")
        elif choice == "0":
            print("Программа завершена. До свидания!")
            break
        else:
            print("Ошибка: Неверный пункт меню. Попробуйте снова.")

if __name__ == "__main__":
    main()
