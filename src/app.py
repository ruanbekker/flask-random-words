from flask import Flask, jsonify
from randomword import RandomWord

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

rw = RandomWord()

def get_random_word():
    result = rw.get()
    return result

@app.route('/', methods=['GET'])
def root():
    response = get_random_word()
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
