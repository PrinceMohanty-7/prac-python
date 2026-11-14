def has_fast(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return True
        seen.add(number)
    return False

numbers = [10,22,55,90,10,69]
result = has_fast(numbers)
if result:
    print("Duplicates found")
else:
    print("Duplicate not found")


