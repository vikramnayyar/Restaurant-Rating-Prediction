# Restaurant-Rating-Prediction

## Introduction
An app is developed that predicts the rating of a Bangalore restaurant. This is based on six user inputs. The app was trained using <b>sklearn</b> models and 
is developed in <b>Streamlit</b>.


## Dataset
The dataset consists of actual information obtained from Zomato. This consists <b>51717</b> restaurants and <b>17</b> features. The dataset was uploaded by Himanshu Poddar in Kaggle. Besides, a recently updated dataset can be obtained using web scraping.   

<b>Note:</b> The dataset is downloaded by running command "dvc pull", therefore; the data is not provided in repository. Furthermore, the dataset can be easily downloaded from https://drive.google.com/file/d/1D-0gn9kJObWDnHXy9_NwI1Us8zCfFlwt/view?usp=sharing


## Problem Statement
In the past six years, over 1400 new eateries have been opened. Evidently, the population's willingness to visit restaurants; has phenomenally increased. Subsequently, numerous  restaurant categories have emerged at several locations. 
Furthermore, they offer several cuisines, price ranges and services and offers.   

Therefore, predicting the customer's liking is remarkably challenging. As; a large amount of finance and time is invested, evaluation of customer tendency is critical. To make the business successful the restaurant must attract customers.  


## Goal
The purpose of the project is to predict restaurant ratings. For a restaurant,  maintaining a good  rating is of chief importance. A highly rated restaurant consistently attracts large customers. This is essential to popularize the restaurant in town.    

A good customer evaluation; certainly lays a lasting platform for the restaurant’s profit.


## System Environment
![](https://forthebadge.com/images/badges/made-with-python.svg)



[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" width=200>](https://pandas.pydata.org/)     [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/512px-NumPy_logo_2020.svg.png" width=200>](https://numpy.org/)     [<img target="_blank" src="https://www.fullstackpython.com/img/logos/scipy.png" width=200>](https://www.scipy.org/)                    



[<img target="_blank" src="https://www.metachris.com/images/posts/logzero/logo-text-wide-cropped.png" width=200>](https://pypi.org/project/logzero/)     [<img target="_blank" src="https://user-images.githubusercontent.com/965439/27257445-8791ea14-539c-11e7-8f5a-eec6cdfababa.png" width=200>](https://pypi.org/project/PyYAML/)     [<img target="_blank" src="https://phyblas.hinaboshi.com/rup/nayuki/2020/pythonsubprocess.png" width=200>](https://docs.python.org/3/library/subprocess.html)



[<img target="_blank" src="https://matplotlib.org/_static/logo2_compressed.svg" width=200>](https://matplotlib.org)     [<img target="_blank" src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" width=200>](https://seaborn.pydata.org/)     [<img target="_blank" src="https://plotly-marketing-website.cdn.prismic.io/plotly-marketing-website/948b6663-9429-4bd6-a4cc-cb33231d4532_logo-plotly.svg" width=200>](https://plotly.com/)        



[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width=200>](https://scikit-learn.org)     [<img target="_blank" src="https://miro.medium.com/max/720/1*yhE3CBwTrlXcAIvNJNTQiA.png" width=200>](https://github.com/dmlc/xgboost)     [<img target="_blank" src="https://lightgbm.readthedocs.io/en/latest/_images/LightGBM_logo_black_text.svg" width=200>](https://lightgbm.readthedocs.io/en/latest/)     [<img target="_blank" src="https://landscape.lfai.foundation/logos/cat-boost.svg" width=200>](https://catboost.ai/)    


[<img target="_blank" src="https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png" width=150>](https://www.docker.com/)     [<img target="_blank" src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" width=200>](https://streamlit.io/)     [<img target="_blank" src="https://repository-images.githubusercontent.com/83878269/a5c64400-8fdd-11ea-9851-ec57bc168db5" width=200>](https://dvc.org/)     




## Technical Description
The main project scripts are in the "src" directory. Exceptionally, "app.py" is in app directory. The main constituting scripts are as follows

* **get_data.py:** This script downloads the data as **"restn_data.csv"** (The data is not present in the repository due to upload size restrictions of Github). NaNs are removed. Cleaned dataset is saved as **"cleaned_data.csv"**. Locations and restaurant type dictionaries are saved as **"locations_dict.pkl"** and **"rest_type_dict.pkl"**. These dictionaries are later used by Streamlit app.

* **data_analysis.py:** This script obtains various visualizations of the dataset. These visualizations are present in the **"Visualization"** directory. 

* **prepare_data.py:** The script converts the required features to **categorical** variables. Subsequent outliers are determined using Grubb's Test. These outliers are removed and cleaned dataset is saved as **"prepared_data.csv"**.   

* **split_data.py:** The cleaned dataset is split using stratified sampling. This ensures the fair splitting. Train data and test data are respectively saved as **"train_set.csv"** and **"test_set.csv"**. Labels are separated from train and test sets and saved as **"train_labels.csv"** and **"test_labels.csv"**.

* **model_data.py:** The train set is modelled using data science models. Accuracy of all the models is verified using test set. Henceforth, the best model is selected. The feature selection of the best model is optimized to increase the accuracy to **91.7%**. This model is saved as **"model.pkl"**. 

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
|  ├── restnt_data.csv.dvc           # Tracking File of Original dataset (DVC)  
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
|  ├── model.pkl                     # Saved model (This file is not present in Github, it is created by running project) 
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
├── dvc.yaml                         # DVC pipelines
├── Dockerfile                       # Docker file for generating containers
├── requirements.txt                 # Required libraries
├── LICENSE                          # License
├── README.md                        # About repository
```
**Note :** Data and Model directories are empty due to Github upload size restriction. These directories fill up by running corresponding scripts. This is already explained in Technical Description section.  

## Prerequisites
### * Installing Dependencies
Foremost running the project, installing the dependencies is essential. 
* Ensure Python 3.8.8 or later is installed in the system. 
* All required libraries are listed in "requirements.txt". These are easily installed; by running the following command in project directory
```bash
pip install -r requirements.txt
```
### * Download Dataset
Running the following command main project directory; downloads the dataset  
```bash
dvc pull
```
The terminal/command prompt asks for the authentication. After gdrive authentication, the dataset downloads in **data** directory.   

**Optional Step:** 
Alternatively, user can download the data from gdrive link https://drive.google.com/file/d/1D-0gn9kJObWDnHXy9_NwI1Us8zCfFlwt/view?usp=sharing, and store in data directory of project. (Due to large size of dataset gdrive as well as Kaggle do not allow data to be downloaded using python scripts. Besides, GitHub has storage restrictions).  User is also recommended to avoid renaming the downloaded dataset. Dataset is required to be copied to **data** directory.


## Run Project
As discussed in **Technical Aspect** section, "src" and “app” directory possess the main scripts. 

Running the following command in **main project directory** executes the entire project  
```bash
python3 src/run_project.py
```
Alternatively, any main project scripts can be individually executed using the general script given as
```bash
python3 src/script.py
```
Here “script.py” represents any python script. 

Application executes by running following command in **main project directory**
```bash
streamlit run app/app.py
```

**NOTE**: All scripts (including application) run from main project directory.  
