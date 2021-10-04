dtr.fit(dtr, [x_train],[y_train])
dtr.fit(dtr, [x_train], [y_train])
d_model = dtr(criterion='poisson')
dtr.fit( [x_train],[y_train])
d_model.fit(x_train, ytrain)
d_model.fit(x_train, y_train)
pred = d_model.predict(x_test)
print(regression_report(pred,y_test))
from sklearn.metrics import Regressor_report
from sklearn.metrics import Regression_report
dir(sklearn.metrics)
d_model.score(pred, y_test)
pred = pred.reshape(-1,1)
pred = pred.reshape(1,-1)
y_test = y_test.reshape(1,-1)
d_model.score(pred, y_test)
pred.reshape(-1,1)
pred =pred.reshape(-1,1)
d_model.score(pred, y_test)
# importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor


# Fit regression model
regr_1 = DecisionTreeRegressor(max_depth=4)

regr_2 = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4),
                          n_estimators=300, random_state=rng)
# importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor


# Fit regression model
regr_1 = DecisionTreeRegressor(max_depth=4)

regr_2 = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4),
                          n_estimators=300, random_state=0)
regr_1.fit(x_train, y_train)
regr_2.fit(x_train, y_train)
# Predict
y_1 = regr_1.predict(x_test)
y_2 = regr_2.predict(x_test)

# Plot the results
plt.figure()
plt.scatter(x_train, y, c="k", label="training samples")
plt.plot(x_test, y_1, c="g", label="n_estimators=1", linewidth=2)
plt.plot(x_test, y_2, c="r", label="n_estimators=300", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Boosted Decision Tree Regression")
plt.legend()
plt.show()
# Predict
y_1 = regr_1.predict(x_test)
y_2 = regr_2.predict(x_test)

# Plot the results
plt.figure()
plt.scatter(x_train, y_train, c="k", label="training samples")
plt.plot(x_test, y_1, c="g", label="n_estimators=1", linewidth=2)
plt.plot(x_test, y_2, c="r", label="n_estimators=300", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Boosted Decision Tree Regression")
plt.legend()
plt.show()
# Predict
y_1 = regr_1.predict(x_test)
y_2 = regr_2.predict(x_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_1))
prediction = pd.DataFrame(columns=['Ytest','y_regress','y_adaboost','resid'])
prediction['Ytest'] = y_test
prediction['y_regress'] = y_1
prediction['y_adaboost'] = y_2
prediction['resid'] = prediction['Ytest'] - prediction['y_regress']
import seaborn as sns
sns.scatterplot(x='Ytest', y='y_regress', hue='resid',data = prediction)
sns.scatterplot(x='x_test', y='y_regress', hue='resid',data = prediction)
sns.scatterplot(x='Ytest', y='y_adaboost', hue='resid',data = prediction)
sns.scatterplot(x='Ytest', y='y_adaboost', hue='resid',data = prediction,palette='crest')
sns.scatterplot(x='Ytest', y='y_adaboost', hue='resid',data = prediction,palette='burst')
dir(sns.palette)
sns.color_palette
sns.color_palette()
dir(sns.color_palette)
dir(sns.color_palette())
sns.scatterplot(x='Ytest', y='y_adaboost', hue='resid',data = prediction,palette='magma')
sns.scatterplot(x='Ytest', y='y_adaboost', hue='resid',data = prediction,palette='viridis_r')
sns.scatterplot(x='Ytest', y='y_adaboost', hue='resid',data = prediction,palette='viridis')
sns.scatterplot(x='Ytest', y='y_adaboost', hue='resid',data = prediction,palette='plasma')
sns.scatterplot(x='Ytest', y='y_adaboost', hue='resid',data = prediction,palette='rocket')
sns.scatterplot(x='Ytest', y='y_adaboost', hue='resid',data = prediction,palette='YlGnBu')
data = pyb.statcast('2021-09-01')
data = pyb.statcast('2021-09-01','2021-09-07')
runcell(0, 'D:/Python/Sklearn_pitch_MLprediction.py')
import requests

url = "https://smsapi-com3.p.rapidapi.com/sms.do"

querystring = {"access_token":"undefined"}

headers = {
    'x-rapidapi-host': "smsapi-com3.p.rapidapi.com",
    'x-rapidapi-key': "b501e0bf75mshf881260fcf61406p1a7f13jsnbce859978dd1"
    }

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)
import requests

url = "https://realty-mole-property-api.p.rapidapi.com/saleListings"

querystring = {"bedrooms":"3","city":"Navarre","state":"FL"}

