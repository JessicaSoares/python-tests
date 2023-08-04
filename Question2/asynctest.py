import time

user_array = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    received_input = input(f"Element {i + 1}: ")
    user_array.append(received_input)

print("Array:", user_array)
delay = 1
for caractere in user_array:
    print(caractere)
    time.sleep(delay)
    delay *= 2
    print(f"Character {caractere} is printed in {delay} sec")

