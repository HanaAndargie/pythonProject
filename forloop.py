# def greet_user(name, age):
#     print(f'hi {name}')
#     print(f'your age is {age}')
#
# greet_user("hana", 30)

#try except
try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("invalid value")