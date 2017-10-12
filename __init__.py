from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template("dashboard.html")

#@app.route('/dashboard/')
#def dashboard():
    #return render_template("dashboard.html")

@app.route('/dashboardodd/')
def dashboardodd():
    return render_template("dashboardodd.html")

@app.route('/loadFiles', methods=['GET','POST'])
def loadFiles():
	#if request.method == 'POST':
	#	return redirect(url_for('dashboard'))
	return render_template("loadFiles.html")

@app.route('/TransformData', methods=['GET','POST'])
def TransformData():
	return render_template("TransformData.html")

@app.route('/FFT_Preview', methods=['GET','POST'])
def FFT_Preview():
	return render_template("FFT_Preview.html")

@app.route('/Configure', methods=['GET','POST'])
def Configure():
	return render_template("Configure.html")

@app.route('/Result', methods=['GET','POST'])
def Result():
	return render_template("Result.html")




if __name__ == "__main__":
    app.run()
