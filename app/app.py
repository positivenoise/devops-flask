from flask import Flask, render_template, session, request
import MySQLdb
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

        cur.execute("SELECT COUNT(1) FROM users WHERE username = %s;", [username_form])
        if cur.fetchone()[0]:
            cur.execute("SELECT password FROM users WHERE username = %s;", [username_form])
            for row in cur.fetchall():
                if password_form == row[0]:
                    session['username'] = username_form
        return main()
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop('username', None)
    return main()
 
if __name__ == "__main__":
    db = MySQLdb.connect(host="db", user="root", passwd="my-secret-password", db="flask")
    cur = db.cursor()
    app.run(host='0.0.0.0')