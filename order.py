from datetime import datetime
from menu_item import MenuItem

class Order:
    def __init__(self, order_id: int):
        self.order_id = order_id
        self.items = []
        self.total_price = 0.0
        self.created_at = datetime.now()

    def add_item(self, item: MenuItem):
        self.items.append(item)
        self.calculate_total()

    def remove_item(self, item: MenuItem):
        if item in self.items:
            self.items.remove(item)
            self.calculate_total()

    def calculate_total(self):
        self.total_price = sum(item.price for item in self.items)

    def __str__(self):
        items_str = "\n".join(f"- {item}" for item in self.items)
        return f"Заказ #{self.order_id}\n" \
               f"Создан: {self.created_at.strftime('%d.%m.%Y %H:%M')}\n" \
               f"Позиции:\n{items_str}\n" \
               f"Итого: {self.total_price} руб."