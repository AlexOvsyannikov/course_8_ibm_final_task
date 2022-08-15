import machinetranslation.translator as translate
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/index')
@app.route('/')
def return_index():
    return render_template('index.html')


@app.route('/englishToFrench')
def en_to_fr():
    text = request.args.get('text')
    return translate.english_to_french(text)


@app.route('/frenchToEnglish')
def fr_to_en():
    text = request.args.get('text')
    return translate.french_to_english(text)


if __name__ == '__main__':
    app.run()