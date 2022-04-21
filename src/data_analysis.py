"""

The script obtains various visualizations of the cleaned dataset 
& stores them in "visualization" directory

"""
import os
import pathlib
import pandas as pd

from utility import create_log, parse_config, read_data
from data_analysis_util import box_plot, hist_plot, bar_plot, polar_plot, find_duplicates, remove_duplicates

create_log("data_analysis.log")  # Creating log file

##################################################
#-----------------Reading Dataset-----------------
##################################################

config_path = "config/config.yaml"   
config = parse_config(config_path)   # read config file
data_path = config["data_analysis"]["data"]   # read dataset
df_clean = read_data(data_path)

df_clean['rate'] = pd.to_numeric(df_clean['rate'], downcast = 'float') # Converting ratings to float

os.chdir('visualizations')  # directory to save visualization figures

##################################################
#------------- 1. Cities vs Rating ---------------
##################################################

box_plot(df_clean, "city", "city_vs_rating")



##################################################
#--------- 2. Restaurant Type vs Rating ----------
##################################################

box_plot(df_clean, "type", "type_vs_rating")



##################################################
#----------- 3. Online Order vs Rating -----------
##################################################

hist_plot(df_clean, "online_order", "online_vs_rating")


##################################################
#------------ 4. Book Table vs Rating ------------
################################################## 

hist_plot(df_clean, "book_table", "book_vs_rating")


##################################################
#----------- 5. Top Cuisines vs Rating -----------
################################################## 

cuisines = df_clean['cuisines'].str.split(',').explode().unique().tolist()  # reading cuisines


# Forming cuisine dataframe
def form_cuisine_df(df_clean):
    data = []
    df_filtered = pd.DataFrame()
    columns = ['cuisine', 'Total Restaurants', 'rate']
    df_cuisine = pd.DataFrame(columns = columns)
    
    for cuisine in cuisines:
        
        df_clean['Cuisine Verification'] = df_clean['cuisines'].str.contains(cuisine, case=False, na=False).astype(int)
        df_filtered = df_clean[df_clean['Cuisine Verification'] == 1]
        total_restnt = len(df_filtered.index) + 1   # Compensates for 0 length 
        df = df_clean.drop(['Cuisine Verification'], axis=1)
        
        avg_rating = df_filtered['rate'].sum()/total_restnt
        df_cuisine = df_cuisine.append({'cuisine': cuisine, 'Total Restaurants': total_restnt, 'rate':avg_rating, }, ignore_index=True)
    
    return df_cuisine

df_cuisine = form_cuisine_df(df_clean)


# Cleaning cusines dataframe
duplicate_cuisines = find_duplicates(df_cuisine, "cuisine") # Finding Duplicates
df_cuisine = remove_duplicates(df_cuisine, duplicate_cuisines) # Removing Duplicates
    

# Filtering & plotting top cuisines
df_cuisine = df_cuisine[df_cuisine['Total Restaurants'] > 900] # Taking cuisines that are atleast served in over 900 restaurants 
bar_plot(df_cuisine, "cuisine", "Total Restaurants", "top_cuisines")


###############################################
#------------ 6. Cuisines vs Rating -----------
###############################################

df_cuisine_filtered = df_cuisine[df_cuisine['rate'] > 3.9]  # Filtering cuisines


polar_plot(df_cuisine_filtered, "cuisine", "rate", "cuisines_vs_rating")


os.chdir('..')  # resetting to main project dir 
# cwd = os.getcwd()    # for validating os.chdir('..')
# print(cwd)
