#Exercise 1

print("---  Exercise 1: Build a List ---")

inventory = ["pen", "notebook", "stapler","tape", "marker"]
print(inventory)
print(len(inventory))


#Exercise 2

print("--- Exercise 2: Index Practice ---")
print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle])

# Exercise 3

print("--- Exercise 3: List Slicing ---")

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

#Exercsie 4

print("--- Exercise 4: List Methods---")

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

#Exercise 5

print("--- Exercise 5: Tuple Comparison---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print(f"Tuples protect coordinates from being changed by accident")

print("--- Exercise 6: List Average Sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")