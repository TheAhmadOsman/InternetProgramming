from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    myDict = {}
    myDict["egg"] = "hatched"
    myDict["Jon Snow"] = "incest"
    nums = []
    for i in range(25):
        nums.append(i+1)
    return render_template("index.html", myDict = myDict, nums = nums)

if __name__ == "__main__":
    app.run(debug=True)