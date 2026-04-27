def add_binary(a, b):
    sum_decimal = int(a, 2) + int(b, 2)
    return bin(sum_decimal)[2:]

a = input("Enter first binary: ")
b = input("Enter second binary: ")

print("Result:", add_binary(a, b))
