from flask import Flask, jsonify, render_template

app = Flask(__name__)

DEV = True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    
    return jsonify({'message': 'Ooooo interactivity'})

if __name__ == '__main__':
    
    app.run(debug=True)

