import random
import time
from pelilauta import PeliLauta
from tekoaly.minimax import paras_siirto
from toiminnot import sallittu_siirto, vapaa_rivi

peli = PeliLauta()
peli.uusi_peli()
siirrot = 42

def siirto(sarake: int, pelaaja: int):
        """Kutsuu tarvittavat funktiot siirtoa varten.

        Args:
            sarake (int): Valittu sarake.
            pelaaja (int): 1: pelaaja, 2: tekoäly

        Returns:
            boolean: Palauttaa false jos siirto ei onnistunut.
        """
        lauta = peli.lauta
        if sallittu_siirto(lauta, sarake):
            rivi = vapaa_rivi(peli.lauta, sarake)
            peli.paivita_lauta(rivi, sarake, pelaaja)
            return True
        return False

def main():
    while True:
        vastustajan_siirto = input()
        print(f"opponent move {vastustajan_siirto}")
        time.sleep(random.randrange(1,10)/100)
        if vastustajan_siirto.startswith("RESET:"):
            peli.uusi_peli()
            print("Board reset!")
            print(f"pelilauta {peli.lauta}!")
            siirrot = 42
        elif vastustajan_siirto.startswith("PLAY:"):
            valinta = paras_siirto(peli.lauta, siirrot)
            siirto(valinta, 2)
            siirrot -= 1
            # example about logs
            print(f"I chose {valinta}!")
            print(f"pelilauta {peli.lauta}!")
            # example about posting a move
            print(f"MOVE:{valinta}")
        elif vastustajan_siirto.startswith("MOVE:"):
            vas_valinta = vastustajan_siirto.removeprefix("MOVE:")
            siirto(int(vastustajan_siirto.removeprefix("MOVE:")), 1)
            siirrot -= 1
            print(f"Received move: {vas_valinta}")
            print(f"pelilauta {peli.lauta}!")
        else:
            print(f"Unknown tag: {vastustajan_siirto}")
            break

if __name__ == "__main__":
    main()
