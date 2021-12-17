from flask import Flask, render_template, request



app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/a', methods=['GET', 'POST'])
def translate():
    alphabet_morse = {"A": ".-",
                      "B": "-...",
                      "C": "-.-.",
                      "D": "-..",
                      "E": ".",
                      "F": "..-.",
                      "G": "--.",
                      "H": "....",
                      "I": "..",
                      "J": ".---",
                      "K": "-.-",
                      "L": ".-..",
                      "M": "--",
                      "N": "-.",
                      "O": "---",
                      "P": ".--.",
                      "Q": "--.-",
                      "R": ".-.",
                      "S": "...",
                      "T": "-",
                      "U": "..-",
                      "V": "...-",
                      "W": ".--",
                      "X": "-..-",
                      "Y": "-.--",
                      "Z": "--..",
                      "0": "-----",
                      "1": ".----",
                      "2": "..---",
                      "3": "...--",
                      "4": "....-",
                      "5": ".....",
                      "6": "-....",
                      "7": "--...",
                      "8": "---..",
                      "9": "----.",
                      " ": "  "}
    q = request.form['text']
    # Convertor Morse
    is_on = True
    while is_on:
        message = q.upper()
        try:
            new_list = [alphabet_morse[letter] for letter in message]
            q = ' '.join(new_list)
            is_on = False
        except KeyError:
            print("Sorry please only English")
            is_on = False

    return render_template('index.html', q=q)



if __name__ == '__main__':
    app.run(debug=True)