def has_duplicates(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                return True
    return False

numbers = [10,22,55,90,52,69]
result = has_duplicates(numbers)
if result:
    print("Duplicates found")
else:
    print("Duplicate not found")

