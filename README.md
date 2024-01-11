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


Beispiel für die Verwendung der Funktion ohne Labels:
```python
grid_size = (20, 20)
data = np.random.rand(grid_size[0] * grid_size[1])  # Erzeugt zufällige Daten für das Gitter
labels = {0: 'A', 25: 'B', 50: 'C'}  # Beispiel-Labels
plot_hexagonal_grid(data, grid_size, title='Gitter mit Labels', show_axes=False, labels=labels)
```


Installation

Sie können das Modul direkt von GitHub installieren. Stellen Sie sicher, dass Sie über die neueste Version von pip verfügen.
Installation mit pip

Um das Modul mit pip zu installieren, führen Sie den folgenden Befehl in Ihrem Terminal aus:
```bash
pip install git+https://github.com/quojus/hexagonal_plot.git
```
Ersetzen Sie IhrBenutzername und IhrRepository durch Ihren GitHub-Benutzernamen und den Namen Ihres Repositories.
Installation mit Conda



