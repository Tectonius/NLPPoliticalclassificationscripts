import pandas as pd

subredditlist = ["DebateAltRight",
"Anarchism",
"childfree",
"communism101",
"Conservative",
"ZeroWaste",
"GenderCritical",
"flatearth",
"antiMLM",
"asktrp",
"neoliberal",
"netneutrality",
"nihilism",
"socialism",
"collapse",
"Stoicism"]

data = pd.read_csv('rspctfile.csv')
DebateAltRightdata = data[data['subreddit'] == 'DebateAltRight']
print(1)
Anarchismdata = data[data['subreddit'] == 'Anarchism']
print(2)
childfreedata = data[data['subreddit'] == 'childfree']
print(3)
communism101data = data[data['subreddit'] == 'communism101']
print(4)
Conservativedata = data[data['subreddit'] == 'Conservative']
print(5)
ZeroWastedata = data[data['subreddit'] == 'ZeroWaste']
print(6)
GenderCriticaldata = data[data['subreddit'] == 'GenderCritical']
print(7)
flatearthdata = data[data['subreddit'] == 'flatearth']
print(8)
antiMLMdata = data[data['subreddit'] == 'antiMLM']
print(9)
asktrpdata = data[data['subreddit'] == 'asktrp']
print(10)
neoliberaldata = data[data['subreddit'] == 'neoliberal']
print(11)
netneutrality = data[data['subreddit'] == 'netneutrality']
print(12)
nihilismdata = data[data['subreddit'] == 'nihilism']
print(13)
socialismdata = data[data['subreddit'] == 'socialism']
print(14)
collapsedata = data[data['subreddit'] == 'collapse']
print(15)
Stoicismdata = data[data['subreddit'] == 'Stoicism']
print(16)
filtereddata = pd.concat([DebateAltRightdata, Anarchismdata, childfreedata, communism101data, Conservativedata, ZeroWastedata, GenderCriticaldata, flatearthdata, antiMLMdata, asktrpdata, neoliberaldata, netneutrality, nihilismdata, socialismdata, collapsedata, Stoicismdata ])
filtereddata = filtereddata.sample(frac=1).reset_index(drop=True)
trainingdata = filtereddata.iloc[:12800]
validationdata = filtereddata.iloc[12800:]
trainingdata.to_csv('trainingdata.csv')
validationdata.to_csv('validationdata.csv')