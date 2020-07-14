for i in range(1,100):
  if i%3:
    if i%5:
        print(i)
    else:
        print("Buzz")
  else:
    if i%5:
      print("Fizz")
    else:
      print("FizzBuzz")
