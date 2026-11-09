# База данных для хранения записей автосервиса
appointments = []

def get_free_time():
    print("\n--- Доступные слоты для записи ---")
    all_slots = [f"{hour}:00" for hour in range(9, 19)]
    booked_slots = [app["time"] for app in appointments]
    has_free = False
    for slot in all_slots:
        if slot not in booked_slots:
            print(f"[ ] {slot}")
            has_free = True
    if not has_free:
        print("К сожалению, все слоты на сегодня заняты.")

def add_appointment():
    print("\n--- Запись нового клиента ---")
    time_input = input("Введите время (например, 14:00): ").strip()
    
    all_slots = [f"{hour}:00" for hour in range(9, 19)]
    if time_input not in all_slots:
        print("Ошибка: Автосервис работает с 9:00 до 18:00. Вводите время в формате ЧЧ:00.")
        return
        
    for app in appointments:
        if app["time"] == time_input:
            print("Ошибка: Это время уже занято другим клиентом!")
            return
            
    name = input("Введите имя клиента: ").strip()
    car = input("Введите марку автомобиля: ").strip()
    
    if not name or not car:
        print("Ошибка: Имя и марка машины не могут быть пустыми!")
        return
        
    appointments.append({"time": time_input, "name": name, "car": car})
    print(f"Успешно! Клиент {name} на машине {car} записан на {time_input}.")

def show_all_appointments():
    print("\n--- Список всех записей на день ---")
    if not appointments:
        print("На сегодня записей нет.")
        return
    
    sorted_apps = sorted(appointments, key=lambda x: x["time"])
    for app in sorted_apps:
        print(f"[{app['time']}] Клиент: {app['name']}, Авто: {app['car']}")

def cancel_appointment():
    print("\n--- Отмена записи ---")
    name_input = input("Введите имя клиента для отмены записи: ").strip()
    
    found_apps = [app for app in appointments if app["name"].lower() == name_input.lower()]
    
    if not found_apps:
        print(f"Записей на имя {name_input} не найдено.")
        return
        
    # Удаляем найденные записи
    global appointments
    appointments = [app for app in appointments if app["name"].lower() != name_input.lower()]
    print(f"Успешно! Все записи для клиента {name_input} были отменены.")

def search_appointment_by_name():
    print("\n--- Поиск записи по имени ---")
    name_input = input("Введите имя клиента для поиска: ").strip()
    
    found_apps = [app for app in appointments if app["name"].lower() == name_input.lower()]
    
    if not found_apps:
        print(f"Записей для клиента {name_input} не найдено.")
        return
        
    print(f"Найдено записей: {len(found_apps)}")
    for app in found_apps:
        print(f"[{app['time']}] Автомобиль: {app['car']}")

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
            add_appointment()
        elif choice == "3":
            show_all_appointments()
        elif choice == "4":
            cancel_appointment()
        elif choice == "5":
            search_appointment_by_name()
        elif choice == "0":
            print("Программа завершена. До свидания!")
            break
        else:
            print("Ошибка: Неверный пункт меню. Попробуйте снова.")

if __name__ == "__main__":
    main()
