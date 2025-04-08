def greet(name):
  """This function greets the person passed in as a parameter."""
  print(f"Hello, {name}!")

def add(num1, num2):
  """This function adds two numbers and returns the result."""
  sum_result = num1 + num2
  return sum_result

def is_even(number):
  """This function checks if a number is even and returns True or False."""
  if number % 2 == 0:
    return True
  else:
    return False

def is_odd(number):
  """This function checks if a number is even and returns True or False."""
  if number % 2 != 0:
    return True
  else:
    return False

# Example of calling the functions within the same file
if __name__ == "__main__":
  greet("Alice")
  result = add(5, 3)
  print(f"The sum of 5 and 3 is: {result}")
  print(f"Is 10 even? {is_even(10)}")
  print(f"Is 7 even? {is_even(7)}")