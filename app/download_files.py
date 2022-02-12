#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 21:17:33 2022

@author: matsya
"""

import sys

sys.path.append('../src')


#from utility import parse_config
from get_data_util import download_dataset, download_model

sys.path.append('../app')


##%% setting config
#config_path = "../config/config.yaml"   
#config = parse_config(config_path)   # read config file


#%% downloading dataset & model

download_dataset()    # downloads data from gdrive (File size is larger than git limit)

download_model()
