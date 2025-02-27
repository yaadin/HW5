from device import Device

class Smartphone(Device):
    def __init__(self, name, price, stock, warranty_period, screen_size, battery_life):
        super().__init__(name, price, stock, warranty_period)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}\n     Screen size: {self.screen_size}\n     Battery life: {self.battery_life}"

    def __str__(self):
        return self.display_info()

    @staticmethod
    def make_call(number):
        return f"Dialing ... {number} Call in progress..."

    @staticmethod
    def install_app(app):
        return f"{app} successfully installed"
