import requests


def main():

    url_template= "https://wttr.in/{}?m&n&q&T&lang=ru"
    locations = ["Лондон", "Шереметьево", "Череповец"]
    
    for location in locations:
        url = url_template.format(location)

        response = requests.get(url)
        response.raise_for_status()

        print(response.text)


if __name__ == "__main__":
    main()
