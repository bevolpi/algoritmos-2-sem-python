'''Fibonacci, Quantas Chamadas? -> ver debbug caso não entenda'''
#variável global
chamada = 0

def fib(x): # -> váriavel local
    global chamada
    #chamada = 1 -> não tem a ver com o problema, mas ver direito dps
    if x == 0: return 0
    elif x == 1: return 1
    chamada += 2
    return fib(x-2) + fib(x-1)

 #programa principal
n = int(input("Quantos fibonaccis você quer descobrir? "))
for i in range(n):
    x = int(input())
    chamada = 0
    f = fib(x)
    print(f"fib({x}) = {chamada} calls = {f}")

