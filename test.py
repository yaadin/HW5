import unittest
from device import Device
from smartphone import Smartphone
from laptop import Laptop
from tablet import Tablet
from cart import Cart

class TestDevice(unittest.TestCase):
    def setUp(self):
        self.device1 = Device("Iphone 13", 999, 10, 24)
        self.device2 = Device("Samsung Galaxy S22", 1099, 8, 24)

    def test_display_info(self):
        self.assertEqual(self.device1.display_info(),"Name: Iphone 13\nPrice: 999\nStock: 10\nWarranty Period: 24")
        self.assertEqual(self.device2.display_info(),"Name: Samsung Galaxy S22\nPrice: 1099\nStock: 8\nWarranty Period: 24")

    def test_apply_discount(self):
        self.device1.apply_discount(10)
        self.assertEqual(self.device1.price, 899)
 
    def test_is_available(self):
        self.assertEqual(self.device1.is_available(5),"YES")
        self.assertEqual(self.device2.is_available(10),"NO")

    def test_reduce_stock(self):
        self.assertTrue(self.device1.reduce_stock(5))
        self.assertFalse(self.device2.reduce_stock(10))

class TestSmartphone(unittest.TestCase):
    def setUp(self):
        self.smartphone = Smartphone("Iphone 13", 999, 10, 24, "6.1 inch", "19 hours")


    def test_make_call(self):
        self.assertEqual(self.smartphone.make_call("996709785"), "Dialing ... 996709785 Call in progress...")

    def test_instaling_app(self):
        self.assertEqual(self.smartphone.install_app("Instagram"), "Instagram successfully installed")


class TestLaptop(unittest.TestCase):
    def setUp(self):
        self.laptop = Laptop("MacBook Pro M2", 1999, 5, 36, "16GB", "3.2 GHz")

    def test_run_program(self):
        self.assertEqual(self.laptop.run_program("VS code"), "VS code is running")


    def test_use_keyboard(self):
        self.assertEqual(Laptop.use_keyboard(), "Typing...")


class TestTablet(unittest.TestCase):
    def setUp(self):
        self.tablet = Tablet("iPad Pro", 1299, 10, 24, "2732x2048", "600g")

    def test_browse_internet(self):
        self.assertEqual(self.tablet.browse_internet("www.google.com"), "Browsing  www.google.com...")


    def test_use_touchscreen(self):
        self.assertEqual(Tablet.use_touchscreen("interface"), "Touching interface...")


class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.device = Device("Iphone 13", 999, 10, 24)
        self.cart.add_device(self.device, 5)

    def test_add_device(self):
        self.cart.add_device(self.device, 5)
        self.assertEqual(len(self.cart.items), 2)
    

    def test_remove_device(self):
        self.cart.remove_device(self.device, 3)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0][1], 2)
        self.assertEqual(self.cart.total_price, 999 * 2)


        self.cart.remove_device(self.device, 2)
        self.assertEqual(len(self.cart.items), 0)
        self.assertEqual(self.cart.total_price, 0)

    def test_total_price(self):
        self.assertEqual(self.cart.get_total_price(), 999 * 5)

    def test_checkout(self):
        self.cart.checkout()

if __name__ == "__main__":
    unittest.main()
