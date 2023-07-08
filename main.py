import requests, json, datetime

r = requests.get("https://www.dota2.com/webapi/ILeaderboard/GetDivisionLeaderboard/v0001?division=europe&leaderboard=0") #Европейский Ладдер
#r = requests.get("https://www.dota2.com/webapi/ILeaderboard/GetDivisionLeaderboard/v0001?division=americas&leaderboard=0") #Американский ладдер
#r = requests.get("https://www.dota2.com/webapi/ILeaderboard/GetDivisionLeaderboard/v0001?division=se_asia&leaderboard=0") #Юго-Восточный ладдер
#r = requests.get("https://www.dota2.com/webapi/ILeaderboard/GetDivisionLeaderboard/v0001?division=china&leaderboard=0") #Китайский ладдер

data = r.json()

now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

jsonFile = 'dataEurope.json'
txtFile = 'dataEurope.txt'

with open(jsonFile, 'w', encoding="utf-8") as file:
    file.write(json.dumps(data, indent=3))

leaderboard = data['leaderboard']

kzPlayers = []
q = 0
print(f"Текущая дата: {str(now)}\n")
for item in leaderboard:
     if "country" in item:
        country = item["country"]
        if country == 'kz':
            try:
                q += 1
                kzPlayers.append({
                'rank': item['rank'],
                'name': item['name'],
                'team_tag': item['team_tag']
                })
                
                print(f"{q})\nРанг: {item['rank']}\nНик: {item['name']}\nКоманда: {item['team_tag']}")
            except KeyError:
                continue
 
with open(txtFile, 'w', encoding="utf-8") as file:
    w = 1
    file.write(f"Текущая дата: {now}\n\n")
    for item in kzPlayers:
            file.write(f"{w})")
            file.write(f"\nРанг: {item['rank']}\nНик: {item['name']}\nКоманда: {item['team_tag']}\n\n")
            w += 1

        
