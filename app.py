from flask import Flask, render_template
import finalcode 

app = Flask(__name__)

@app.route('/')
def dynamic_page():
    finalcode.printSentences()
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
