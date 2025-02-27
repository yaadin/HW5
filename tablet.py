from device import Device

class Tablet(Device):
    def __init__(self, name, price, stock, warranty_period, screen_resolution, weight):
        super().__init__(name, price, stock, warranty_period)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}\n     Screen resolution: {self.screen_resolution}\n     Weight: {self.weight}"

    def __str__(self):
        return self.display_info()

    @staticmethod
    def browse_internet(site):
        return f"Browsing  {site}..."

    @staticmethod
    def use_touchscreen(touch):
        return f"Touching {touch}..."