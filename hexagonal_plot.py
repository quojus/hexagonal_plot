# hexagonal_plot.py
# erstelt mit GPT

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

def plot_hexagonal_grid_simpel(data, grid_size=(20, 20), colormap='viridis', title=None, show_axes=True):
    """
    Plottet ein sechseckiges Gitter basierend auf den übergebenen Daten.

    :param data: Array von Werten, die jedem Sechseck zugeordnet sind (Flache Liste oder 1D Numpy-Array).
    :param grid_size: Die Größe des Gitters (Zeilen, Spalten).
    :param colormap: Farbschema für die Plots.
    :param title: Titel für das Diagramm.
    :param show_axes: Bestimmt, ob die Achsen angezeigt werden sollen.
    """
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Versteckt die Achsen, wenn show_axes False ist
    if not show_axes:
        ax.axis('off')

    # Berechnet den Radius eines Sechsecks basierend auf der Gittergröße
    radius = 1 / np.sqrt(grid_size[0]**2 + grid_size[1]**2)

    # Erstellt jedes Sechseck
    for row in range(grid_size[0]):
        for col in range(grid_size[1]):
            x = col * 1.5 * radius
            y = row * np.sqrt(3) * radius + (col % 2) * radius * np.sqrt(3) / 2
            
            hexagon = mpatches.RegularPolygon((x, y), numVertices=6, radius=radius, 
                                               orientation=np.radians(30),
                                               facecolor=plt.cm.get_cmap(colormap)(data[row * grid_size[1] + col]),
                                               edgecolor='k')
            ax.add_patch(hexagon)

    # Fügt einen Titel hinzu, wenn einer angegeben ist
    if title:
        plt.title(title)

    ax.autoscale_view()
    plt.colorbar(plt.cm.ScalarMappable(cmap=colormap), ax=ax)
    plt.show()

def plot_hexagonal_grid(data, grid_size=(20, 20), colormap='viridis', title=None, show_axes=True, label_fontsize=8, label_weight='bold', labels=None):
    """
    Plottet ein sechseckiges Gitter mit optionalen Labels auf bestimmten Zellen.

    :param data: Array von Werten, die jedem Sechseck zugeordnet sind.
    :param grid_size: Die Größe des Gitters (Zeilen, Spalten).
    :param colormap: Farbschema für die Plots.
    :param title: Titel für das Diagramm.
    :param show_axes: Bestimmt, ob die Achsen angezeigt werden sollen.
    :param label_fontsize: Schriftgröße für die Labels.
    :param label_weight: Schriftstärke für die Labels.
    :param labels: Optional. Dictionary, das Indizes (als Schlüssel) und Textlabels (als Werte) enthält.
    """
    # Überprüfung der Eingabeparameter
    if not isinstance(data, np.ndarray):
        raise ValueError("Parameter 'data' muss ein NumPy-Array sein.")
    if labels is not None and not isinstance(labels, dict):
        raise ValueError("Parameter 'labels' muss ein Dictionary sein.")
    if not (isinstance(grid_size, tuple) and len(grid_size) == 2 and all(isinstance(x, int) for x in grid_size)):
        raise ValueError("Parameter 'grid_size' muss ein Tupel mit zwei ganzen Zahlen sein, z.B. (20, 20).")
    if not (isinstance(label_fontsize, (int, float)) and label_fontsize > 0):
        raise ValueError("Parameter 'label_fontsize' muss eine positive Zahl sein.")
    if not isinstance(label_weight, str):
        raise ValueError("Parameter 'label_weight' muss ein String sein.")

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Versteckt die Achsen, wenn show_axes False ist
    if not show_axes:
        ax.axis('off')

    # Berechnet den Radius eines Sechsecks basierend auf der Gittergröße
    radius = 1 / np.sqrt(grid_size[0]**2 + grid_size[1]**2)

    # Erstellt jedes Sechseck und fügt Labels hinzu
    for row in range(grid_size[0]):
        for col in range(grid_size[1]):
            x = col * 1.5 * radius
            y = row * np.sqrt(3) * radius + (col % 2) * radius * np.sqrt(3) / 2
            index = row * grid_size[1] + col

            hexagon = mpatches.RegularPolygon((x, y), numVertices=6, radius=radius, 
                                               orientation=np.radians(30),
                                               facecolor=plt.cm.get_cmap(colormap)(data[index]),
                                               edgecolor='k')
            ax.add_patch(hexagon)

            # Fügt das Label hinzu, wenn vorhanden und gültig
            if labels and index in labels:
                ax.text(x, y, labels[index], ha='center', va='center', fontsize=label_fontsize, fontweight=label_weight)

    # Fügt einen Titel hinzu, wenn einer angegeben ist
    if title:
        plt.title(title)

    ax.autoscale_view()
    plt.colorbar(plt.cm.ScalarMappable(cmap=colormap), ax=ax)
    plt.show()

