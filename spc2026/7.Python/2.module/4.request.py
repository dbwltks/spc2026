# 외부 모듈은 pip install requests 로 설치해야 합니다.
# 그러면, pypi.org로 부터 모듈을 다운로드 받아서, 나의 "가상환경"에 설치합니다.

import requests

# 외부에 HTTP 요청을 보내고, 응답을 받아오는 모듈입니다.
resp = requests.get("https://api.github.com")
curr_user_url = resp.json()["current_user_url"] # 현재 사용자의 URL
print(curr_user_url)
