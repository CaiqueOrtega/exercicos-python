
def main():
    inicial = int(input("Entre com o valor inicial: "))
    final = int(input("Entre com o valor final: "))
    
    if final < inicial:
        print("O valor final nao pode ser menor que o inicial")
        return
    
    while inicial <= final:
     
        if inicial%3 == 0 and inicial%5 == 0:
            print("FizzBuzz")
        elif inicial%3 == 0:
            print("Fizz")
        elif inicial%5 == 0:
            print("Buzz") 
        else:
            print(inicial)           
        inicial += 1
main()