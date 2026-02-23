pizza_orders=["cheese", "pepperoni", "canadian bacon", "Sausage", "black olive"]
finished_pizzas []
while pizza_orders:
    current_pizza = pizza_orders.pop(0)
print("Your pizza pie is finished!!")
finished_pizzas.append(current_pizza)
print("\nAll pizzas are finished:\n")
for pizza in finished_pizzas:
    print(f"The pizza {pizza} was made.")
    