#Name: Elijah Raji
#Class:6th hour
#Assinment:hw22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class store:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight
    def double_price(self):
        self.cost *= 2
#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
chips = store(200, 2, 1)
soda = store(300, 1.50, 3)
candy = store(500, 2.25, 0.7)
#3. Print the stock of all three objects and the cost of the second store item.
print(f"the chips stock: {chips.stock}")
print(f"the soda stock: {soda.stock}")
print(f"the candy stock: {candy.stock}")
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
soda.double_price()
print(F"the soda cost {soda.cost}")
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
candy.stock *= (1/4)
print(f"the candy stock: {candy.stock}")
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del chips

try:
    print(f"the chips stock: {chips.weight}")
except:
    print("this item no longer exist")