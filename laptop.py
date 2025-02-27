from device import Device

class Laptop(Device):
    def __init__(self, name, price, stock, warranty_period, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty_period)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}\n     RAM size: {self.ram_size}\n     Processor speed: {self.processor_speed}"

    def __str__(self):
        return self.display_info()

    @staticmethod
    def run_program(program):
        return f"{program} is running"

    @staticmethod
    def use_keyboard():
        return "Typing..."