#WAP to input two number and swap those value.
a=int(input(" enter a value "))
b=int(input(" enter b value "))
print(f"before swap a = {a} And b = {b}")
b=a+b
a=b-a
b=b-a
print(f"After swap a = {a} And b = {b}")
