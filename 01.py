

def main():
    name = input('>Entre com um Nome:').strip()
    
    if not name: 
        name = "voce"
    print('Um para ', name, " um para mim")

        
main()
