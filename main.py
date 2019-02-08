from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("palindrom_home.html")


@app.route('/palindrom',methods=['POST', 'GET'])
def palindrom():
    if request.method == 'POST':
        number=request.form['nm']
        actual=int(number)
        if number == str(number)[::-1]:
          return 'The given number is palindrom'
        else:
            return 'The given number is NOT a palindrom'

if __name__ == '__main__':
    app.run(debug = True)
