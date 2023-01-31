#Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve

#'Fizz' se o número for divisível por 3 e não for divisível por 5;
#'Buzz' se o número for divisível por 5 e não for divisível por 3;
#'FizzBuzz' se o número for divisível por 3 e por 5;

#Caso a função não seja divisível por 3 e também não seja divisível por 5,
#ela deve devolver o número recebido como parâmetro.

#Note que

#fizzbuzz(3) deve devolver Fizz
#fizzbuzz(5) deve devolver Buzz
#fizzbuzz(15) deve devolver FizzBuzz
#fizzbuzz(4) deve devolver 4

#As cadeias de caracteres Fizz e Buzz devem respeitar letras maiúsculas e minúsculas

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