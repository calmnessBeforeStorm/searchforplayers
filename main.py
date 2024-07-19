import requests
import json
import datetime

def fetch_leaderboard(region):
    url = f"https://www.dota2.com/webapi/ILeaderboard/GetDivisionLeaderboard/v0001?division={region}&leaderboard=0"
    response = requests.get(url)
    return response.json()

def save_data(data, region):
    now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    
    jsonFile = f'data_{region}.json'
    txtFile = f'data_{region}.txt'

    with open(jsonFile, 'w', encoding="utf-8") as file:
        file.write(json.dumps(data, indent=3))

    leaderboard = data['leaderboard']

    kzPlayers = []
    q = 1
    print(f"Текущая дата: {str(now)}\n")
    for item in leaderboard:
        if "country" in item:
            country = item["country"]
            if country == 'kz':
                try:
                    kzPlayers.append({
                        'rank': item['rank'],
                        'name': item['name'],
                        'team_tag': item['team_tag']
                    })
                    print(f"{q})\nРанг: {item['rank']}\nНик: {item['name']}\nКоманда: {item['team_tag']}")
                    q += 1
                except KeyError:
                    continue
    
    with open(txtFile, 'w', encoding="utf-8") as file:
        w = 1
        file.write(f"Текущая дата: {now}\n\n")
        for item in kzPlayers:
            file.write(f"{w})\nРанг: {item['rank']}\nНик: {item['name']}\nКоманда: {item['team_tag']}\n\n")
            w += 1

def main():
    regions = {
        '1': 'europe',
        '2': 'americas',
        '3': 'se_asia',
        '4': 'china'
    }

    while True:
        print("Выберите регион:\n")
        print("1 - Европа")
        print("2 - Америка")
        print("3 - Юго-Восточная Азия")
        print("4 - Китай\n")
        print("Введите 'q' или 'quit' для выхода из программы\n")
        choice = input("Введите номер региона: ")

        if choice in regions:
            region = regions[choice]
            data = fetch_leaderboard(region)
            save_data(data, region)
        elif choice == "q" or choice == "quit":
            print("Мы вышли из программы")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")
if __name__ == "__main__":
    main()
