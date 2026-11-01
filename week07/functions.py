# AI DISCLOSURE
# Tool Used: ChatGPT 6
# Prompt: what does the error mean? 'IndexError print(sales(i))' context: sales = [120, 80, 250, 175, 90]
# Adaptation: I read and understood where I might've been missing a value and updated line 17 based on the index of line 4.

# --- Self-Assessment Questions ---
# 1. The first bug I found was the colon missing. I actually found it from simply reading the code to myself.
#    I feel like that told me that I have a pretty decent grasp on some of the things we've learned so far
#    as I was able to identify and remember the missing colon from the 'for' statement.
# 2. The apply_discount function takes the original price and the tier of the customers discount to determine
#    and return the final price after the discount is applied. I don't believe a colleague could use it 
#    without reading the body as they dont know what the tiers or values for each tier are.

# --- Exercise 1 ---

def calculate_tax(price, rate): 
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f'Tax on $100 at 7%: ${tax1:.2f}')
print(f'Tax on $250 at 8%: ${tax2:.2f}')

# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == 'gold':
        return price * 0.85
    elif tier == 'silver':
        return price * 0.90
    elif tier == 'bronze':
        return price * 0.95
    else:
        return price


original_price = 200

for tier in ['gold','silver','bronze','none']:
    print(f'{tier}: ${apply_discount(original_price, tier):.2f}')


# --- exercise 3 ---

def final_price(price, tier, rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, rate)
    return discounted_price + tax

print(f'After gold discount: ${apply_discount(original_price, 'gold'):.2f}')
print(f'After tax: ${final_price(200,'gold',0.07):.2f}')
print(f'final_price(price, tier, rate) = ${final_price(200, 'gold', 0.07):.2f}')

# --- Exercise 4 ---

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, tier, rate)
    print(f'Price: ${price} | Tier:{tier} | Total: ${total:.2f}')

# --- Exercise 5 ---

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale            #was before replacing the old value with the new value rather than adding it to the total
print(f"Total: ${total}")

count = 0
for sale in sales: #missing the colon, so the for loop wouldnt execute
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):     #there are 5 items in the list, but the index only goes up to 4, so index 5 doesnt exist
    print(sales[i])
    i += 1

# --- Exercise 6 ---

x = 100               #global x

def double_it():
    x = 999           #local x
    return x * 2

print(x)
print(double_it())
print(x)

# The function includes its own local 'x' set to 999. so it uses that value instead of the global 'x'.
# Then outside of any function 'x' is set to 100 making it a global variable.
# The local 'x' inside the function has no effect on the global 'x'.