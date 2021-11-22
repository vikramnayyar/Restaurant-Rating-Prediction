# Restaurant-Rating-Prediction

## Introduction
An app is developed that predicts the rating of a Bangalore restaurant. This is based on six user inputs. The app was trained using <b>sklearn</b> models and 
is developed in <b>Streamlit</b>.


## Dataset
The dataset consists of actual information obtained from Zomato. This consists <b>51717</b> restaurants and <b>17</b> features. 

The dataset was acquired from Kaggle and was uploaded by Himanshu Poddar. Besides, a recently updated dataset can be obtained using web scraping.   

<b>Note:</b> The dataset is downloaded by running "get_data.py" script, therefore; the data is not provided is repository. Furthermore, the dataset can be easily downloaded from ___________________________________


## Problem Statement
In the past six years, over 1400 new eateries have been opened. Evidently, the population's willingness to visit restaurants; has phenomenally increased. Subsequently, numerous  restaurant categories have emerged at several locations. 
Furthermore, they offer several cuisines, price ranges and services and offers.   

Therefore, predicting the customer's liking is remarkably challenging. As; a large amount of finance and time is invested, evaluation of customer tendency is critical. To make the business successful the restaurant must attract customers.  


## Goal
This work was performed as a insternship project in iNeuron. The purpose of the product is to predict restaurant ratings. For a restaurant,  maintaining a good  rating is of chief importance. A highly rated restaurant consistently attracts large customers. This is essential to popularize the restaurant in town.    

A good customer evaluation; certainly lays a lasting platform for the restaurant’s profit.

## Technical Description
The main project scripts are in the "src" directory. Exceptionally, "app.py" is in app directory. The main constituting scripts are as follows

* **get_data.py:** This script downloads the data as **"restn_data.csv"** (The data is not present in the repository due to upload size restrictions of Github). NaNs are removed. Cleaned dataset is saved as **"cleaned_data.csv"**. Locations and restaurant type dictionaries are saved as **"locations_dict.pkl"** and **"rest_type_dict.pkl"**. These dictionaries are later used by Streamlit app.

* **data_analysis.py:** This script obtains various visualizations of the dataset. These visualizations are present in the **"Visualization"** directory. 

* **prepare_data.py:** The script converts the required features to **categorical** variables. Subsequent outliers are determined using Grubb's Test. These outliers are removed and cleaned dataset is saved as **"prepared_data.csv"**.   

* **split_data.py:** The cleaned dataset is split using stratified sampling. This ensures the fair splitting. Train data and test data are respectively saved as **"train_set.csv"** and **"test_set.csv"**. Labels are separated from train and test sets and saved as **"train_labels.csv"** and **"test_labels.csv"**.

* **model_data.py:** The train set is modelled using data science models. Accuracy of all the models is verified using test set. Henceforth, the best model is selected. The feature selection of the best model is optimized to increase the accuracy to_________. This model is saved as **"model.pkl"**. 

* **app.py:** The script develops a Streamlit app; that accepts six user inputs to predict the restaurant rating. 
 
* **run_project.py:** The script runs all the project scripts sequentially (including applcation). Therefore, entire project is executed with this script.  

**get_data_util.py**, **data_analysis_util.py**, **prepare_data_util.py**, **split_data_util.py**, **model_data_util.py** and **utility.py** delcare vital functions that are required by respective scripts.    

## Directory Structure

```bash
├── app                              # Application files
|  ├── app.py                        # Application script
├── config                           # Configuration files
|  ├── config.yaml                   # Configuration file  
├── data                             # Data files ()   
|  ├── restnt_data.csv               # Original dataset 
|  ├── clean_data.csv                # Cleaned dataset 
|  ├── prepared_data.csv             # Prepared dataset 
|  ├── train_set.csv                 # Train data
|  ├── test_set.csv                  # Test data
|  ├── train_label.csv               # Train labels
|  ├── test_set.csv                  # Test labels
├── dict                             # Dictionary Files
|  ├── locations_dict.pkl            # Locations dictionary
|  ├── rest_type_dict.pkl            # Resaturant type dictionary
├── doc                              # Documentation Files
|  ├── HDL.pdf                       # High-Level Design document
|  ├── LLD.pdf                       # Low-Level Design document
|  ├── project_report.pdf            # Detailed Project Report 
├── log                              # Log files
|  ├── get_data.log                  # "get_data.py" script logs
|  ├── data_analysis.log             # "data_analysis.py" script logs
|  ├── prepare_data.log              # "prepare_data.py" script logs 
|  ├── split_data.log                # "split_data.py" script logs 
|  ├── model_data.log                # "model_data.py" script logs 
├── model                            # Model Files
|  ├── model.pkl                     # Saved model
├── src                              # Main project scripts 
|  ├── get_data.log                  # Dataset acquistion and cleaning script
|  ├── data_analysis.log             # Dataset analysis and visualization script
|  ├── prepare_data.log              # Dataset preperation script
|  ├── split_data.log                # Dataset splitting script  
|  ├── model_data.log                # Dataset modelling script
├── visualizations                   # Dataset visualizations
|  ├── book_table_vs_rating.png      # Bookings vs ratings figure
|  ├── cities_vs_rating.png          # Cities vs ratings figure
|  ├── correlation_heatmap.png       # Feature correlations figure
|  ├── cuisines_vs_rating.png        # Cuisines vs rating figure 
|  ├── feature_importances.png       # Best model feature importance figure
|  ├── online_order_vs_rating.png    # Online oreder vs rating figure
|  ├── rest_type_vs_rating           # Rest-type vs rating figure 
|  ├── top_cuisines.png              # Top cuisines figure
├── requirements.txt                 # Required libraries
```
**Note :** Data and Model directories are empty due to Github upload size restriction. These directories fill up by running corresponding scripts. This is already explained in Technical Description section. The project directory structure is given as follows  

## Installing Dependencies
Foremost running the project, installing the dependencies is essential. 
* Ensure Python 3.8.8 or later is installed in the system. 
* All required libraries are listed in "requirements.txt". These are easily installed; by running the following command in project directory
```bash
pip install -r requirements.txt
```

## Run Project
As discussed in **Technical Aspect** section, "src" directory possess the main scripts. 

Running the following command in the "src" directory executes the entire project  
```bash
python3 run_project.py
```
Alternatively, "src" and “app” directory  contain the main project scripts. They can be individually executed using the general script given as
```bash
python3 script.py
```
Here “script.py” is any python script. 
