# Hexagonal Plot in Matplotlib

Dieses Skript enthält eine Funktion `plot_hexagonal_grid`, die es ermöglicht, Daten in einem sechseckigen Gitter mit Matplotlib zu visualisieren.

## Verwendung

Importieren Sie die Funktion in Ihr Python-Skript und übergeben Sie die Daten als flaches Array. Sie können auch die Gittergröße und das Farbschema anpassen.

Beispiel:
```python
from hexagonal_plot import plot_hexagonal_grid
import numpy as np

grid_size = (20, 20)
data = np.random.rand(grid_size[0] * grid_size[1])
plot_hexagonal_grid(data, grid_size)
```
Beispiel 2:
```python
grid_size = (20, 20)
data = np.random.rand(grid_size[0] * grid_size[1])  # Erzeugt zufällige Daten für das Gitter
plot_hexagonal_grid(data, grid_size, title='Mein Hexagonales Gitter', show_axes=False)
```

