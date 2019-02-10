from flask import Flask , render_template

app = Flask(__name__)
@app.route('/',methods=["GET"])
def index():
	names = {'name':'rebecca'}
	return render_template("layout.html",names=names,lang = "english",l=True)
             

if __name__ == '__main__':
	app.run(debug=True)