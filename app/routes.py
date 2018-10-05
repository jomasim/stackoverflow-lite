from flask import Flask, redirect

# create flask app
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
    


# define endpoints
@app.route('/')
def home():
    return "welcome to stackoverflow-lite"


@app.route('/api/v1/sign-up/', strict_slashes=False)
def register():
    return "welcome to sign up"


@app.route('/api/v1/login/', strict_slashes=False)
def login():
    return "register here"
