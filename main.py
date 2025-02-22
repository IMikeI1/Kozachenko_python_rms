from order_manager import OrderManager

def manager_menu():
    print("\nУправлениями заказами кафе")
    print("1. Создать новый заказ")
    print("2. Просмотреть все заказы")
    print("3. Просмотреть заказ")
    print("4. Удалить заказ")
    print("5. Выход")

def create_order(manager: OrderManager):
    order = manager.create_order()
    while True:
        print("\nДоступные позиции меню:")
        for i, item in enumerate(manager.menu_items, 1):
            print(f"{i}. {item}")
        print("0. Завершение заказа")


        choice = input("Выберите позицию (0-4): ")
        if choice == "0":
            break
        try:
            item_index = int(choice) - 1
            if 0 <= item_index < len(manager.menu_items):
                order.add_item(manager.menu_items[item_index])
                print("Позиция добавлена в заказ")
            else:
                print("Неверный выбор")
        except ValueError:
            print("Пожалуйста, введите число")

def main():
    manager = OrderManager()
    manager.load_orders_from_csv("orders.csv")
    while True:
        display_menu()
        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            create_order(manager)
        elif choice == "2":
            manager.view_orders()
        elif choice == "3":
            try:
                order_id = int(input("Введите номер заказа" ))
                manager.view_orders(order_id)
            except ValueError:
                print("Пожалуйста, введите число")
        elif choice == "4":
            try:
                order_id = int(input("введите номер заказа для удаления: "))
                manager.delete_order(order_id)
            except ValueError:
                print("Пожалуйста, введите число")
        elif choice == "5":
            manager.save_orders_to_csv("orders.csv")
            print("Данные сохранены. До свидание!")
            break
        else:
            print("Неверный выбор. пожалуйста выберите от 1 до 5")

if __name__ == "__main__":
    main()