from flask import Flask, render_template, request
import segno

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.form.get('data')
    print("Data received:", data)  # This should print the entered data in the terminal
    qr_code = segno.make(data)
    qr_code.save('static/qr_code.png')
    print("QR code saved")  # To confirm that the QR code is saved
    return render_template('index.html', qr_generated=True)

if __name__ == '__main__':
    app.run(debug=True)
