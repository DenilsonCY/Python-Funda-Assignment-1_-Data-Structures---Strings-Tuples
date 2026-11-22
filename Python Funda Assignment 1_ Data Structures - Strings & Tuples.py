str1 = "Hello"
name = input("Enter your Name: ")

greeting = str1 + " " + name
print(greeting)

str3 = ", welcome to Python programming"
full_message = greeting + str3
print(full_message)

print("First char:", full_message[0])
print("Last char:", full_message[-1])
print("First 5:", full_message[:5])
print("Last 11:", full_message[-11:])
print("Reverse:", full_message[::-1])

start = full_message.find("Python")
print("Python word:", full_message[start:start+6])

strM = "Python beginner tutorial"

print("Uppercase:", strM.upper())
print("Lowercase:", strM.lower())
print("Capitalized:", strM.capitalize())
print("Count of 't':", strM.count('t'))
print("Replaced:", strM.replace("Python", "Machine Learning"))

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

t_combine = tuple1 + tuple2
print("Combined tuple:", t_combine)
print("Repeated 3 times:", t_combine * 3)
print("3rd element:", t_combine[2])
print("First three:", t_combine[:3])
print("Last three:", t_combine[-3:])
