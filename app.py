from flask import Flask, render_template, request, jsonify
from sklearn.linear_model import Ridge,Lasso,ElasticNet,RidgeCV,LassoCV,ElasticNetCV,LinearRegression
from sklearn.model_selection import train_test_split
import pickle
from wsgiref import simple_server




app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])  # This will be called from UI

def math_operation():
    try:
        if (request.method=='POST'):
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            num3 = float(request.form['num3'])
            num4 = float(request.form['num4'])
            num5 = float(request.form['num5'])
            num6 = float(request.form['num6'])
            num7 = float(request.form['num7'])
            num8 = float(request.form['num8'])
            num9 = float(request.form['num9'])

            model = pickle.load(open('lasso Linear Regression Homework Model for deployment', 'rb'))
            scaler = pickle.load(open('Scaler for lasso Linear Regression Homework Model for deployment', 'rb'))

            test = [num1, num2, num3, num4, num5, num6, num7, num8, num9]
            #test = [308.6, 1551, 42.8, 0, 0, 0, 0, 0, 0]
            test = scaler.transform([test])
            result = model.predict(test)

            return render_template('results.html',result=result)
    except Exception as e:
        return render_template('results.html',result=f"Something Went wrong {e}")
"""
@app.route('/add')
def add():
    test1=request.args.get('val1')
    test2=request.args.get('val2')
    test3=int(test1)+int(test2)
    return '''<h1>My result is :{}/<h1>'''.format(test3)
"""
"""
if __name__ == '__main__':
    #app.run()
    port = int(os.getenv("PORT"))
    host = '0.0.0.0'
    httpd = simple_server.make_server(host=host, port=port, app=app)
    httpd.serve_forever()

"""
if __name__ == '__main__':
    #app.run()
    app.run(debug=True)