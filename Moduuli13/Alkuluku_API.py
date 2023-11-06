from flask import Flask

app = Flask(__name__)

@app.route('/alkuluku/<user_input>')
def alkuluku(user_input):
    num = int(user_input)
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    vastaus = {
        "Number" : num,
        "isPrime" : is_prime,
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


