def function_name():
    # Code goes here
    # Must be indented
    pass

def check_weather():
    temperature = 16
    if temperature > 25:
        print("It's hot")
    else:
        print("It's nice weather!")

check_weather()

def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")

greet("Martin", "Kim")
greet(first_name="Martin", last_name="Kim")

###
def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

calculate_total(100, 0.08, 10)

### Returns (allow us to caputre and store that information)
def add_return(a, b):
    return a + b

result = add_return(a=5, b=10)
  
def calculate_area(width, height):
    area = width * height
    return area

room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sqt feet")

def simple_function():
    numbers = [1, 2, 3, 4, 5]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number, last_number

first_number, last_number = simple_function()
print(first_number)