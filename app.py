from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    return jsonify({'message': 'Hello, this is data from the server!'})

if __name__ == '__main__':
    app.run(debug=True)
