from flask import Flask, render_template, request, url_for, redirect
import joblib
import pandas as pd


# load our model file
model = joblib.load('model.xgb')
scale = joblib.load('Scalized.scl')

# Object for Flask
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':

        # GET ALL DATA AND SCALIZED

        age = request.form['age']

        sex = int(request.form['sex'])

        TSH_measured = int(request.form['TSH measured'])

        if TSH_measured == 0:
            TSH = 0
        else:
            TSH = request.form['TSH']

        T3_measured = int(request.form['T3 measured'])

        if T3_measured == 0:
            T3 = 0
        else:
            T3 = request.form['T3']

        TT4_measured = int(request.form['TT4 measured'])

        if TT4_measured == 0:
            TT4 = 0
        else:
            TT4 = request.form['TT4']

        T4U_measured = int(request.form['T4U measured'])

        if T4U_measured == 0:
            T4U = 0
        else:
            T4U = request.form['T4U']

        FTI_measured = int(request.form['FTI measured'])

        if FTI_measured == 0:
            FTI = 0
        else:
            FTI = request.form['FTI']

        # 2. create DataFrame
        data = [[age, sex, TSH_measured, TSH, T3_measured, T3, TT4_measured, TT4, T4U_measured, T4U, FTI_measured, FTI]]
        column_name = ['age', 'sex', 'TSH_measured', 'TSH', 'T3_measured', 'T3', 'TT4_measured', 'TT4', 'T4U_measured',
                       'T4U', 'FTI_measured', 'FTI']

        data_model = pd.DataFrame(data, columns=column_name)

        # scalized
        num_col = ['age', 'TSH', 'T3', 'TT4', 'T4U', 'FTI']
        data_model[num_col] = scale.transform(data_model[num_col])

        # Prediction
        result = model.predict(data_model)[0]

        # 3. Display
        if result == 0:
            return render_template('index.html', Thyroid_Text='Have Hyperthyroidism')
        elif result == 1:
            return render_template('index.html', Thyroid_Text='Have Hypothyroidism')
        else:
            return render_template('index.html', Thyroid_Text='Thyroid Negative')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
