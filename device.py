class Device:
    def __init__(self, name, price: int , stock, warranty_period):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty_period = warranty_period

    def display_info(self):

        return f"Name: {self.name}\nPrice: {self.price}\nStock: {self.stock}\nWarranty Period: {self.warranty_period}"

    def __str__(self):
        return f"Name: {self.name}\nPrice: {self.price}\nStock: {self.stock}\nWarranty Period: {self.warranty_period}"
    def apply_discount(self, discount_percentage:int):
        self.price = round(self.price * (1 - discount_percentage / 100))

    def is_available(self, amount):
        if self.stock >= amount:
            return "YES"
        return "NO"

    def reduce_stock(self, amount):
        if self.stock >= amount:
            self.stock -= amount
            return True
        return False














