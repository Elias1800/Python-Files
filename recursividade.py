#Função Fatorial
def fatorial(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return n * fatorial(n - 1) 

#Sequencia Fibonacci 
def seq_fibonacci(n):

    seq=[]
 
    for  i in range(n+1):
        seq.append(fibonacci(i))
    
    return seq

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
if __name__ == '__main__':
    print(fatorial(5))
    print(seq_fibonacci(5))