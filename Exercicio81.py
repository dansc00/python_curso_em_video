# Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo n e devolva a soma de todos os inteiros entre 1 e n que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.

# Dica1: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser somado apenas uma vez. Uma boa solução para este exercício é fazer um laço de 1 até n  testando se o número é hipotenusa de algum triângulo e somando em caso afirmativo. Uma solução que dificilmente vai dar certo é fazer um laço construindo triângulos e somando as hipotenusas inteiras encontradas.

# Dica2: primeiro faça uma função é_hipotenusa que diz se um número inteiro é o comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou não.