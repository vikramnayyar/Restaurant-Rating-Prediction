"""

The script converts the columns to categorical features 
& then remove the outliers


"""

import pandas as pd
from logzero import logger, logfile

from utility import create_log, parse_config, read_data
from prepare_data_util import convert_cat, cols_with_ouliers, grubbs_test


create_log("prepare_data.log")  # Creating log file

##################################################
#-----------------Reading Dataset-----------------
##################################################

config_path = "config/config.yaml"   
config = parse_config(config_path)   # read config file
data_path = config["prepare_data"]["data"]   # read dataset
df_clean = read_data(data_path)


################################################
#----------- Categorical Coversion--------------
################################################

# Dropping non-categorical columns 
df_clean = df_clean.drop(['cuisines'], axis = 1)   # previously, 'cuisines' was required for data analysis

# Converting columns to categorical data type
col_list = ['online_order', 'book_table', 'location', 'rest_type', 'type', 'city']
df_clean = convert_cat(df_clean, col_list)


################################################
#----------------Outlier Removal----------------
################################################

# Finding columns with outliers
cols_with_ouliers = cols_with_ouliers(df_clean)

# removing outliers from votes column
cut_off = 3300
for i in df_clean['votes']:
    if i >= cut_off:
        df_clean['votes'] = df_clean['votes'].replace(i, cut_off)

grubbs_test(df_clean['votes'])

# removing outliers from approx_cost column
cut_off = 2700
for i in df_clean['approx_cost']:
    if i >= cut_off:
        df_clean['approx_cost'] = df_clean['approx_cost'].replace(i, cut_off)

grubbs_test(df_clean['approx_cost'])

df_clean.to_csv("data/prepared_data.csv", index = False)   # Saving file