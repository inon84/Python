apple_ids = [357828853,
            389157776,
            909998122,
            521633042,
            545551605,
            1176001245,
            1044413150] # remove when un-needed

import requests

API_URL = 'https://itunes.apple.com/lookup?country=us'

def main(apple_ids):
    if not apple_ids:
        print('No input provided')
        return
    with requests.Session() as s:
        for id in apple_ids:
            url = f'{API_URL}&id={id}'
            r = s.get(url)
            data = r.json()
            if not data.get('resultCount', 0):
                print(f'No results found, check your input Apple App ID: {id}')
            elif 'results' in data:
                bundle = data['results'][0].get('bundleId', 'N/A')
                print(f'AppStoreID: {id}, BundleID: {bundle}')
            else:
                print(f'Invalid response from server for Apple App ID: {id}')

if __name__ == "__main__":
    main(apple_ids)
