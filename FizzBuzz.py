def fizzbuzz(x):
    if x % 3 == 0 and x % 5 != 0:
        return 'Fizz'
    elif x % 5 == 0 and x % 3 != 0:
        return 'Buzz'
    elif x % 3 == 0 and x % 5 == 0:
        return 'FizzBuzz'
    elif x % 3 != 0 and x % 5 != 0:
        return x

val = int(input('Digite um número inteiro: '))
print(fizzbuzz(val))
