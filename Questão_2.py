#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
#(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
#ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def pertence_fibonacci(num):
    fibonacci = [0, 1]
    
    while fibonacci[-1] < num:
        
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    
    if num in fibonacci:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci."

# Entrada
numero_informado = 55
print(pertence_fibonacci(numero_informado))
