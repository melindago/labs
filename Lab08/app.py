from flask import Flask, render_template, request
from apod_model import get_apod

app = Flask(__name__)

@app.route('/')
def home():
    try:
        apod_data = get_apod()
        print(f"APOD data for home: {apod_data}")
        return render_template('home.html', data=apod_data)
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/history', methods=['GET', 'POST'])
def history():
    apod_data = None
    if request.method == 'POST':
        date = request.form['date']
        print(f"Date received from form: {date}") 
        if date:
            try:
                apod_data = get_apod(date=date)
                print(f"APOD data for history with date {date}: {apod_data}")
            except Exception as e:
                    return f"An error occurred: {e}"
    return render_template('history.html', data=apod_data)

if __name__ == '__main__':
    app.run(debug=True)

