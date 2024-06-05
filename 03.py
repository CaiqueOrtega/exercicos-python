

def main():
    salario = float(input('>Entre com o salario:'))
    reajuste = float(input('>Entre com o valor percentual do reajuste:'))
    
    salario += salario * (reajuste / 1000)
    
    print("O Valor do Salario com Reajuste é:", salario)
    
main()