import requests


def main():

    locations = ["Лондон", "Шереметьево", "Череповец"]

    for location in locations:
        url = f"https://wttr.in/{location}?m&n&q&T&lang=ru"

        response = requests.get(url)
        response.raise_for_status()

        print(response.text)


if __name__ == "__main__":
    main()
