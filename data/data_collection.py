
# coding: utf-8

# In[1]:

import numpy as np
import requests
import os
import pandas as pd
from selenium import webdriver
import time
import copy
import urllib3
from bs4 import BeautifulSoup
import re
import csv
from selenium import webdriver


# In[2]:

def preprocess_match(game, team_name, fileName):
    matchID_set = [str(x) for x in range(0, 200)]
    game.rename(columns = {'Unnamed: 5':'Home_away'}, inplace = True)
    mask_home = (game['Home_away'] == '@')
    mask_away = (game['Home_away'] != '@')
    game.loc[mask_home, 'Home_away'] = 1
    game.loc[mask_away, 'Home_away'] = 0
    game = game.loc[game['G'].isin(matchID_set)]
    game = game[['G', 'Opponent', 'Home_away','Tm', 'Opp']]
    file_path = './match_data/' + team_name 
    os.makedirs(file_path, exist_ok=True)
    game.to_csv(file_path + '/' + fileName + '.csv')
def collect_match(start_year, end_year, team_name, dict_used_name):
    year_list = [str(x) for x in range(start_year, end_year)]
    for year in year_list:
        for team in dict_used_name:
            url = 'https://www.basketball-reference.com/teams/' + team +'/' + year + '_games.html'
            try:
                tb = pd.read_html(url)
                fileName = team_name +'_'+ year + '_regular'
                preprocess_match(tb[0], team_name,  fileName)
                try :
                    tb[1]
                except:
                    continue
                fileName = team_name +'_'+ year + '_playoff'
                preprocess_match(tb[1], team_name, fileName)
            except:
                continue
             
def collect_coach_id():
    coach_id = []
    res = requests.get('https://www.basketball-reference.com/coaches/NBA_stats.html/')
    regular_exp = '.*><a href="/coaches/' + charc + '/(.*)">.*'
    result = re.findall(regular_exp, res.text)
    for x in result:
        coach_id.append(x.split(".html")[0])
    file = open('./coach_data/coach_id.txt', 'w')
    for cid in coach_id:
        file.write("%s\n" % cid)
def collect_player_id():
    alphabet = [chr(i) for i in range(97,123)] 
    player_id = []
    for charc in alphabet:
        res = requests.get('https://www.basketball-reference.com/players/' + charc +'/')
        regular_exp = '.*><a href="/players/' + charc + '/(.*)">.*'
        result = re.findall(regular_exp, res.text)
        for x in result:
            player_id.append(x.split(".html")[0])
    file = open('./player_data/player_id.txt', 'w')
    for pid in player_id:
        file.write("%s\n" % pid)
