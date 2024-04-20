from flask import Flask
from flask import url_for
from markupsafe import escape


app = Flask(__name__)
routes = ['login', 'user']

@app.route('/')
def home():
    return 'This is the home page.'

@app.route('/<route>')
def route_display(route):
    if route in routes:
        return f'This is the {route} route.'
    else:
        url_for('static', filename='index.css')
        return '<div><img width="100px" height="100px" src="goblin.jpg"><p>Yesss, yesss, you are in the wrong path, young hobbit.<p></div>'
    




if __name__ == '__main__':
    app.run(debug=True)




