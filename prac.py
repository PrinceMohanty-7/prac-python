def find_duplicates(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                return True
    return False

numbers = [10, 20, 30, 40, 10]
result = find_duplicates(numbers)

if result:
    print("Duplicates found in the list.")
else:
    print("No duplicates found in the list.")

print(result)
    