s#import
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac ou Linux
    else:
        _ = system('clear')

# Função principal do jogo
def game():
    limpa_tela()

    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    # ✅ Correção: Renomeado `palavra` para `lista_palavras` para evitar confusão
    lista_palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    # ✅ Correção: Agora escolhe uma palavra corretamente da lista
    palavra = random.choice(lista_palavras)

    # ✅ Correção: Alterado `palavra` para `palavra` (agora corretamente definida)
    letras_descobertas = ['_' for _ in palavra]

    # Número de chances
    chances = 6

    # Letras erradas
    letras_erradas = []

    # Loop enquanto houver chances disponíveis
    while chances > 0:
        # Exibe o estado atual da palavra
        print("\n" + " ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        # Entrada do usuário
        tentativa = input("\nDigite uma letra: ").lower()

        # ✅ Correção: Alterado `palavra` (antes era a lista) para `palavra` (a palavra sorteada)
        if tentativa in palavra:
            for index, letra in enumerate(palavra):  # ✅ Correção: Usando `enumerate` para melhorar a iteração
                if tentativa == letra:
                    letras_descobertas[index] = letra
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # ✅ Correção: Agora verifica corretamente se todas as letras foram descobertas
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break

    # ✅ Correção: Agora exibe corretamente a palavra em caso de derrota
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)

# Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns, Você está aprendendo programação em Python com a DSA.\n")
