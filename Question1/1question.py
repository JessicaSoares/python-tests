
user_array = []
n = int(input("Enter the number of elements: "))


for i in range(n):
    received_input = input(f"Enter the Element {i + 1}: ")
    user_array.append(received_input)


print("Array:", user_array)

freq = [0] * len(user_array)

for x in range(len(user_array)):
    if freq[x] == 0:
        freq_item = 1
        for j in range(x + 1, len(user_array)):
            if user_array[x] == user_array[j]:
                freq_item += 1
                freq[j] = -1  
                freq[x] = freq_item

for x in range(len(user_array)):
    if freq[x] > 0:
        print(f'"{user_array[x]}" appeared {freq[x]} times.')

duplicates = []
for x in range(len(user_array)):
    if freq[x] == 2:
        duplicates.append(user_array[x])

print(f'Duplicate items: "{duplicates}"')

