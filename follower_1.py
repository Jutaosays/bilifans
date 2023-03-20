
import requests
import time
from datetime import datetime, timedelta

uid = '在这里输入up主uid号'

while True:
    url = f'https://api.bilibili.com/x/web-interface/card?mid={uid}'
    response = requests.get(url)
    data = response.json()

    name = data['data']['card']['name']
    follower = data['data']['card']['fans']
    unfollower=1532700-int(follower)


    current_time = datetime.utcnow() + timedelta(hours=8)
    current_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

    print(f'Up主：{name}(UID:{uid}),实时关注人数：\033[1;31m{follower}\033[0m，实时掉粉数：{unfollower},时间：{current_time}')

    time.sleep(10)
