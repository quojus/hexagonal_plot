import numpy as np
import random

def generate_large_hexagon_data(r, distribution="uniform", min_value=1, max_value=10)->dict:
    """
    Generiert ein Daten-Dictionary für ein großes Hexagon basierend auf dem Radius r.

    :param r: Der Radius des großen Hexagons.
    :param distribution: Verteilung der Werte - "uniform" (gleichmäßig) oder "normal" (normalverteilt).
    :param min_value: Das Minimum für die generierten Werte.
    :param max_value: Das Maximum für die generierten Werte.
    :return: Ein Daten-Dictionary mit Axialkoordinaten (q, r) und zugeordneten Werten.
    """
    data = {}

    for q in range(-r, r + 1):
        for s in range(max(-r, -q - r), min(r, -q + r) + 1):
            if distribution == "uniform" or distribution == "u":
                value = random.uniform(min_value, max_value)
            elif distribution == "normal" or distribution == "n":
                value = np.random.normal(loc=(min_value + max_value) / 2, scale=(max_value - min_value) / 4)
                # Hier wird eine Normalverteilung mit Mittelwert und Standardabweichung basierend auf min_value und max_value verwendet
                value = max(min_value, min(max_value, value))  # Wert auf den Bereich [min_value, max_value] beschränken
            else:
                raise ValueError("Ungültige Verteilung. Verwenden Sie 'uniform' oder 'normal'.")

            data[(q, s)] = value

    return data
