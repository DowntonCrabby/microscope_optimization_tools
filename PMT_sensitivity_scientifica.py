from scipy.stats import linregress

import matplotlib.pyplot as plt
import configparser as configp #for parsing the ini file
from glob import glob
import pandas as pd
import numpy as np
import sys
import os

config = configparser.ConfigParser()

def get_raw_files(file_folder):
    raw_files = glob(os.path.join(file_folder, 
                              '*', # Wildcard = any sub-directory 
                              '*.raw')) # Wildcard.raw = any file ending in .raw
    return raw_files

def get_ini_files(file_folder):
    ini_files = glob(os.path.join(file_folder, 
                              '*', # Wildcard = any sub-directory 
                              '*.ini')) # Wildcard.ini = any file ending in .ini
    return ini_files



def read_ini_file(ini_filepath):
    config.read(ini_file_path)

def metadata_from_ini_file([list_of_keys]):
    metadata_df = pd.DataFrame()
    for key in list_of_keys:
        data = config['_'][key]
        metadata_df.loc[:,key] = data


def get_filename_timestamp():

def get_raw_data(raw_filepath):
    data = np.fromfile(os.path.join(dest,file), dtype=">u2")
    raw_df = pd.DataFrame({})
    raw_data_mean = int(np.mean(data))
    raw_data_std_dev = int(np.std(data))
    raw_data_var = int(np.var(data))



def get_pmt_gain_offset(dataframe):
    pmt_gain_df = dataframe.loc[dataframe["laser_power"]=="shuttered", ["frame_mean"]].copy






def calculate_pmt_slope(dataframe):
    dataframe["pmt_slope"] = linregress(dataframe["frame_mean"], dataframe["frame_var"])[0]
    return dataframe 


def calculate_mean_photons(dataframe):
    dataframe["mean_photons"] = (dataframe["frame_mean"] - dataframe["pmt_offset"])/ dataframe["pmt_slope"]
    return dataframe