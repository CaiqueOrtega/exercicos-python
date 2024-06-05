

def main():
    a = input(">Entre com o valor de A:")
    b = input(">Entre com o valor de B:")
    
    a, b = b, a
    
    print("O valor invertido é A ", a, " o valor de B é ", b)
    
main()