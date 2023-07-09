from flask import Flask, request, jsonify, render_template
from utils import MobilePrice
import config

app = Flask(__name__)

@app.route('/')
def home():
    
    return jsonify({"Result":"Successful"})

@app.route('/mobile_price_pred')
def home1():

    return render_template('mobile_pred.html')


@app.route('/predict_price',methods = ['GET'])
def predict_price():
    data = request.args.get
    print("Data :",data)
    Sale = eval(data('Sale'))
    weight = eval(data('weight'))
    resoloution = eval(data('resoloution'))
    ppi = eval(data('ppi'))
    cpu_core = eval(data('cpu_core'))
    cpu_freq = eval(data('cpu_freq'))
    internal_mem = eval(data('internal_mem'))
    ram = eval(data('ram'))
    RearCam = eval(data('RearCam'))
    Front_Cam = eval(data('Front_Cam'))
    battery = eval(data('battery'))
    thickness = eval(data('thickness'))

    Obj = MobilePrice(Sale,weight,resoloution,ppi,cpu_core,cpu_freq,internal_mem,ram,RearCam,Front_Cam,battery,thickness)
    pred_price = Obj.get_predicted_price()

    
    
    return render_template('mobile_pred.html', prediction = pred_price)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER, debug=False)