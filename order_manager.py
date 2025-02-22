import csv
from datetime import datetime
from menu_item import MenuItem
from order import Order

class OrderManager:
    def __init__(self):
        self.orders = []
        self.next_order_id = 1
        self.menu_items = [
            MenuItem("Капучино", 150.00, 200),
            MenuItem("Латте", 170.00, 250),
            MenuItem("Круассан", 120.00, 150),
            MenuItem("Чизкейк", 250.00, 150),
        ]

    def create_order(self): -> Order:
        order = Order(self.next_order_id)
        self.next_order_id += 1
        self.orders.append(order)
        return order


    def view_orders(self):
        if not self.orders:
            print("Нету активных заказов")
            return
        for order in self.orders:
            print(f"\n{order}")

    def view_order(self, order_id: int):
        if order:
            print(order)
        else:
            print(f"Заказ #{order_id} не найден")

    def delete_order(self, order_id: int):
        order = self.find_order(order_id)
        if order:
            self.orders.remove(order)
            print(f"Заказ #{order_id} не найден")