"""

Running this script alone executes the entire project. 
The script sequentially runs all the project scripts.

"""

import os
  
os.system('python get_data.py')
os.system('python data_analysis.py')
os.system('python prepare_data.py')
os.system('python split_data.py')
os.system('python model_data.py')
# os.system('python ../app/app.py')
print("---------------Project Successfully Executed ---------------")