# Suppose the input is of type [(),(),(),(),...], the number is treated as number not string.
# team_off_win = sql_state(SELECT M.team, COUNT(team) FROM match_records M WHERE M.Tm > M.Opp AND year = 2017 AND playoff_regular = 'playoff' GROUP BY team ORDER BY COUNT(team) DESC)
# team_records_reg = sql_state(SELECT team, Tm, Opp FROM match_records WHERE year = 2017 AND playoff_regular = 'regular')
# team_records_off = sql_state(SELECT team, Tm, Opp FROM match_records WHERE year = 2017 AND playoff_regular = 'playoff')
from django.db import connection
import numpy as np
from sklearn.svm import SVC

def sql_state(state):
	cursor = connection.cursor()
	    cursor.execute(state)
	    out = cursor.fetchall()
	return out

def team_rank_yr(yr):
	team_reg_win = sql_state(SELECT M.team, COUNT(team) FROM match_records M WHERE M.Tm > M.Opp AND year = 2017 AND playoff_regular = 'regular' GROUP BY team ORDER BY COUNT(team) DESC)
	team_rank = []
	for i in range(len(team)):
		team_rank = team_rank + [team_dict[team_reg_win[i,0]]]
	return team_rank

def per_processing_yr(yr1,yr2,yr3,yr4):
	team_rank_1 = team_rank_yr(yr1)
	team_rank_2 = team_rank_yr(yr2)
	team_rank_3 = team_rank_yr(yr3)
	team_rank_4 = team_rank_yr(yr4)

	Input = np.zeros((len(team_rank_4),3))
	for i in range(len(y4)):
	    Input[i,0] = y4.index(team_rank_1[i])
	    Input[i,1] = y4.index(team_rank_2[i])
	    Input[i,2] = y4.index(team_rank_3[i])

	label = np.array(list(range(1, len(y4) + 1)))
	return Input, label

def predict_input(yr,team):
	team_rank_1 = team_rank_yr(yr - 1)
	team_rank_2 = team_rank_yr(yr - 2)
	team_rank_3 = team_rank_yr(yr - 3)
	out = [team_rank_1.index(team_dict[team]), team_rank_2.index(team_dict[team]), team_rank_3.index(team_dict[team])]
	return [out]


def predict_yr(Input, label):
	clf = SVC()
	clf.fit(Input, label) 
	SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
	    decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
	    max_iter=-1, probability=False, random_state=None, shrinking=True,
	    tol=0.001, verbose=False)
	return clf



team = sql_state(SELECT DISTINCT team FROM match_records WHERE year = 2015)
team_dict = {}
dict_team = {}
for i in range(len(team)):
	team_dict[team[i,0]] = i
	dict_team[i] = team[i,0]

Input1, label1 = per_processing_yr(2012,2013,2014,2015)
Input2, label2 = per_processing_yr(2013,2014,2015,2016)
Input3, label3 = per_processing_yr(2014,2015,2016,2017)

Input = np.vstack((Input1,Input2,Input3))
label = np.vstack((label1,label2,label3))

clf = predict_yr(Input, label)
pre_input = predict_input(2018, 'POR')
rank_predict = clf.predict(pre_input)

