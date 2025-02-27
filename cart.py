class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            device.reduce_stock(amount)
            return True
        return False

    def remove_device(self, device, amount):
        for i, (d, a) in enumerate(self.items):
            if d == device:
                if a > amount:
                    self.items[i] = (d, a - amount)
                    self.total_price -= device.price * amount
                    device.stock += amount
                elif a == amount:
                    self.items.pop(i)
                    self.total_price -= device.price * amount
                    device.stock += amount
                else:
                    raise ValueError("Not enough items to remove")
                break
        else:
            raise ValueError("Device not found in cart")

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        for item in self.items:
            if item[1] == 0:
                print(f"{item[0].name} - 0 units (Out of stock)")
            else:
                print(f"{item[0].name} - {item[1]} units")

    def checkout(self):
        for device, amount in self.items:
            if device.is_available(amount):
                device.reduce_stock(amount)
                print(f"{device.name} - {amount} units at ${device.price} each and total ${device.price * amount}")
            else:
                print(f"Device {device.name} is not available in the required quantity.")



