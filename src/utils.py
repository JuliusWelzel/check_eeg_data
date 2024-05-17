import mne
import pandas as pd
from pathlib import Path

from src.config import dir_rawdata

def load_bv_montage():
    """Load the BrainVision montage.

    This function finds all available datasets with the pattern "*eo*.vhdr" and loads the first dataset using the 
    `mne.io.read_raw_brainvision` function. It then retrieves the montage from the loaded dataset and returns it.

    Returns:
        The BrainVision montage for MNE.
    """
    # find all available datasets
    datasets = list(dir_rawdata.glob("*eo*.vhdr"))

    # load the first dataset
    raw = mne.io.read_raw_brainvision(datasets[0], preload=True)

    # save montage
    montage = raw.get_montage()

    return montage