import mne
from mnelab.io.xdf import read_raw_xdf
import pyxdf

from src.config import dir_rawdata, dir_figures

# find all avaliable datasets
datasets = list(dir_rawdata.glob("*.xdf"))

for dataset in datasets:

    # extract id from filename
    tmp_id = str(dataset).split(".")[0].split("\\")[-1]

    # Identify stream containing EEG channels
    streams = pyxdf.resolve_streams(dataset) # raw_fname is an .xdf file
    stream_id = pyxdf.match_streaminfos(streams, [{"type": "EEG"}])

    # Read in data
    raw = read_raw_xdf(dataset, stream_ids = stream_id)

    # set channel types 64*eeg, 9*behavioral
    # create a mapping dict, the first 65 channel names from raw should be eeg, the rest behavioral
    ch_type_map = dict(zip(raw.ch_names, ['eeg']*64 + ['misc']*9))
    # Add montage
    raw.set_channel_types(ch_type_map)
    raw.set_montage('standard_1020')

    # set the average reference
    raw = raw.set_eeg_reference()

    # filter the data
    raw = raw.filter(0.5, 35, verbose=False)

    # plot spectorgram per channel
    fig = raw.compute_psd(fmin=0, fmax=35).plot()

    # save plot
    fig.savefig(dir_figures.joinpath(f"rawSpectorgram_{tmp_id}.png"))