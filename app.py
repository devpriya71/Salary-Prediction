from flask import Flask,request,jsonify
import pickle
# create flask app
app=Flask(__name__)
# load the train model from model.pkl file
model=pickle.load(open('model.pkl','rb'))
# home route (just to check if api is running)
@app.route('/')
def home():
    return "API running!"
@app.route('/predict',methods=['POST'])
def predict():
    data=request.json
    exp=data['experience']
    result=model.predict([[exp]])
    return jsonify({
        "salary": int(result[0])
    })
if __name__ =="__main__":
    app.run(debug=True)