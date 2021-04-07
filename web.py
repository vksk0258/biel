from flask import Flask, render_template, request

from xgboost import XGBRegressor
from xgboost import plot_importance, plot_tree
from sklearn.model_selection import train_test_split
import pandas as pd

def create_app():
    app = Flask(__name__)

    from sklearn.metrics import mean_squared_error


    @app.route("/", methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            return render_template('index.html')
        if request.method == 'POST':
            max_tem = float(request.form['max_tem'])
            tem_rate = float(request.form['tem_rate'])
            height = float(request.form['height'])
            length = float(request.form['length'])
            width = float(request.form['width'])
            W_top = float(request.form['W_top'])
            W_side = float(request.form['W_side'])
            W_bottom = float(request.form['W_bottom'])
            tem_initial = float(request.form['tem_initial'])
            tem_out = float(request.form['tem_out'])
            location = str(request.form['location'])

            df = pd.read_csv('biel_train.csv')
            validation = pd.read_csv('biel_validation.csv')
            validation = validation[0:280]

            df = df.dropna()
            df = df.drop(['shape'], axis=1)                           
            validation = validation.drop(['shape'], axis=1)

            validation['max_tem'] = max_tem
            validation['tem_rate'] = tem_rate
            validation['height'] = height
            validation['length'] = length
            validation['width'] = width
            validation['W_top'] = W_top
            validation['W_side'] = W_side
            validation['W_bottom'] = W_bottom
            validation['tem_initial'] = tem_initial
            validation['tem_out'] = tem_out
            validation['location'] = location

            df = df[df['location'] == location]

            df = df.drop(['location'], axis=1)
            validation = validation.drop(['location'], axis=1)

            columns = list(df.columns.values)
            columns.remove('y_temp')

            v_columns = list(validation.columns.values)
            v_columns.remove('y_temp')

            X_train = df[columns]
            y_train = df[['y_temp']]

            model = XGBRegressor(n_estimators=400) # 트리 개수 400개로 모델 생성
            model.fit(X_train, y_train)

            temp_data = validation[v_columns]
            temp = model.predict(temp_data)
                
            
        return render_template('index.html', temp=temp, max_tem=max_tem, tem_rate=tem_rate, height=height, length=length, width=width, W_top=W_top, W_side=W_side, W_bottom=W_bottom, tem_initial=tem_initial, tem_out=tem_out, location=location)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')

   