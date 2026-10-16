import math
import random
import platform


# 1. Generate a random integer between 1 and 100
number = random.randint(1, 100)
print(f"Number: {number}")

# 2. Calculate the square root
sqrt_result = math.sqrt(number)
print(f"Square root: {sqrt_result}")

# 3. Round it down
rounded = math.floor(sqrt_result)
print(f"Rounded down: {rounded}")

# 1. Get the OS name
os_name = platform.system() 

# 2. Get the Python version
python_version = platform.python_version()
print(f"Operating System: {os_name}")
print(f"Python Version: {python_version}")
print(platform.machine())
print(platform.processor()) # CPU name
print(platform.node())      # computer name