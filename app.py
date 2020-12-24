from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
        "https://files.slack.com/files-pri/T024TCSN9-F01GM16VA5U/ios_______.gif",
	"https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fu1MBP%2FbtqEgQZP2NJ%2FucXogL5koT9K7idkoZioJk%2Fimg.gif",
	"https://mblogthumb-phinf.pstatic.net/MjAxODAzMjZfMTIy/MDAxNTIxOTkwODA4NDQ5.hutL1xCVQCBV7W89PGCXY8ExkP3fgDwK9mMPWzcitgMg.ju1wEuU9OeYwTrMK2x3Fxn6HdNOqSWLg4U2v1N7n2dwg.GIF.gpal762/m_entertainer1-20180325-163249-000.gif?type=w800",
	"https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F8zTkq%2FbtqHVosQ1vk%2FlekwS4c6aqgUGcoSsvZOx0%2Fimg.gif",
	"https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FvSjnD%2FbtqH0qDuArx%2FLcdVj5Qvrlb3ygqKo0lFyk%2Fimg.gif",
	"https://mblogthumb-phinf.pstatic.net/MjAxODAyMjdfMTk1/MDAxNTE5NzMxNjE5MTI4.hcBxr6amiZnEq5AVaWNqFGTyLib3OoS9gej4VNXzBhUg.gm8YHw0f1pJlaRGTdXnkH3w1dFQeVWnqE7cwhQzrsccg.GIF.thatluv/1519606689664.gif?type=w2",
	"https://mblogthumb-phinf.pstatic.net/MjAxODAyMjdfMjUw/MDAxNTE5NzMxNjIxNjM1.xrdjUcmCW1hkUM53J-5kYB-1i8808Ko-SwgvGHRP020g.QeDkwQ6cVGYSdGkGoriszfxn_B5VCxc5RNMowmCswCIg.GIF.thatluv/1519606683127.gif?type=w2",
	"https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile8.uf.tistory.com%2Fimage%2F992C90385B23791F049C38",
	"https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile27.uf.tistory.com%2Fimage%2F995C85385B2379221E5CB9",
	"https://img.theqoo.net/proxy/https://i.imgur.com/xo063lr.gif",
	"https://post-phinf.pstatic.net/MjAyMDEyMTFfMjM1/MDAxNjA3NjUyMzQzNDUz.aW_tyQqF92LR9qLWuRdTY_aQhpUMHeiNeY2aihJGh1og.nprkygAx4LX5craP66ZGqI0mVGpGx4sbnUr6fFIe5awg.GIF/%EC%97%94%EC%8B%9C%ED%8B%B0_%EC%A0%95%EC%9A%B0.gif?type=w1200",
	"https://post-phinf.pstatic.net/MjAyMDEyMTFfMjgx/MDAxNjA3NjUyMzQzNTg2.OhNTKQRi4ZF3VgHvtptZcDdSX7x3yZ4iP1RV7avlbn4g.f3sWRQk4MnfmFXlM-rNkxQK7znqraTHmwGldY11weVog.GIF/%EC%97%94%EC%8B%9C%ED%8B%B0_%EC%A0%95%EC%9A%B03.gif?type=w1200",
	"https://post-phinf.pstatic.net/MjAyMDEyMTFfMyAg/MDAxNjA3NjUyNjQ4MDIy.MRL-HfWjUPsXVZsZRPGi58eXq1uVz7Tu3nRklCJKAhYg.7RqQs35oyi3RQ0yD1z1t07lBXOSSl82TzPjDuncvok0g.GIF/%EC%97%94%EC%8B%9C%ED%8B%B0_%EC%A0%95%EC%9A%B04.gif?type=w1200"
	
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
