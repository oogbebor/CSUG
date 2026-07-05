class cookie_cutter:
    def __init__(self, coat, base, base_price):
        self.coat = coat
        self.base = base
        self.__discount_rate = 0.10
        self.__final_price = base_price * (1 - self.__discount_rate)

    def flavour(self):
        print(f"The cookie has chocolate flavour coated with {self.coat}.")
        
    def price(self):
        return self.__final_price
#Creating instances of the cookie class
cookie1 = cookie_cutter("white chocolate", "vanilla", 2.50)
cookie2 = cookie_cutter("dark chocolate", "chocolate", 3.00)

cookie1.flavour()
cookie2.flavour()

print(f"The cookie has chocolate flavour coated with {cookie1.coat}.")
print(f"The cookie has chocolate flavour coated with {cookie2.coat}.")

# Output:
The cookie has chocolate flavour coated with white chocolate.
The cookie has chocolate flavour coated with dark chocolate.

print(f"Price of cookie1: ${cookie1.price():.2f}")
print(f"Price of cookie2: ${cookie2.price():.2f}")

# Output:
    Price of cookie1: $2.25
    Price of cookie2: $2.70

# Trying to access the hidden attribute directly fails:
print(cookie1.__discount)
AttributeError: 'CookieCutter' object has no attribute '__discount'
