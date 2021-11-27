"""

The script declares functions used in 'data_analysis.py'

"""

import os

import yaml
from logzero import logger

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Patch
import plotly.graph_objects as go

from utility import parse_config




config_path = "../config/config.yaml"   
config = parse_config(config_path)   # read config file



def box_plot(df_clean, col, plot_type):
    sorted_cities = df_clean.groupby([col])['rate'].median().sort_values()  # Grouping dataframe city-wise 
    fig, ax = plt.subplots(figsize = (20,10))
    # sns.set_style("whitegrid")
    sns.boxplot(x=df_clean[col], y = df_clean['rate'], order=list(sorted_cities.index), palette = 'crest')
    
    plt.title(config["data_analysis"][plot_type]["title"], size = 18, y=1.08) 
    plt.xlabel(config["data_analysis"][plot_type]["xlabel"], size = 14)
    plt.ylabel(config["data_analysis"][plot_type]["ylabel"], size = 14) 
    plt.xticks( rotation = 90)
    
    plt.savefig(plot_type)  # saving figure
    # os.chdir('../src')



def hist_plot(df_clean, col, plot_type):
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    fig.suptitle(config["data_analysis"][plot_type]["title"], size = 16)
    
    # Subplot 1
    ax[0].hist(df_clean[df_clean[col]=='Yes']["rate"], bins=15, alpha=0.5, color="green", label="Available")
    ax[0].hist(df_clean[df_clean[col]=='No']["rate"], bins=15, alpha=0.5, color="blue", label="Not-Available")
    
    ax[0].set_xlabel(config["data_analysis"][plot_type]["xlabel"], fontsize=14)
    ax[0].set_ylabel(config["data_analysis"][plot_type]["ylabel"], fontsize=14)
    ax[0].legend(fontsize = 11);
    
    # Subplot 2
    sns.boxplot(x="rate", y="online_order", data=df_clean, orient="h", palette={ 'Yes':"#80e880", 'No':"#2626ff"}, ax = ax[1])
    ax[1].get_yaxis().set_visible(False)
    ax[1].set_xlabel(config["data_analysis"][plot_type]["xlabel"], fontsize=14)
    
    color_patches = [
        Patch(facecolor="#80e880", label="Available"),
        Patch(facecolor="#2626ff", label="Not Available")
    ]
    ax[1].legend(handles=color_patches, fontsize=11);
    plt.savefig(plot_type)  # saving figure



def find_duplicates(df_1, col):
    # Reseting index and removing double space 
    df_1 = df_1.reset_index(drop = True)   
    df_1[col]= df_1[col].str.replace(' ', '')
    
    # Identifying values with duplicate values
    duplicate_val = df_1.duplicated(subset = [col])
    all_duplicates = []
    all_duplicates = df_1.loc[duplicate_val][col]
    logger.info("Duplication is in following cuisines: \n{}".format(all_duplicates))
    
    return all_duplicates



def remove_duplicates(df_2, duplicates):
    
    # Identifying indices of dulplicate cuisines
    duplicate_indices = []
    duplicate_bool = []
    count = 0
    for index, cuisine in enumerate(duplicates):
        duplicate_bool = df_2['cuisine'].str.find(cuisine)
    
        for index, value in enumerate(duplicate_bool):
            if value == 0:
                duplicate_indices.append(index)
                
    
    # Removing duplicate indices and updating attributes
    
    i = 0
    for index in duplicate_indices:
        
        if (i) % 2 == 0:
            count = 0
            # Updating attributes in first duplicate index (or Original Index)
            total_restnt_1 = (df_2['Total Restaurants'][index])
            avg_rating_1 = df_2['rate'][index]
        
        else:
            count = 2
            total_restnt_2 = (df_2['Total Restaurants'][index])
            avg_rating_2 = df_2['rate'][index]
        
        i += 1
        if count == 2:
            df_2['Total Restaurants'][(index-1)] = (total_restnt_1 + total_restnt_2)
            df_2['rate'][(index-1)] = ((total_restnt_1*avg_rating_1) + (total_restnt_2*avg_rating_2))/(total_restnt_1 + total_restnt_2)
            
            # Removing second duplicate index
            df_2 = df_2.drop(index)
    
    return df_2


def bar_plot(df_3, col_1, col_2, plot_type):
    fig = go.Figure(data=[
    go.Bar(name = config["data_analysis"][plot_type]["ylabel"], # 
            x=df_3[col_1], 
            y=df_3[col_2])
    ])

    fig.update_traces(marker_color ='rgb(12, 128, 128)', opacity=1)
    fig.update_layout(xaxis_title = config["data_analysis"][plot_type]["xlabel"], 
                      yaxis_title = col_2, 
                      title_text=config["data_analysis"][plot_type]["title"], 
                      title_x=0.5,
                      font=dict(
                          family="Courier New, monospace",
                          size=12,
                          color='rgb(12, 128, 128)'
                      ))
    
    fig.write_image('top_cuisines.png')  # saving file
    
    
    
def polar_plot(df_4, col_1, col_2, plot_type):
    labels = df_4[col_1]
    x1 = df_4[col_2]
    num_slices = len(x1)
    theta = [(i+1.5)*360/num_slices for i in range(num_slices)]
    r=x1
    width = [360 / num_slices for _ in range(num_slices)]
    
    barpolar_plots = [go.Barpolar(r=[r], theta=[t], width=[w], name=n)
    for r, t, w, n in zip(r, theta, width, labels)]
    
    fig = go.Figure(barpolar_plots)
    
    fig.update_layout(
                        polar = dict(
                            radialaxis = dict(range=[3.8, 4.15], showticklabels=True),
                            angularaxis = dict(showticklabels=False, ticks='')
                            ),
                        # yaxis_title = 'States', xaxis_title = 'Total Restaurants', 
                        title_text = config["data_analysis"][plot_type]["title"], 
                        title_x=0.46,
                        font=dict(
                          family="Courier New, monospace",
                          size=12,
                      )
    )
    
    fig.write_image('cuisines_vs_rating.png')  # saving file
