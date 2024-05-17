"""
===========
Config file
===========

"""

import matplotlib as mpl
import os
from socket import getfqdn
from pathlib import Path


def define_dir(root, *names):
    """define_dir create path handle and creates dir if not existend.

    Args:
        root (str): root to directory of interest
        names (tuple): subdirectories as separate arguments

    Returns:
        pathlib.Path: Pathlib handle of dir
    """
    path = root
    for name in names:
        path = Path.joinpath(path, name)
    Path.mkdir(path, parents=True, exist_ok=True)
    return path


###############################################################################
# Determine which user is running the scripts on which machine and set the path
# where the data is stored and how many CPU cores to use.

# If the user is not known, assume that the project is in the current working directory
dir_proj = Path.cwd().parent


###############################################################################
# These are relevant directories which are used in the analysis.

# (import) helper functions
dir_rawdata = Path.joinpath(dir_proj, "data", "raw")
dir_prep_erp = Path.joinpath(dir_proj, "data", "prep")
dir_figures = define_dir(dir_proj, "figures")
dir_src = Path.joinpath(dir_proj, "src")


###############################################################################
# These are all the relevant colors settings for the analysis
cfg_colors = {'blue': '#006685', 'tblue': '#3FA5C4', 'red': '#BF003F', 'tred': '#E84653', 'yellow': '#FFE48D'}

###############################################################################
# Set size for figure text
cfg_ax_font = 16
cfg_title_font = 22
cfg_label_font = 18
cfg_legend_font = 16

###############################################################################
# Set standard font to use
#cfg_font = "Open Sans"

def set_style(font_size: int = 24):
    """
    Just some basic things I do before plotting.
    """
    mpl.rcParams['font.family'] = 'sans-serif'
    mpl.rcParams['font.size'] = font_size
    mpl.rcParams.update({'font.size': cfg_title_font})
    mpl.rcParams.update({'axes.labelsize': cfg_ax_font})
    mpl.rcParams.update({'legend.fontsize': cfg_legend_font})
    mpl.rcParams.update({'xtick.labelsize': cfg_label_font})
    mpl.rcParams.update({'ytick.labelsize': cfg_label_font})
    mpl.rcParams.update({'figure.autolayout': True})
    mpl.rcParams.update({'axes.spines.right': False})
    mpl.rcParams.update({'axes.spines.top': False})