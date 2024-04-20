from flask import Flask, render_template

app = Flask(__name__)
routes = ['login', 'user']
unique_login='blabla'
unique_user='hable'

@app.route('/')
def home():
    return render_template('index.html', message='Welcome to you first flask project',page='landing')

@app.route('/<route>')
def route_display(route):
    if route in routes:
        return render_template(f'{route}.html',page=f'{route}', data = unique_login if route == 'login' else unique_user)
    else:
        # Render the index.html template dynamically
        return render_template('404.html', message='Yesss, yesss, you are in the wrong path, young hobbit.',page='not found')



if __name__ == '__main__':
    app.run(debug=True)


