from flask import Flask, render_template,redirect

app=Flask(__name__)

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/")
def login():
    return render_template('login.html')


@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/blogs")
def blogs():
    return render_template('blogs.html')

@app.route("/explore")
def explore():
    return render_template('explore.html')

if __name__=="__main__":
    app.run(debug=True)