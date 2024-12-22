# Type hinting
from typing import Union

# Visualization
import plotly.graph_objects as go
from IPython.display import display
import kaleido
import webp

# Configuration
from utils.config import format, PLOTS, INTERACTIVE

if kaleido.__version__ != '0.1.0.post1':
    # pip install kaleido==0.1.0post1
    # Restart kernel
    print('Kaleido version may not work properly. Version 0.1.0.post1 is supported')


def title_to_filename(title: str, save_dir: str = PLOTS):
    replace_dict = {',': '_', '!': '_', '?': '_', ' ': '_', ':': '_'}
    # Create a translation table
    translation_table = str.maketrans(replace_dict)
    filename = save_dir + title.translate(translation_table) + '.' + format
    return filename


def show_plot(fig: Union[None, go.Figure] = None, save_only: bool = False, display_only: bool = False, save_dir: str = PLOTS, interactive: bool = INTERACTIVE) -> Union[None, str]:
    '''
    Display a plot from either a saved image file or an interactive figure. All figures need a title to be able to create a filename

    Parameters:
    fig (Union[None, go.Figure]): The Plotly Figure object to display interactively. Default is None.
    save_only (bool): True saves the fig but do not render to display.
    display_only (bool): True displays or renders the fig from the saved plots and do not attempt to save it.
    save_dir (str): Directory to save plots, defaults to PLOTS constant.
    interactive (bool): True displays and interactive plot without saving, defaults to INTERACTIVE constant. 

    Returns:
    Union[None, str]: Returns None if in interactive mode and the displayed image if in non-interactive mode.
    '''
    if fig is None:  # If fig is provided, display interactive figure
        return print('Pass in a plotly figure as argument')
    else:
        if interactive:  # Check if in interactive mode
            return fig.show()
        elif save_only:  # Save fig, no display
            filename = title_to_filename(fig.layout.title.text, save_dir)
            fig.write_image(filename, format=format,
                            engine='kaleido', width='1280', scale=2)
            return filename
        elif display_only:  # Load fig from saved plots folder, no writing to save
            filename = title_to_filename(fig.layout.title.text, save_dir)
            img = webp.load_image(f'{filename}')  # Load image file
            return display(img)  # Display the image
        else:  # Save and Display
            filename = title_to_filename(fig.layout.title.text, save_dir)
            fig.write_image(filename, format=format,
                            engine='kaleido', width='1280', scale=2)
            img = webp.load_image(f'{filename}')  # Load image file
            return display(img)  # Display the image
