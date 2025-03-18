class MenuItem:
    def __init__(self, name: str, price: float, weight: int):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"{self.name} - {self.price} руб. ({self.weight} г)"