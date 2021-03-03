import requests
import pprint


print = pprint.PrettyPrinter(indent=4).pprint


if __name__ == '__main__':
    query = 'битрикс'
    res = requests.post(
        url='https://egrul.nalog.ru/',
        data={
            'vyp3CaptchaToken': None, 
            'page': None,
            'query': query,
            'nameEq': 'on',
            'region': None
        }
    )
    print(res.json())
    t = res.json()['t']
    res = requests.get(
        url=f'https://egrul.nalog.ru/search-result/{t}'
    )
    print(res.json())
