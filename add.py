import requests
import time
from bs4 import BeautifulSoup
import os
os.system(f"title Auto Friend")
os.system('cls') 
print('\033[92m')
cookie = input('Nhập cookie: ')
if 'c_user=' in cookie:
    tg = input('Nhập thời gian delay sau mỗi lần (s): ')
    list = open('uid.txt', 'r')
    while True:
        uid = list.readline().strip()
        if uid == '':
            input('CHẠY XONG !!!!')
        headers1 = {
            'authority': 'mbasic.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4685.46 Safari/537.36',
        }

        params1 = {
            'id': uid,
        }

        r1 = requests.get('https://mbasic.facebook.com/profile.php', params=params1, headers=headers1)
        soup = BeautifulSoup(r1.text, 'html.parser')
        for link in soup.find_all('a'):
            if 'profile_button' in str(link.get('href')):
                link1 = link.get('href')
        a1, b1 = link1.split('eav=')
        c1, d1 = b1.split('&paipv=0&ext=')
        e1, f1 = d1.split('&hash=')
        g1, h1 = f1.split('&')
        headers2 = {
            'authority': 'mbasic.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': cookie,
            'referer': f'https://mbasic.facebook.com/profile.php?id={uid}',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4685.46 Safari/537.36',
        }

        params2 = {
            'subject_id': uid,
            'is_timeline': '1',
            'how_found': 'profile_button',
            'ref_param': 'unknown',
            'referrer_id': '0',
            'eav': c1,
            'paipv': '0',
            'ext': e1,
            'hash': g1,
            'refid': '17',
        }
        try:
            r2 = requests.get('https://mbasic.facebook.com/a/friends/profile/add/', params=params2, headers=headers2)
            if r2.status_code == 200:
                print(f'Đã kết bạn với {uid}')
                print(f'Tạm nghỉ {tg}s')
                time.sleep(int(tg))
            else:
                print(f'Lỗi kết bạn với {uid}')
                print(f'Tạm nghỉ {tg}s')
                time.sleep(int(tg))
        except:
            print('Lỗi không xác định...')
else:
    input('Hãy nhập đúng định dạng Cookie.!')