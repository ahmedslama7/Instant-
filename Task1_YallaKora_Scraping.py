import requests
from bs4 import BeautifulSoup

List_Of_ChampionShips = []
List_Of_Teams = []
List_Of_Results = []

date = input("Please enter the date mm/dd/yyyy:\t")
url = f"https://www.yallakora.com/match-center/?date={date}"
src = requests.get(url)

page = src.content
soup = BeautifulSoup(page , "html")
#print(soup.prettify())

Container = soup.find('div', {'class':"dayDtlsContent"})

ChampionShips = Container.find_all('div',{'class':"matchCard"})

for championship in range(len(ChampionShips)):
    ChampionShip_title = ChampionShips[championship].contents[1].find('h2').text.strip()
    print(ChampionShip_title)
    List_Of_ChampionShips.append(ChampionShip_title)
    
    matchs = ChampionShips[championship].contents[3].find_all("div", {'class':"item finish liItem"})
    for match_ in range(len(matchs)):
        Team_A = matchs[match_].contents[1].find("div", {'class':"teams teamA"}).find("p").text.strip()
        Team_B = matchs[match_].contents[1].find("div", {'class':"teams teamB"}).find("p").text.strip()
        
        Teams = Team_A +" - "+Team_B
        print(Teams)
        List_Of_Teams.append(Teams)
        
        Result = matchs[match_].contents[1].find("div", {'class':"MResult"}).find_all("span", {"class":"score"})
        Result = str(Result[0].text.strip())+" | "+str(Result[1].text.strip())
        print(Result)
        List_Of_Results.append(Result)
        
        print("\n")

#Save DataSet
Data = {'Team_A Vs Team_B':List_Of_Teams,
        'Results':List_Of_Results}

import pandas as pd
Dataframe = pd.DataFrame(Data)
file_name = input("please enter the name of file:\t")
Dataframe.to_csv(f'{file_name}.csv')


        
# #Tiltle-------------------------------------------------------------------------

# ChampionShip_title = ChampionShips.contents[1].find('h2').text.strip()
# print(ChampionShip_title)

 
# matchs = ChampionShips.contents[3].find_all("div", {'class':"item finish liItem"})
# #print(len(matchs))
    
# for match_ in range(len(matchs)):
#     #Teams--------------------------------------------------------------------------

#     Team_A = matchs[match_].contents[1].find("div", {'class':"teams teamA"}).find("p").text.strip()
 
#     Team_B = matchs[match_].contents[1].find("div", {'class':"teams teamB"}).find("p").text.strip()

#     Teams = Team_A +" - "+Team_B
#     print(Teams)
    
#     #Match_Result-------------------------------------------------------------------
    
#     Result = matchs[match_].contents[1].find("div", {'class':"MResult"}).find_all("span", {"class":"score"})
#     Result = Result[0].text.strip()+"-"+Result[1].text.strip()
#     print(Result)


