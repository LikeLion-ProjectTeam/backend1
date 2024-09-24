from flask import Flask, render_template, request, redirect, url_for, flash # type: ignore

app = Flask(__name__)
app.secret_key = 'key';

#시험용 더미 데이터 
test_data = {
    "이시준" : "12345",
    "종강기원" : "abcdefg"
}

#디폴트로 처음 방문시 로그인 페이지 호출
@app.route('/')
def home():
    return render_template('login.html')

#로그인
@app.route('/login', methods=['POST'])
def login():
    #입력칸 생성
    username = request.form['user']
    password = request.form['password']
    #더미 데이터 베이스 내에서 직접 대조
    if username in test_data and test_data[username] == password:
        return f"Welcome, {username}!"
    else:
        flash('Uesrname or password is invalid')
        return redirect(url_for('home'))
    
if __name__ == '__main__':
    app.run(debug=True)




