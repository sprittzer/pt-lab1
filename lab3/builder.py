class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
    
    def __str__(self):
        toppings = []
        if self.cheese:
            toppings.append("сыр")
        if self.pepperoni:
            toppings.append("пепперони")
        if self.mushrooms:
            toppings.append("грибы")
        if self.onions:
            toppings.append("лук")
        
        return f"Пицца {self.size} с: {', '.join(toppings) if toppings else 'ничего'}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def set_size(self, size):
        self.pizza.size = size
        return self
    
    def add_cheese(self):
        self.pizza.cheese = True
        return self
    
    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self
    
    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self
    
    def add_onions(self):
        self.pizza.onions = True
        return self
    
    def build(self):
        return self.pizza


if __name__ == "__main__":
    print("ПИЦЦЕРИЯ =)")
    
    pizza1 = (PizzaBuilder()
              .set_size("большая")
              .add_cheese()
              .add_mushrooms()
              .build())
    print(f"\nЗаказ 1: {pizza1}")
    
    pizza2 = (PizzaBuilder()
              .set_size("средняя")
              .add_cheese()
              .add_pepperoni()
              .add_onions()
              .build())
    print(f"\nЗаказ 2: {pizza2}")
    
    pizza3 = (PizzaBuilder()
              .set_size("маленькая")
              .build())
    print(f"\nЗаказ 3: {pizza3}")