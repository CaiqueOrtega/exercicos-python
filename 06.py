def scrabble_score(palavra):
    letras_valores = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    
    palavra = palavra.upper().replace(" ", "")
    
    score = 0
    
    for letra in palavra:
        if letra in letras_valores:
            score += letras_valores[letra]
    
    return score

def main():
    palavra = input("Digite a palavra para calcular o Scrabble Score: ")
    score = scrabble_score(palavra)
    print(f"Scrabble Score de '{palavra}' é: {score}")


main()