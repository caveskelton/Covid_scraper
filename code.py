import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date

response = requests.get('https://www.worldometers.info/coronavirus/country/us/')

soup = BeautifulSoup(response.content,'html.parser')

table = soup.find('table') #Covid info is stored under tbody which means its a table

#table has 15 columns and for our use table will be converted into a 1d list which mean all rows are merged into 1 big row.

# index1(note: index starts from 0) is states and index2 is total cases

index = 16 #first row(till 15th index) are USA total which we do not need so we start from 16th index 
final_states = [] #list to append
final_cases = [] #list to append

while index<960: #there are 64 states so 64x15=960 total indexes
  state = table.find_all('td')[index].text.strip() #accesing the big 1d list using indexes and getting the state , .strip() removes spaces
  final_states.append(state)
  index+=1 #the index after state is total cases
  cases = table.find_all('td')[index].text #getting the cases
  final_cases.append(cases)
  index+=14 #you can go to the same column in the nex row adding 15(we added 1 beore so now 14)
  
df = pd.DataFrame({'State':final_states,'Cases':final_cases}) #Making pandas df by using both the lists as 2 columns
date = date.today()
df.to_csv(f'{date}.csv') #writing as csv with file name as todays date
