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


def get_filename(file_path):
    filename = os.path.split(file_path)[-1]
    return filename


def get_file_timestamp(file_path):
    filename = get_filename(file_path)
    timestamp = filename[:17]
    return timestamp


def check_if_shuttered(file_path):
    filename = get_filename(file_path)
    shuttered = "shuttered" in filename
    return shuttered

def read_ini_file(ini_filepath):
    config.read(ini_file_path)


def metadata_from_ini_file(list_of_keys):
    metadata_df = pd.DataFrame()
    for key in list_of_keys:
        data = config['_'][key]
        metadata_df= metadata_df.loc[:,key] = data


def load_rawdata(raw_filepath):
    data = np.fromfile(raw_filepath, dtype=">u2")
    return data

def gen_single_rawfile_df(raw_filepath):
    data = load_rawdata(raw_filepath)
    
    timestamp = get_file_timestamp(raw_filepath)
    shuttered = check_if_shuttered(raw_filepath)

    raw_data_mean = int(np.mean(data))
    raw_data_std_dev = int(np.std(data))
    raw_data_var = int(np.var(data))
    
    raw_df = pd.DataFrame({"timestamp":timestamp,
                            "shuttered":shuttered,
                            "frame_mean": raw_data_mean, 
                            "frame_std": raw_data_std_dev, 
                            "frame_var": raw_data_var}, 
                            index =[0])
    return raw_df

def gen_multi_rawfile_df(list_of_filepaths):
    multi_rawfile_df = pd.DataFrame()
    for rawfile in list_of_filepaths:
        single_df = gen_single_rawfile_df(rawfile)
        multi_rawfile_df.append(single_df)
    multi_rawfile_df = multi_rawfile_df.reset_index(drop=True)
    return multi_rawfile_df


def gen_raw_data_df()
    



def get_pmt_gain_offset(dataframe):
    pmt_gain_df = dataframe.loc[dataframe["laser_power"]=="shuttered", ["pmt_gain","frame_mean"]].copy





def calculate_pmt_slope(dataframe):
    dataframe["pmt_slope"] = linregress(dataframe["frame_mean"], dataframe["frame_var"])[0]
    return dataframe 


def calculate_mean_photons(dataframe):
    dataframe["mean_photons"] = (dataframe["frame_mean"] - dataframe["pmt_offset"])/ dataframe["pmt_slope"]
    return dataframe