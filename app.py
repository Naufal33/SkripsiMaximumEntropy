from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/preprocessing')
def preprocessing():
    return render_template('preprocessing.html')

@app.route('/vectorizer')
def vectorizer():
    return render_template('vectorizer.html') 

@app.route('/training')
def training():
    return render_template('training.html') 

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')  

if __name__ == '__main__':
    app.run(debug=True)