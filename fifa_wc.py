from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_matches(year: str) -> pd.DataFrame:
    url = f"https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup"

    try:
        response = requests.get(url)
        content = response.text

        # parsing the page's html
        soup = BeautifulSoup(content, "lxml")

        # extract data of the matches
        matches = soup.find_all("div", class_="footballbox")

        home = []
        score = []
        away = []

        for match in matches:
            home.append(match.find("th", class_="fhome").get_text())
            score.append(match.find("th", class_="fscore").get_text())
            away.append(match.find("th", class_="faway").get_text())

        # criando um dicionario para organizar as listas com os dados extraídos
        dict_matches = {"home": home, "score": score, "away": away}

        # craindo o dataframe com os dados coletados
        df_world_cup = pd.DataFrame(dict_matches)
        df_world_cup["year"] = year

        return df_world_cup

    except Exception as e:
        print(f"Error at 'get_matches':\n{e}")


def main():
    # list years between 1938 and 2018 step 4, exceto os anos 1942 e 1946
    years = list(range(1930, 2023, 4))

    print("Executando consulta. Por favor aguarde!\n...")
    try:
        fifa_wc_matches = [get_matches(year) for year in years]
        df = pd.concat(fifa_wc_matches, ignore_index=True)

        # export data to csv file
        df.to_csv("fifa_world_cup_matches.csv", index=False)
        print(f'{df},\nProcesso concluido.')
    except Exception as e:
        print(f"Error at 'main':\n{e}")


if __name__ == "__main__":
    main()
