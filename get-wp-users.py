#!/usr/bin/env python3
import requests
import re
import argparse
import threading


def extract_users(session: requests.Session, url: str):
	base_url = url
	users = []
    url = prepare_url(base_url, 'wp-json')
    response = session.head(url)
    if response.status_code == 200:
        try:
            pages = int(response.headers['X-WP-TotalPages'])
            for page in range(pages):
                url = prepare_url(base_url, 'wp-json', page + 1)
                response = session.get(url)
                for user in re.findall(r'"slug":"(.*?)"', response.text):
                    users.append(user)
        except Exception as e:
            print(e)
    else:

        print(f'[-] Problem accessing {url}. Trying enumeration via ?author...')

        for num in range(100):
            url = prepare_url(base_url, 'author', num + 1)
            response = session.get(url)
            if response.status_code in [301, 302]:
                try:

                    user = re.match(r'{base_url}/author/(.*?)/', response.headers['Location'])

                    print(user)
                except KeyError as e:
                    print(e)
            else:
                print('Cannot enumerate using ?author.')
    return users

def prepare_url(url: str, path_name: str, num: int = 1):
    paths = {
        'xmlrpc': '/xmlrpc.php',
        'wp-json': f'/wp-json/wp/v2/users?page={num}&per_page=100',
        'author': f'/?author={num}',
    }
    return url + paths[path_name]

def brute_force(session: requests.Session, url: str, users: list, passwords: list):

    print(users)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', dest='url', help='Wordpress site URL', type=str, required=True)
    parser.add_argument('-o', '--output', dest='output', help='Output filename', type=str)
    parser.add_argument('-t', '--threads', dest='threads', help='Brute forcer threads limit', type=int, default=5)
    parser.add_argument('-f', '--firstonly', dest='firstonly', help='Stop after first success', type=bool,
                        default=False)
    parser.add_argument('-x', '--proxy', dest='proxy', help='Specify proxy to use', type=str)
    args = parser.parse_args()

    url = args.url
    proxies = {
        'http': args.proxy,
        'https': args.proxy,
    }
    session = requests.session()
    session.proxies.update(proxies)
    users = extract_users(session, url)
    print(users)


if __name__ == '__main__':
    main()
