from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "jesse the big red dog"


@app.route('/')
def home():
    if 'count' not in session:
        session['count'] = 0
        return render_template('index.html')
    else:
        session['count'] += 1
        return render_template('index.html')
    
@app.route('/add-1')
def add_1():
    session['count'] += 0
    return redirect('/')

@app.route('/add-2')
def add_2():
    session['count'] += 1
    return redirect('/')

@app.route('/clear-session')
def clear_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)