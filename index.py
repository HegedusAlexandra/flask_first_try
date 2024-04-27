from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)
routes = ['login', 'user']
unique_login='blabla'
unique_user='hable'

@app.route('/month/<int:year>/<int:month>')
def month(year, month):
    # Calculate the first day of the month
    first_day = datetime(year, month, 1)
    
    # Calculate the number of days in the month
    num_days = (first_day + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    
    # Generate a list of dates for the month
    dates = [first_day + timedelta(days=i) for i in range(num_days.days)]
    
    return render_template('month.html', year=year, month=month, dates=dates)



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


