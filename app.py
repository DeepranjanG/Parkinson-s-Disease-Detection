
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            mdvp_fo=float(request.form['mdvp_fo'])
            mdvp_fhi=float(request.form['mdvp_fhi'])
            mdvp_flo=float(request.form['mdvp_flo'])
            mdvp_jitper=float(request.form['mdvp_jitper'])
            mdvp_jitabs=float(request.form['mdvp_jitabs'])
            mdvp_rap=float(request.form['mdvp_rap'])
            mdvp_ppq=float(request.form['mdvp_ppq'])
            jitter_ddp=float(request.form['jitter_ddp'])
            mdvp_shim=float(request.form['mdvp_shim'])
            mdvp_shim_db=float(request.form['mdvp_shim_db'])
            shimm_apq3=float(request.form['shimm_apq3'])
            shimm_apq5=float(request.form['shimm_apq5'])
            mdvp_apq=float(request.form['mdvp_apq'])
            shimm_dda=float(request.form['shimm_dda'])
            nhr=float(request.form['nhr'])
            hnr=float(request.form['hnr'])
            rpde=float(request.form['rpde'])
            dfa=float(request.form['dfa'])
            spread1=float(request.form['spread1'])
            spread2=float(request.form['spread2'])
            d2=float(request.form['d2'])
            ppe=float(request.form['ppe'])

            
            filename = 'modelForPrediction.sav'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            scaler = pickle.load(open('standardScalar.sav', 'rb'))
            prediction=loaded_model.predict(scaler.transform([[mdvp_fo,mdvp_fhi,mdvp_flo,mdvp_jitper, mdvp_jitabs,
                mdvp_rap,mdvp_ppq, jitter_ddp, mdvp_shim, mdvp_shim_db,shimm_apq3,shimm_apq5,mdvp_apq,shimm_dda,nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe]]))
            print('prediction is', prediction)
            if prediction == 1:
                pred = "You have Parkinson's Disease. Please consult a specialist."
            else:
                pred = "You are Healthy Person."
            # showing the prediction results in a UI
            return render_template('results.html',prediction=pred)
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app