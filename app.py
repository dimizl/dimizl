from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def Index():
    return render_template('login.html')
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    #elif request.method == 'POST':
        

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80, debug=True)