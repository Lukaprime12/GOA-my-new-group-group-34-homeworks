def factorial():
    namravli = 1
    fact = int(input('enter number'))
    for i in range(1, fact + 1):
        namravli *= i
    print(namravli)
factorial()