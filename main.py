from pprint import pp

from bing import Bing
from xbox import Xbox


def main():
    bing = Bing()
    xbox = Xbox()

    for m in range(1, 13):
        print(f"mes: {m}")

        pontos = sum(xbox.mes(False))
        bing.mes()
        pontos += bing.total
        print("pontos")
        print(f"{pontos:,}".replace(",", "."))

        valor = 25 / 4085 * pontos
        game_pass = 119.9

        print(f"R$ {valor:.2f}".replace(".", ","))

        print(f"game pass: R$ {game_pass:.2f}".replace(".", ","))

        soma = game_pass - valor

        print(f"soma: {soma:.2f}".replace(".", ","))
        print()

        bing.total = 0


if __name__ == "__main__":
    main()
