from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('data.csv')

@app.route('/data', methods=["GET"])
def get_data():
    return jsonify(pd.to_dict(orient='records'))

@app.route('/average salary', methods=["GET"])
def get_average_salary():
    average_salary = df['salary'].mean()
    return jsonify({'average_salary': average_salary})

@app.route('/data/<name>', methods=["GET"])
def get_data_by_name(name):
    person = df[df['name'].str.lower() == name.lower()]
    if not person.empty:
        return jsonify(person.to_dict(orient='records')[0])
    else:
        return jsonify({'error': 'Name not found'}), 404

if __name__ == ' __main__':
    app.run(debug=True)