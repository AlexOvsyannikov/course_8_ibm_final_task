"""Flask server"""
from flask import Flask, render_template, request

import machinetranslation.translator as translate

app = Flask(__name__, template_folder='templates')


@app.route('/index')
@app.route('/')
def return_index():
    """Index endpoint"""
    return render_template('index.html')


@app.route('/englishToFrench')
def en_to_fr():
    """Endpoint for en to fr translate"""
    text = request.args.get('text')
    return translate.english_to_french(text)


@app.route('/frenchToEnglish')
def fr_to_en():
    """Endpoint for fr to en translate"""
    text = request.args.get('text')
    return translate.french_to_english(text)


if __name__ == '__main__':
    app.run()
