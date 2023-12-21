class Coffee:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.getter
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not hasattr(self,'name') and isinstance(name,str) and len(name) >= 3:
            self._name = name
   
       
    def orders(self):
        coffee_orders = []
        for order in Order.all:
            if (order.coffee == self):
                coffee_orders.append(order)
        return coffee_orders

       
    def customers(self):
        customers_set = set()
        for order in Order.all:
            if order.coffee == self:
                customers_set.add(order.customer)
        return list(customers_set)
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        if not orders:
            return None  # or any other value you want to return for an empty list

        total_price = sum(order.price for order in orders)
        return total_price / len(orders)

class Customer:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.getter
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
       if isinstance(value, str) and 1 <= len(value) <= 15:
           self._name = value
        
    def orders(self):
        customer_orders = []
        for order in Order.all:
            if order.customer == self:
                customer_orders.append(order)
        return customer_orders
    
    def coffees(self):
        return list(set(order.coffee for order in self.orders()))
    
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        return order  
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
    @property
    def price(self):
        return self._price  
    @price.getter
    def price(self):
        return self._price
    @price.setter
    def price(self,price):
        if not hasattr(self,'price'):
            self._price = price

  
