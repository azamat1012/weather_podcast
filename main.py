import requests


def main():
    params = {
        'm': '',
        'n': '',
        'q': '',
        'T': '',
        'lang=ru': ''
    }

    url_template= "https://wttr.in/{}"
    locations = ["Лондон", "Шереметьево", "Череповец"]
    
    for location in locations:
        url = url_template.format(location)

        response = requests.get(url, params=params)
        response.raise_for_status()

        print(response.text)


if __name__ == "__main__":
    main()