def read_player_id():
    with open('./player_data/player_id.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    return content
def collect_player_basic():
    alphabet = [chr(i) for i in range(97,123)] 
    for charc in alphabet:
        if charc != 'x':
            url = 'https://www.basketball-reference.com/players/' + charc + '/'
            tb = pd.read_html(url)
            for k in range(len(tb[0]['Ht'])):
                tb[0]['Ht'][k] = str(tb[0]['Ht'][k]) + '\t'
            file_path = './player_data/basic/' 
            os.makedirs(file_path, exist_ok=True)
            tb[0].to_csv(file_path + '/' + charc + '.csv')     
def collect_player_performance():
    player_id = read_player_id()
    for pid in player_id:
        for year in range(1999, 2018):
#             print('https://www.basketball-reference.com/players/' + pid[0] +'/' + str(pid) + '/gamelog/' + str(year) +'/')
            try:
                url = 'https://www.basketball-reference.com/players/' + pid[0] +'/' + str(pid) + '/gamelog/' + str(year) +'/'
                tb = pd.read_html(url)
                file_path = './player_data/performance/' + str(year) + '/regular/' + pid[0] 
                os.makedirs(file_path, exist_ok=True)
                tb[7].to_csv(file_path + '/' + pid + '.csv')
#                 print('save')
            except:
                continue
# def collect_player_average():
#     player_id = read_player_id()
#     for pid in player_id:


# In[11]:

# collect_player_performance()
# https://www.basketball-reference.com/players/c/curryst01.html
player_id = read_player_id()
count = 0
for pid in player_id:
    try:
        url = 'https://www.basketball-reference.com/players/'+pid[0]+'/'+pid+'.html'
        tb = pd.read_html(url)
        col_ct = 0
        lst = (list(tb[0])[0:30])
        for it in lst:
            if it.split(':')[0] != 'Unnamed':
                col_ct += 1
            else:
                break
        tb = tb[0][list(tb[0])[0:col_ct]]
        tb.insert(loc=0, column='Id', value= [pid] * len(tb['Season']))
        tb = tb[0:-1]
        if count == 0:
            all_tab = copy.deepcopy(tb)
            count += 1
        else:
            all_tab = all_tab.append(copy.deepcopy(tb))
        print(pid)
    except:
        continue
all_tab = all_tab.fillna(0)
all_tab.to_csv('player_perform_avg.csv')


# In[10]:

all_tab = all_tab.fillna(0)
all_tab['3P%']


# In[ ]:

dict_used_name = {}
dict_used_name['ATL'] = ['ATL','STL', 'MLH']
dict_used_name['BOS'] = ['BOS']
dict_used_name['BRK'] = ['BRK', 'NJN', 'NYN','NJA','NYA']
dict_used_name['CHO'] = ['CHO','CHH','CHA']
dict_used_name['CHI'] = ['CHI']
dict_used_name['CLE'] = ['CLE']
dict_used_name['DAL'] = ['DAL']
dict_used_name['DEN'] = ['DEN', 'DNR','DNA']
dict_used_name['DET'] = ['DET', 'FTW']
dict_used_name['GSW'] = ['GSW', 'SFW', 'PHW']
dict_used_name['HOU'] = ['HOU', 'SDR']
dict_used_name['IND'] = ['IND', 'INA']
dict_used_name['LAC'] = ['LAC', 'SDC', 'BUF']
dict_used_name['LAL'] = ['LAL', 'MNL']
dict_used_name['MEM'] = ['MEM', 'VAN']
dict_used_name['MIA'] = ['MIA']
dict_used_name['MIL'] = ['MIL']
dict_used_name['MIN'] = ['MIN']
dict_used_name['NOP'] = ['NOP', 'NOK','NOH']
dict_used_name['NYK'] = ['NYK']
dict_used_name['OKC'] = ['SEA', 'OKC']
dict_used_name['ORL'] = ['ORL']
dict_used_name['PHI'] = ['PHI', 'SYR']
dict_used_name['PHO'] = ['PHO']
dict_used_name['POR'] = ['POR']
dict_used_name['SAS'] = ['SAS', 'DLC', 'TEX', 'SAA']
dict_used_name['SAC'] = ['SAC', 'KCK','KCO','CIN','ROC']
dict_used_name['TOR'] = ['TOR']
dict_used_name['UTA'] = ['UTA', 'NOJ']
dict_used_name['WAS'] = ['WAS', 'WSB','CAP','BAL','CHZ','CHP']
team_name_list = ['ATL', 'BOS', 'BRK', 'CHO', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 
                  'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 
                  'OKC', 'ORL', 'PHI', 'PHO', 'POR', 'SAS', 'SAC', 'TOR', 'UTA', 'WAS']
start_year = 1980
end_year = 1981
for team in team_name_list:
    collect_match(start_year, end_year, team, dict_used_name[team])


# In[36]:

pid_list = read_player_id()


# In[9]:

collect_player_basic()


# In[81]:


driver = webdriver.Chrome()
driver.get('https://www.basketball-reference.com/players/z/zellety01/gamelog/2017/')
soup = BeautifulSoup(driver.page_source,'lxml')
driver.quit()
table = soup.find_all('table')[-1]  #This is the index of any table of that page. If you change it you can get different tables.
# print(table[])
tab_data = [[celldata.text for celldata in rowdata.find_all(["th","td"])]
                        for rowdata in table.find_all("tr")]

with open("./player_data/performance/test.csv",'w') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    for k in tab_data:
        wr.writerow(k)


# In[33]:

# options.add_argument("--test-type")
# options.binary_location = "/usr/bin/chromium"
# # driver = webdriver.Chrome()
# driver.get('https://www.basketball-reference.com/players/a/')


# In[34]:

# driver = webdriver.Chrome()


# In[9]:




# In[2]:

# file_path = './team_data/' + 'AHL'
# print(file_path)
# os.makedirs(file_path)


# In[60]:




# In[ ]:




# In[3]:

url = 'https://www.basketball-reference.com/players/z/zellety01/gamelog/2017/#pgl_basic_playoffs::none'
tb = pd.read_html(url)


# In[4]:




# In[3]:

# import urllib.request
with urllib.request.urlopen("https://www.basketball-reference.com/players/z/zellety01/gamelog/2017/") as url:
    html_text = url.read()
# print(html_text)
from bs4 import BeautifulSoup, Comment
soup = BeautifulSoup(html_text, 'lxml')
comments = soup.findAll(text=lambda text:isinstance(text, Comment))
[comment.extract() for comment in comments]


# In[60]:

type(html_text)


# In[4]:

alphabet = [chr(i) for i in range(97,98)] 
for charc in alphabet:
    if charc != 'x':
        url = 'https://www.basketball-reference.com/players/' + charc + '/'
        tb = pd.read_html(url)
        for k in range(len(tb[0]['Ht'])):
            tb[0]['Ht'][k] = str(tb[0]['Ht'][k]) + '\t'
        file_path = './player_data/basic/' 
        os.makedirs(file_path, exist_ok=True)
        tb[0].to_csv(file_path + '/' + charc + '.csv')     



# In[5]:

url = 'https://www.basketball-reference.com/players/' + 'a' + '/'
tb = pd.read_html(url)


# In[6]:

tb


# In[ ]:



