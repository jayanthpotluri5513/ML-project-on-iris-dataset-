from flask import Flask, render_template,request
import pickle
app=Flask(__name__)
model=pickle.load(open('irisdata.sav','rb'))

@app.route('/')
def home():
    return render_template('home.html', result=None)


@app.route('/predict',methods=['POST', 'GET'])
def predict():
   try:
      sepal_length = float(request.form['sepal_length'])
      sepal_width = float(request.form['sepal_width'])
      petal_length = float(request.form['petal_length'])
      petal_width =float( request.form['petal_width'])
   except ValueError:
     return render_template('home.html', result=None)
   
   result=model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
   return render_template('home.html', result=result[0])
if __name__=='__main__':
    app.run(debug=True)
