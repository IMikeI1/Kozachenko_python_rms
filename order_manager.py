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

    def create_order(self) -> Order:
        order = Order(self.next_order_id)
        self.next_order_id += 1
        self.orders.append(order)
        return order

    def view_orders(self):
        if not self.orders:
            print("Нет активных заказов")
            return
        for order in self.orders:
            print(f"\n{order}")

    def view_order(self, order_id: int):
        order = self.find_order(order_id)
        if order:
            print(order)
        else:
            print(f"Заказ #{order_id} не найден")

    def delete_order(self, order_id: int):
        order = self.find_order(order_id)
        if order:
            self.orders.remove(order)
            print(f"Заказ #{order_id} удален")
        else:
            print(f"Заказ #{order_id} не найден")

    def find_order(self, order_id: int) -> Order | None:
        return next((order for order in self.orders if order.order_id == order_id), None)

    def save_orders_to_csv(self, filename: str):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['order_id', 'created_at', 'items', 'total_price'])
            for order in self.orders:
                items_str = ';'.join(f"{item.name},{item.price},{item.weight}" for item in order.items)
                writer.writerow([
                    order.order_id,
                    order.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    items_str,
                    order.total_price
                ])

    def load_orders_from_csv(self, filename: str):
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    order_id = int(row[0])
                    created_at = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
                    items_str = row[2]

                    order = Order(order_id)
                    order.created_at = created_at

                    if items_str:
                        items = items_str.split(';')
                        for item in items:
                            name, price, weight = item.split(',')
                            menu_item = MenuItem(name, float(price), int(weight))
                            order.add_item(menu_item)

                    self.orders.append(order)
                    self.next_order_id = max(self.next_order_id, order_id + 1)
        except FileNotFoundError:
            pass