headers = {
    'x-rapidapi-host': "realty-mole-property-api.p.rapidapi.com",
    'x-rapidapi-key': "b501e0bf75mshf881260fcf61406p1a7f13jsnbce859978dd1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
x= response.text
import pandas as pd
pd.read_json(x)
df = pd.read_json(x)
runcell(0, 'D:/Python/AppScripts/RealEstateAPIReq.py')
from real_estate import rentals
runcell(0, 'D:/Python/AppScripts/RealEstateAPIReq.py')
listings('Navarre','FL')
runcell(0, 'D:/Python/AppScripts/RealEstateAPIReq.py')
globals()
runcell(0, 'D:/Python/AppScripts/RealEstateAPIReq.py')
listings('Denver','CO')
runcell(0, 'D:/Python/AppScripts/RealEstateAPIReq.py')
listings('Hollister','CA')
rentals('Destin','FL')
runcell(0, 'D:/Python/AppScripts/RealEstateAPIReq.py')
listings('Destin','FL')
import requests

url = "https://google-maps-geocoding.p.rapidapi.com/geocode/json"

querystring = {"address":"6232 E. Bay Blvd., Gulf Breeze, FL","language":"en"}

headers = {
    'x-rapidapi-host': "google-maps-geocoding.p.rapidapi.com",
    'x-rapidapi-key': "b501e0bf75mshf881260fcf61406p1a7f13jsnbce859978dd1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
pd.read_json(response.text)
geo = pd.read_json(response.text)
geo = pd.read_json(response.json)
geo[1]
geo[:,1]
geo[:1]
geo[0,0]
geo[0:0]
geo[0]
geo['results']
res = geo['results']
pd.DataFrame(res)
res =pd.DataFrame(res)
res[0].to_dict
res[0:].to_dict
res_dict = res[0:].to_dict
res_dict =pd.DataFrame(res_dict)
res_dict =pd.DataFrame(res_dict,index = [0])
res_dict =pd.DataFrame(data = res_dict ,index = [0])
res_dict = res[0:].to_dict
res_dict = res[0:].to_dict()
res_dict =pd.DataFrame(res_dict)
import requests

url = "https://odds.p.rapidapi.com/v1/odds"

querystring = {"sport":"baseball_mlb","region":"us","mkt":"h2h","dateFormat":"iso","oddsFormat":"american"}

headers = {
    'x-rapidapi-host': "odds.p.rapidapi.com",
    'x-rapidapi-key': "b501e0bf75mshf881260fcf61406p1a7f13jsnbce859978dd1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
import requests


url = "https://odds.p.rapidapi.com/v1/odds"

querystring = {"sport":"baseball_mlb","region":"us","mkt":"h2h","dateFormat":"iso","oddsFormat":"american"}

headers = {
    'x-rapidapi-host': "odds.p.rapidapi.com",
    'x-rapidapi-key': "b501e0bf75mshf881260fcf61406p1a7f13jsnbce859978dd1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
df['lastSeen'].split('-',3)
za = df['lastSeen']
import numpy as np
za = np.array(za)
za.split('-',3)
za = df['formattedAddress']
runcell(0, 'C:/Users/Robin/GIT/Website(baseball portfolio)/untitled5.py')
runcell(0, 'D:/Python/pybaseball_scripts/OTOT_LahmanSQLload.py')
print(data_[0])
pip install retrosheet
runcell(0, 'C:/Users/Robin/GIT/Website(baseball portfolio)/untitled5.py')
runcell(0, 'D:/Python/AppScripts/RealEstateAPIReq.py')
rentals('Gulf Breeze','FL')
list_df.to_csv("D:/Python/AppScripts/listings.csv")
rent_df.to_csv("D:/Python/AppScipts/rentals.csv')
rent_df.to_csv("D:/Python/AppScipts/rentals.csv")
rent_df.to_csv("D:/Python/AppScripts/rentals.csv")
import requests

url = "https://cis-automotive.p.rapidapi.com/salePrice"

querystring = {"brandName":"<REQUIRED>","regionName":"REGION_STATE_CA"}

headers = {
    'x-rapidapi-host': "cis-automotive.p.rapidapi.com",
    'x-rapidapi-key': "b501e0bf75mshf881260fcf61406p1a7f13jsnbce859978dd1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
import requests

url = "https://cis-automotive.p.rapidapi.com/salePrice"

querystring = {"brandName":"Nissan","regionName":"REGION_STATE_FL"}

headers = {
    'x-rapidapi-host': "cis-automotive.p.rapidapi.com",
    'x-rapidapi-key': "b501e0bf75mshf881260fcf61406p1a7f13jsnbce859978dd1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
data =response.text
data = data.to_dict
data = data.to_dict()
data = np.array(data)
data.to_dict
data=pd.DataFrame(data)
import requests

url = "https://cis-automotive.p.rapidapi.com/regionDailySales"
"2021-09-18","brandName":"Nissan","regionName":"REGION_STATE_FL"}

headers = {
    'x-rapidapi-host': "cis-automotive.p.rapidapi.com",
    'x-rapidapi-key': "b501e0bf75mshf881260fcf61406p1a7f13jsnbce859978dd1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
import requests

url = "https://cis-automotive.p.rapidapi.com/regionDailySales"
querystring"2021-09-18","brandName":"Nissan","regionName":"REGION_STATE_FL"}

headers = {
    'x-rapidapi-host': "cis-automotive.p.rapidapi.com",
    'x-rapidapi-key': "b501e0bf75mshf881260fcf61406p1a7f13jsnbce859978dd1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
import requests

url = "https://cis-automotive.p.rapidapi.com/regionDailySales"
querystring={"2021-09-18","brandName":"Nissan","regionName":"REGION_STATE_FL"}

headers = {
    'x-rapidapi-host': "cis-automotive.p.rapidapi.com",
    'x-rapidapi-key': "b501e0bf75mshf881260fcf61406p1a7f13jsnbce859978dd1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
import requests

url = "https://cis-automotive.p.rapidapi.com/regionDailySales"
querystring={'day':"2021-09-18","brandName":"Nissan","regionName":"REGION_STATE_FL"}

headers = {
    'x-rapidapi-host': "cis-automotive.p.rapidapi.com",
    'x-rapidapi-key': "b501e0bf75mshf881260fcf61406p1a7f13jsnbce859978dd1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
import requests

url = "https://cis-automotive.p.rapidapi.com/salePrice"

querystring = {"brandName":"Nissan","regionName":"REGION_STATE_FL"}

headers = {
    'x-rapidapi-host': "cis-automotive.p.rapidapi.com",
    'x-rapidapi-key': "b501e0bf75mshf881260fcf61406p1a7f13jsnbce859978dd1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
datafr = pd.DataFrame(response.text)
datafr = pd.DataFrame(response.text,index=[0])
get_namespace_view()
get_namespace_view
import this
import requests

url = "https://marketcheck-cars-search-v1.p.rapidapi.com/search"

headers = {
    'x-rapidapi-host': "marketcheck-cars-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "b501e0bf75mshf881260fcf61406p1a7f13jsnbce859978dd1"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
pip install pywebio
y = df.iterrows(0)
q = df.iterrows0)
q = df.iterrows()
print(q)
q()
q
dir(q)
q.gi_frame()
q.gi_frame
from pyb import statcast as sc
import pybaseball as pyb
from pyb import statcast as sc
from pybaseball import statcast as sc
s_c = sc('2021-09-12','2021-09-19','TOR')
runcell(0, 'D:/Python/pybaseball_scripts/OTOT_LahmanSQLload.py')

## ---(Tue Sep 21 02:25:06 2021)---
pyb.statcast()
runcell(0, 'C:/Users/Robin/GIT/Website(baseball portfolio)/untitled1.py')
print(PATH)
cwd
PATH
mkdir
dir
osdir
diros
cd
mkdir('"D:\downloadjunk")
cd
"D:\downloadjunk"
DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]

}
FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}
def organize_junk():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))

        for dir in os.scandir():
            try:
                os.rmdir(dir)
            except:
                pass
                
organize_junk()
runcell(0, 'D:/downloadjunk/orgjunk.py')
pip install streamlit
runcell(0, 'C:/Users/Robin/GIT/Website(baseball portfolio)/untitled7.py')
print(cyan + 'This color is Cyan')
print(yellow + 'This color is yellow')
print(blue + 'BLUE")
print(blue + 'BLUE')
print(red +'REDDDDDDDDDD')
print(green + 'GREEEEEEEEEEEEENNNNNNNNNNNNNN')
pip install termcolor
import sys
from termcolor import colored, cprint

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')
print(colored('This shit is cray','white', 'blue'))
print(colored('This shit is cray','white', 'red'))
print(colored('This shit is cray','white',on_color 'red'))
print(colored('This shit is cray','white',oncolor='red'))
print(colored('THIS SHIT BETTER WORK', 'yellow', 'on blue')
print(colored('THIS SHIT BETTER WORK', 'yellow', 'on blue'))
print(colored('THIS SHIT BETTER WORK', 'yellow', ='blue'))
print(colored('THIS SHIT BETTER WORK', 'yellow', on='blue'))
print(colored(text='THIS SHIT BETTER WORK', color='yellow', on_color='blue'))
print(colored(text='THIS SHIT BETTER WORK', color='yellow'))
print(colored(text='THIS SHIT BETTER WORK', color='blue'))
runcell(0, 'C:/Users/Robin/GIT/Website(baseball portfolio)/untitled7.py')
print(Fore.YELLOW + Back.BLUE + 'This is Yellow')
print(Fore.WHITE + Back.BLUE + 'This is Yellow')
print(Fore.WHITE + Back.CYAN + 'This is Yellow')
print(Fore.WHITE + Back.RED + 'This is Yellow')
stat = pyb.statcast('2021-09-10','2021-09-19')
stat.isna()
pyb.cache_enable()
pyb.cache.enable()
pyb.statcast('2021-09-10','2021-09-19')
pyb.cache.enable()
pyb.statcast('2021-09-10','2021-09-19')
pyb.cache.enable()
stats = pyb.statcast('2021-09-10','2021-09-19')
stats.dropna()
stats.dropna(axis=1)
stats = stats.dropna(axis=1)
sns.scatterplot(x ='launch_angle', y ='launch_speed','hue = estimated_woba_using_speedangle, data = stats, palette='crest_r')
sns.scatterplot(x ='launch_angle', y ='launch_speed','hue = estimated_woba_using_speedangle', data = stats, palette='crest_r')
sns.scatterplot(x ='launch_angle', y ='launch_speed',hue = 'estimated_woba_using_speedangle', data = stats, palette='crest_r')
sns.scatterplot(x =int('launch_angle)', y ='launch_speed',hue = 'estimated_woba_using_speedangle', data = stats, palette='crest_r')
sns.scatterplot(x =int('launch_angle'), y ='launch_speed',hue = 'estimated_woba_using_speedangle', data = stats, palette='crest_r')
sns.scatterplot(x =float('launch_angle'), y ='launch_speed',hue = 'estimated_woba_using_speedangle', data = stats, palette='crest_r')
sns.scatterplot(x =float('launch_angle'), y ='spin_rate_deprecated',hue = 'estimated_woba_using_speedangle', data = stats, palette='crest_r')
sns.scatterplot(x ='launch_angle', y ='spin_rate_deprecated',hue = 'estimated_woba_using_speedangle', data = stats, palette='crest_r')
sns.scatterplot(x = 'spin_rate_deprecated',y = 'effective_speed',hue = 'estimated_woba_using_speedangle', data = stats, palette='crest_r')
stats.columns
sns.scatterplot(x = 'release_spin_rate',y = 'effective_speed',hue = 'estimated_woba_using_speedangle', data = stats, palette='crest_r')
stats = pyb.statcast('2021-09-10','2021-09-19')
stats[stats['bb_type']!= 'nan']
stats[stats['event']!= 'None']
stats[stats['events']!= 'None']
stats[stats['events']!= None]
stats['events'].unique
stats['events'].unique()
it = ['field_out', 'single', 'hit_by_pitch', 'strikeout', 'double',
       'sac_bunt', 'force_out', 'walk', 'grounded_into_double_play',
       'caught_stealing_2b', 'other_out', 'home_run', 'field_error',
       'sac_fly', 'double_play', 'fielders_choice_out', 'fielders_choice',
       'triple', 'strikeout_double_play', 'stolen_base_2b', 'pickoff_2b',
       'catcher_interf']
stats[stats['events'] = it]
stats[stats['events'] ==it]
it = [['field_out', 'single', 'hit_by_pitch', 'strikeout', 'double',
       'sac_bunt', 'force_out', 'walk', 'grounded_into_double_play',
       'caught_stealing_2b', 'other_out', 'home_run', 'field_error',
       'sac_fly', 'double_play', 'fielders_choice_out', 'fielders_choice',
       'triple', 'strikeout_double_play', 'stolen_base_2b', 'pickoff_2b',
       'catcher_interf']]
stats[stats['events'] ==it]
stats['events'] ==it
stats['events'].dropna()
stats[stats['events'].dropna()]
stats[stats['events].notna()]
stats[stats['events'].notna()]
stats = stats[stats['events'].notna()]
sns.scatterplot(x = 'release_spin_rate',y = 'effective_speed',hue = 'estimated_woba_using_speedangle', data = stats, palette='crest_r')
sns.scatterplot(x ='launch_angle', y ='spin_rate_deprecated',hue = 'estimated_woba_using_speedangle', data = stats, palette='crest_r')
sns.scatterplot(x = 'release_spin_rate',y = 'effective_speed',hue = 'estimated_woba_using_speedangle', data = stats, palette='crest_r')
type(stats)
stats[stats['bb_type'].notna()]
stats = stats[stats['bb_type'].notna()]
sns.scatterplot(x ='launch_angle', y ='spin_rate_deprecated',hue = 'estimated_woba_using_speedangle', data = stats, palette='crest_r')
sns.scatterplot(x = 'release_spin_rate',y = 'effective_speed',hue = 'estimated_woba_using_speedangle', data = stats, palette='crest_r')
sns.lmplot(x = 'release_spin_rate',y = 'effective_speed',hue = 'estimated_woba_using_speedangle', data = stats, palette='crest_r')
stats.isna().cumsum()
empty = stats.isna().cumsum()
stats.dropna(axis=1)
stats = stats.dropna(axis=1)
stats['estimated_woba_using_speedangle']
sns.lmplot(x = 'release_spin_rate',y = 'effective_speed',hue = 'events', data = stats, palette='crest_r')
dir(pyb)
pyb.statcast_batter_exitvelo_barrels
pyb.statcast_batter_exitvelo_barrels(2021)
sc = pyb.statcast_batter_exitvelo_barrels(2021)
list = sc['player_id']
sc = pyb.statcast_batter('2021-09-01','2021-09-19', list)
list
list = pd.Series(list)
sc = pyb.statcast_batter('2021-09-01','2021-09-19', list)
sc = pyb.statcast_batter('2021-09-01','2021-09-19', [[518626,571970,458015,547180]])
sc = pyb.statcast_batter('2021-09-17','2021-09-19', [[518626,571970,458015,547180]])
sc = pyb.statcast_batter('2021-09-17', [[518626,571970,458015,547180]])
sc = pyb.statcast_batter('2021-09-19','2021-09-20', [[518626,571970,458015,547180]])
plt.scatter(x=stats['release_spin_rate'],y=stats['effective_speed'])
plt.scatter(x=stats['release_spin_rate'],y=stats['effective_speed'],alpha=0.5)
plt.scatter(x=stats['release_spin_rate'],y=stats['effective_speed'],c='r',alpha=0.5)
sns.scatterplot(x='ax',y='ay',hue='release_spin_rate',data=stats)
sns.scatterplot(x='effective_speed',y='release_spin_rate',data=stats)

## ---(Tue Sep 21 05:16:35 2021)---
pyb.statcast('2021-09-12','2021-09-19')
x = pyb.statcast()
pyb.statcast()
pyb.statcast('2021-09-19')
dir(pyb)
import pybaseball as pyb
pyb.statcast()
import pybaseball as pyb
pyb.team_batting(2021)
dir
cd
import openpyxl
from pathlib import Path
file = Path('C:\Users\Robin\BayouBobsProject\Weekly Financials')
file = Path('Users\Robin\BayouBobsProject\Weekly Financials')
wb_obj = openpyxl.load_workbook(file)
file = Path('0107 Weekly Financials.xls')
wb_obj = openpyxl.load_workbook(file)
import pandas as pd
pd.read_excel('0107 Weekly Financials.xls')
wb = pd.read_excel('0107 Weekly Financials.xls')
wb
wb.fillna(0)
wb = wb.fillna(0)
wb['Week of:'] = wb[0]
wb['Week of:'] = wb['0']
wb.drop(0)
wb[0:]
wb[0,:]
wb[0,-1]
wb['0']
days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
wb.columns = days
days = ['index','Expenses','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
wb.columns = days
days = ['','Expenses','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
days = [,'Expenses','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
days = ['Expenses','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
wb.columns = days
wb.drop(index)
wb.drop('index')
wb.drop([0])
wb = wb.drop([0])
days = ['Expenses','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Total']
wb.columns = days
wb.index([12])
wb.index[12]
wb.index = wb['Expenses']
wb.drop('Expenses')
wb.drop('Expenses',axis=1)
wb = wb.drop('Expenses',axis=1)
runcell(0, 'C:/Users/Robin/GIT/Website(baseball portfolio)/robin-hoffpauir/untitled4.py')
wb.dropna(axis=0, how = 'all')
dir(wb.index)
wb.index.isna()
wb.index.isin(0)
wb.index.isin('0')
wb.index['0']
wb.iloc(10)
wb.iloc(0)
print(wb.iloc(0))
wb.iloc(0).value()
wb.iloc(0).value
wb.index
wb.index(0)
wb.index[0]
wb.index[0]='Expenses'
wb.index[0]=['Expenses']
wb.index[0]
wb.index[1]
day=('Days')
wb.index[0]=day
wb.index[0].value
wb.index[0]=['Days']
dir(wb.index[0])
wb.index[0].real
wb.index[0].real = 'Days'
wb.index[1].real
days = ["0107 Weekly Financials.xls",
"0114 Weekly Financial 1.xls",
"0121 Weekly Financials.xls",
"0128 Weekly Financials.xls",
"0204 WEEKLY FINANCIALS.xls",
"0211 Weekly Financials.xls",
"0218 Weekly Financial .xls",
"0225 Weekly Fincancial.xls",
"0304 Weekly Financial.xls",
"0311 Weekly Financial.xls",
"0318 Weekly Financial 1.xls",
"0325 Weekly Financial .xls",
"0401 Weekly Financial2.xls",
"0408 Weekly Financial2.xls",
"0415 Weekly Financial .xls",
"0422 Weekly Financial2.xls",
"0529 Weekly Financial.xls"]
files = ["0107 Weekly Financials.xls",
"0114 Weekly Financial 1.xls",
"0121 Weekly Financials.xls",
"0128 Weekly Financials.xls",
"0204 WEEKLY FINANCIALS.xls",
"0211 Weekly Financials.xls",
"0218 Weekly Financial .xls",
"0225 Weekly Fincancial.xls",
"0304 Weekly Financial.xls",
"0311 Weekly Financial.xls",
"0318 Weekly Financial 1.xls",
"0325 Weekly Financial .xls",
"0401 Weekly Financial2.xls",
"0408 Weekly Financial2.xls",
"0415 Weekly Financial .xls",
"0422 Weekly Financial2.xls",
"0529 Weekly Financial.xls"]
wb = pd.read_excel(file)
wb = pd.read_excel(files)
for f in files:
    w_b = pd.read_excel(f)
    wb.append(w_b)
    
for f in files:
    w_b = pd.read_excel(f)
    wb = wb.append(w_b)
wb['Week Of:'].fillna(----)
wb['Week Of:'].fillna('----')
wb = wb['Week Of:'].fillna('----')
for f in files:
    w_b = pd.read_excel(f)
    wb = wb.merge(w_b)
    
wb = pd.read_excel('0107 Weekly Financials.xls')
for f in files:
    w_b = pd.read_excel(f)
    wb = wb.merge(w_b)
for f in files:
    w_b = pd.read_excel(f)
    wb = wb.concat(w_b,join='left')
    
for f in files:
    w_b = pd.read_excel(f)
    pd.concat(w_b,wb,join='left')
for f in files:
    w_b = pd.read_excel(f)
    pd.concat(w_b,wb)
for f in files:
    w_b = pd.read_excel(f)
    wb = pd.merge(wb,w_b,how='inner')
    
wb=pd.DataFrame()
for f in files:
    w_b = pd.read_excel(f)
    z = pd.merge(wb,w_b,how='inner')
wb=pd.DataFrame(columns=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Total'])
for f in files:
    w_b = pd.read_excel(f)
    z = pd.merge(wb,w_b,how='inner')
wb=pd.DataFrame(columns=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Total'])
for f in files:
    w_b = pd.read_excel(f)
    z = pd.merge(wb,w_b,how='right')
day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Total']
wb=pd.DataFrame(columns=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Total'])
for f in files:
    w_b = pd.read_excel(f)
    w_b.columns = day
    z = pd.merge(wb,w_b,how='right')
day = ['Company','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Total']
wb=pd.DataFrame(columns=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Total'])
for f in files:
    w_b = pd.read_excel(f)
    w_b.columns = day
    z = pd.merge(wb,w_b,how='inner')
wb=pd.DataFrame(columns=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Total'])
for f in files:
    w_b = pd.read_excel(f)
    w_b.columns = day
    wb = pd.merge(wb,w_b,how='inner')
wb=pd.DataFrame(columns=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Total'])
for f in files:
    w_b = pd.read_excel(f)
    w_b.columns = day
    wb = pd.merge(wb,w_b,how='right')
wb=pd.DataFrame(columns=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Total'])
for f in files:
    w_b = pd.read_excel(f)
    w_b.columns = day
    wb = pd.merge(wb,w_b,how='left')
wb=pd.DataFrame(columns=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Total'])
for f in files:
    w_b = pd.read_excel(f)
    w_b.columns = day
    wb = pd.merge(wb,w_b,how='inner')
wb=pd.DataFrame(columns=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Total'])
for f in files:
    w_b = pd.read_excel(f)
    w_b.columns = day
    wb = pd.merge(wb,w_b,how='right')
wb.dropna(axis=0,how='all')
wb = wb.dropna(axis=0,how='all')
wb = wb.fillna(0)
runcell(0, 'C:/Users/Robin/GIT/Website(baseball portfolio)/robin-hoffpauir/untitled4.py')
file
path = Path('C:\Users\Robin\BayouBobsProject\Weekly Financials')
path = Path('\Users\Robin\BayouBobsProject\Weekly Financials')
path = Path('Users\Robin\BayouBobsProject\Weekly Financials')
path
Path
for f in path:
    x=pd.read_excel(path)
    
files
for f in path:
    x=pd.read_excel(files)
for f in files:
    x=pd.read_excel(f)
    
for f in files:
    x=pd.read_excel(f)
    wb=wb.append(x)
for f in files:
    x=pd.read_excel(f)
    wb=wb.combine(x)
func = lambda x,x1: x+x1
for f in files:
    x=pd.read_excel(f)
    wb=wb.combine(x,func)
wb = pd.DataFrame(columns=day)
for f in files:
    x=pd.read_excel(f)
    wb = wb.add(x,axis=1)
    
wb = pd.DataFrame(columns=day)
for f in files:
    x=pd.read_excel(f)
    wb = wb.add(x,axis=1,fill_value=0)
import pybaseball as pyb
sc = pyb.statcast('2021-04-29','2021-04-30')
import pybaseball as pyb
sc = pyb.statcast('2021-04-29','2021-04-30')
dir(pyb)
from pathlib import Path
dir(pyb)
import pybaseball
dir(pybaseball)
import pybaseball
dir(pybaseball)
pybaseball.__package__
pybaseball.__path__
import pybaseball
dir(pybaseball)
pybaseball.__path__
import pybaseball as pyb
dir(pyb)
sc = pyb.statcast('2021-04-29','2021-04-30')
sc
sc['estimated_woba_using_speedangle']
sc['estimated_woba_using_speedangle'] = sc['estimated_woba_using_speedangle'].dropna()
sc['events'].unique()
event = ['field_out', 'single', 'sac_fly', 'walk', 'double',
       'strikeout', 'grounded_into_double_play', 'home_run',
       'double_play', 'hit_by_pitch', 'force_out', 'field_error',
       'fielders_choice_out', 'triple', 'sac_bunt',
       'sac_bunt_double_play', 'fielders_choice', 'catcher_interf',
       'wild_pitch', 'strikeout_double_play']
sc[sc['events']==event]
sc[sc['events']=event]
sc['events']=event
sc['events']!=None
sc[sc['events']!=None]
sc = sc[sc['events']!=None]
pyb.cache.enable()
sc['bb_type'].unique()
sc['bb_type'].dropna()

sc[sc['bb_type'].dropna()]
sc['bb_type']=sc['bb_type'].dropna()
sns.scatterplot(x='effective_speed', y='release_spinrate')
sns.scatterplot(x=int('effective_speed'), y='release_spinrate')
sc['events'].dropna()
sc.dropna(axis=1)
sc=sc.dropna(axis=1)
sc = pyb.statcast('2021-04-29','2021-04-30')
sns.scatterplot(x='plate_x',y='plate_z',hue'type',data=sc)
sns.scatterplot(x='plate_x',y='plate_z',hue='type',data=sc)
sc[sc['type']=['B','S']]
sc[sc['type']==['B','S']]
sc['type'].replace('X',NaN)'
sc['type'].replace('X',NaN)
sc['type'].replace('X','NaN')
x=sc['type'].dropna()
sc[sc['type'].dropna()]
s = sc[sc['type']=='S']
data = sc[sc['type']==['S','B']

data = sc[sc['type']==['S','B']]
data = sc[sc['type']=='S','B']
data = sc[sc['type']!='NaN']
data = sc[sc['type']!='X']
x=data['plate_x']
y=data['plate_z']
t=data['type']
sns.scatterplot(x=x,y=y,hue=t)
sns.scatterplot(x=x,y=y,hue=t,xlabel='Horizontal',ylabel='Vertical',title='Pitch Location')
sns.scatterplot(x=x,y=y,hue=t,xlab='Horizontal',ylab='Vertical',title='Pitch Location')
sns.scatterplot(x=x,y=y,hue=t,palatte='crest')
sns.scatterplot(x=x,y=y,hue=t,alpha=0.5)
data['type'].replace('S','Strike')
data=['type'] = data['type'].replace('S','Strike')
data['type'].replace(['S','B'],['Strike','Ball])
data['type'].replace(['S','B'],['Strike','Ball'])
data['type'] = data['type'].replace(['S','B'],['Strike','Ball'])
t = data['type'].replace(['S','B'],['Strike','Ball'])
sns.scatterplot(x=x,y=y,hue=t,alpha=0.5)
df = sc[sc['events']!='None']
df = sc[sc['events']!=None]
df = sc[sc['bb_type']!=None]
df = sc[sc['bb_type']!='NaN']
df['bb_type'].dropna()
df.dropna(axis=0)
df.dropna(subset=['bb_type'])
df = df.dropna(subset=['bb_type'])
x1=df['launch_angle']
x2=df['launch_speed']
hue = df['estimated_woba_using_speedangle']
sns.scatterplot(x=x1,y=x2,hue=hue)
hue = df['estimated_obp_using_speedangle']
hue = df['estimated_ba_using_speedangle']
sns.scatterplot(x=x1,y=x2,hue=hue)
hue.agg(*1000)
lam = lambda x:x*1000
hue.agg(lam)
hue = hue.agg(lam)
sns.scatterplot(x=x1,y=x2,hue=hue)
sns.scatterplot(x=x1,y=x2,hue=hue,legend='brief')
sns.scatterplot(x=x1,y=x2,hue=hue,legend='false')
sns.scatterplot(x=x1,y=x2,hue=hue,legend=False)
sns.scatterplot(x=x2,y=x1,hue=hue,legend=False)
sns.relplot(x=x2,y=x1,hue=hue,legend=False)
sns.relplot(x=x2,y=x1,hue=data['bb_type'],legend=False)
sns.relplot(x=x2,y=x1,hue=df['bb_type'],legend=False)
sns.relplot(x=x2,y=x1,hue=df['bb_type'])
sns.scatterplot(x=x1,y=x2,hue=df['bb_type'])
sns.relplot(x=x1,y=x2,hue=hue)
sns.relplot(x=x1,y=x2,hue=hue,legend=False)
sns.relplot(x='launch_angle',y='hit_distance_sc',hue='bb_type',data=df)
sns.relplot(x='launch_angle',y='hit_distance_sc',hue='estimated_ba_using_speedangle',data=df)
sns.relplot(x='launch_angle',y='hit_distance_sc',hue='bb_type',data=df,pallete='crest')
sns.scatterplot(x=df['plate_x'],y=df['plate_z'],hue=df['bb_type'])
sns.scatterplot(x=df['plate_x'],y=df['plate_z'],hue=df['pitch_name'])
sns.scatterplot(x='launch_angle',y='hit_distance_sc',hue='bb_type',data=df)
col = pyb.statcast('04-23-2021','04-24-2021',team='COL')
col = pyb.statcast('2021-04-23','2021-04-24',team='COL')
new = col[col['inning_topbot']=='Top']
col[col['inning_topbot']=='Top']
col['inning_topbot']=='Top'
sns.relplot(x=col['release_pos_x'],y=col['release_pos_z'],hue=col['player_name'])
sns.relplot(x=col['release_pos_x'],y=col['release_pos_z'],hue=col['player_name'],sizes='release_speed')
sns.relplot(x=col['release_pos_x'],y=col['release_pos_z'],hue=col['player_name'],sizes=col['release_speed'])
sns.relplot(x=col['release_pos_x'],y=col['release_pos_z'],hue=col['player_name'],size=col['release_speed'])
sns.relplot(x=col['release_pos_x'],y=col['release_pos_z'],hue=col['player_name'],markers=col['pitch_name'])
t=data['type']==['fly_ball','ground_ball']
t1=t=['fly_ball','ground_ball']
t1
t
sns.relplot(x='launch_angle',y='hit_distance_sc',hue='bb_type',data=df,kind='line')
sns.scatterplot(x='launch_angle',y='hit_distance_sc',hue='bb_type',data=df,kind='line')
sns.jointplot(x='launch_angle',y='hit_distance_sc',hue='bb_type',data=df,)
sns.hexplot(x='launch_angle',y='hit_distance_sc',hue='bb_type',data=df,)
sns.stripplot(x='launch_angle',y='hit_distance_sc',hue='bb_type',data=df,)
sns.stripplot(x='launch_angle',y='hit_distance_sc',hue='bb_type',data=df)
sns.choose_diverging_palette
sns.choose_diverging_palette()
sns.choose_diverging_palette(as_cmap=True)
sns.choose_diverging_palette()
sns.heatmap(df['plate_x','plate_z'])
sns.heatmap(df[['plate_x','plate_z']])
sns.heatmap(df)
sns.displot(x='launch_angle',y='hit_distance_sc',hue='bb_type',data=df)
sns.displot(x='plate_x',y='plate_z',data=df)
sns.displot(x='plate_x',y='plate_z',data=df,palette='crest')
sns.lineplot(x='plate_x',y='plate_z',data=df)
sns.lineplot(x='launch_angle',y='hit_distance_sc',hue='bb_type',data=df)
pd.melt(df,'bb_type',var_name='Batted_ball_type')
import sklearn as sk
from sklearn.neighbors import KNearestNeighbor
from sklearn.neighbors import KNNeighbor
dir(sklearn.neighbors)
from sklearn.neighbors import kneighbors_graph
from sklearn.neighbors import KNeighborsClassifier
x=df['bb_type']
y=df['bb_type']
x=df['plate_z','plate_x']
x=df[['plate_z','plate_x']]
neigh = KNeighborsClassifier(n_neighbors=5)
neigh.fit(x,y)
neigh.fit(x,y)
KNeighborsClassifier(...)
from sklearn import *
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25)
neigh.predict(x_test)
predict = neigh.predict(x_test)
score(predict,y_test)
sns.scatterplot(predict,y_test)
sns.scatterplot(x=predict,y=y_test)
sns.catplot(x=predict, y=y_test)
accuracy_score(predict, y_test)
from sklearn.metrics import accuracy_score
accuracy_score(predict, y_test)
neigh = KNeighborsClassifier(n_neighbors=8)
neigh.fit(x_train,y_train)
predict=neigh.predict(x_test)
accuracy_score(predict,y_test)
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(x_train,y_train)
predict=neigh.predict(x_test)
accuracy_score(predict,y_test)
neigh = KNeighborsClassifier(n_neighbors=5)
neigh.fit(x_train,y_train)
predict=neigh.predict(x_test)
accuracy_score(predict,y_test)
neigh = KNeighborsClassifier(n_neighbors=3)
x=df['launch_angle']
y=df['hit_distance_sc']
x_train, x_test, y_train, y_test = test_train_split(x,y,test_size=0.25)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25)
neigh = KNeighborsClassifier(n_neighbors=5)
neigh.fit(x_train, y_train)
accuracy_score(predict, y_test)
clf = KNeighborsClassifier(n_neighbors=5)
clf.fit(x_train,y_train)
x=np.array(x_train)
x.reshape(-1,1)
x=x.reshape(-1,1)
y=np.array(y_train)
y=y.reshape(-1,1)
clf.fit(x,y)
y=df['bb_type']
x=df[['launch_angle','hit_distance_sc']]
x_train, x_test, y_train, y_test = test_train_split(x,y,test_size=0.25)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25)
clf.fit(x_train, y_train)
x_train.dropna()
x_train = x_train.dropna()
y_train = y_train.dropna()
clf.fit(x_train, y_train)
import pybaseball as pyb
dir(pyb)
arm_angle = sns.relplot(x=col['release_pos_x'],y=col['release_pos_z'],hue=col['player_name'])
arm_angle.set(xlim=(-3.0,3.0))
arm_angle.set(ylim=(0,7))
arm_angle
runcell(0, 'C:/Users/Robin/untitled5.py')
type(x)
df['release_pos_z']=df['release_pos_z'].astype(int)
df['release_pos_x']=df['release_pos_x'].astype(int)
runcell(0, 'C:/Users/Robin/untitled5.py')
arm_angle = sns.jointplot(x=col['release_pos_x'],y=col['release_pos_z'],hue=col['player_name'],kind='kde')
arm_angle = sns.kdeplot(x=col['release_pos_x'],y=col['release_pos_z'],hue=col['player_name'])
sns.kdeplot('plate_x','plate_z',data=df)

## ---(Thu Sep 23 01:44:15 2021)---
import pybaseball as pyb
df = pyb.statcast('2021-09-01','2021-09-15')

## ---(Thu Sep 23 04:23:42 2021)---
import pybaseball as pyb
df = pyb.statcast('2021-09-20','2021-09-22')
df = df.dropna(axis=1,how='all')
df=df[df['type']=='X']
import seaborn as sns
from seaborn import *
sns.relplot(x='launch_angle',y='hit_distance_sc',hue='bb_type',data=df)
pip install plotnine
runcell(0, 'C:/Users/Robin/.spyder-py3/temp.py')