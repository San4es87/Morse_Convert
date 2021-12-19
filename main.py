from flask import Flask, render_template, request
import alphabet



app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/a', methods=['GET', 'POST'])
def translate():
    text = request.form['text']
    # Convertor Morse
    is_on = True
    while is_on:
        try:
            message = text.upper()
            new_list = [alphabet.encode[letter] for letter in message]
            text = ' '.join(new_list)
            is_on = False
        except KeyError:
            text = "Sorry please only English"
            is_on = False



    return render_template('index.html', text=text)



if __name__ == '__main__':
    app.run(debug=True)