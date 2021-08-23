from ...core.common.environment import is_jupyter
from ...logger import logging_widget
import ipywidgets as widgets

if is_jupyter:
    # third party
    from IPython.core.display import Image
    from IPython.core.display import display

def process_widget():
    display(logging_widget)