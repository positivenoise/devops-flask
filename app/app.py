from flask import Flask, render_template, session, request
app = Flask(__name__)
app.secret_key = 'welcome to the jungle'
 
@app.route("/")
def main():
    if 'username' in session:
        return render_template('index.html', session_user_name=session['username'])
    return render_template('index.html')

@app.route("/login", methods=['GET','POST'])
def login():
    if 'username' in session:
        return main()
    if request.method == 'POST':
        username_form = request.form['username']
        password_form = request.form['password']
        if username_form == "brendan.muscat@gmail.com" and password_form == "hello":
            session['username'] = username_form
            return main()
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop('username', None)
    return main()
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')