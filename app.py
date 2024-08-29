from flask import Flask, jsonify, render_template

app = Flask(__name__)

DEV = True

@app.route('/')
def home():
    
    with open('./content/intro.txt', 'r') as file:
        intro = file.read()

    with open('./content/lorem.txt', 'r') as file:
        lorem = file.read()
    return render_template('index.html', intro=intro, lorem=lorem)

@app.route('/get_data')
def get_data():
    
    return jsonify({'message': 'Ooooo interactivity'})

if __name__ == '__main__':
    
    app.run(debug=True)

