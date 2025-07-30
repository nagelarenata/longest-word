"""Módulo do jogo The Longest Word."""

import random
import string
from collections import Counter

class Game:
    """Classe principal que representa o jogo The Longest Word."""

    def __init__(self) -> None:
        """Inicializa o jogo com uma grade aleatória de 9 letras maiúsculas."""
        self.grid = random.choices(string.ascii_uppercase, k=9)

    def is_valid(self, word: str) -> bool:
        """
        Retorna True se e somente se a palavra puder ser formada
        com as letras da grid (respeitando quantidade de letras).
        """
        if not word:
            return False

        word = word.upper()
        word_count = Counter(word)
        grid_count = Counter(self.grid)

        return all(word_count[letter] <= grid_count[letter] for letter in word)
