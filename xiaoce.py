import requests
import time


class Xiaoce:
    def __init__(self,cookie):
        self.headers = {
            "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
            "cookie" :cookie
        }
        self.date = time.strftime("%Y%m%d")
    def daily_challenge(self):
        response = requests.get("http://xiaoce.fun/api/v0/quiz/daily/list?sort=hot", headers=self.headers).json()
        count = 0
        if response['success']:
            _quizzes = [{__: quiz[__] for __ in ["type", "name", "subType"]} for quiz in response['data']]
            for quiz in _quizzes:
                response = requests.get(
                    f"http://xiaoce.fun/api/v0/quiz/daily/addRecord?type={quiz['type']}&date={self.date}&status=success" + (
                        f"&subType={quiz['subType']}" if quiz['subType'] is not None else ""), headers=self.headers).json()
                if response['success']:
                    count += 1
                    print(f"\r[每日挑战] {quiz['name']} 已完成。", end='')
        print(f'\r[每日挑战] 完成了 {count} 个项目！')



if __name__ == "__main__":
    with open("cookies.dat",'r') as f:
        xiaoce = Xiaoce(f.read().strip())
        xiaoce.daily_challenge()
