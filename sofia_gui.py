from flask import Flask,render_template,request
from sofia_deducer import LogicalStructure

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("sofia.html",solved=False)   

@app.route('/proof',methods=['POST'])
def proof():
    theorem = request.form["theorem"]
    lg = LogicalStructure()
    lg.extract(theorem)
    return render_template("sofia.html",solved=True,assumptions=lg.assumptions,conclusions=lg.conclusions)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug = True)
