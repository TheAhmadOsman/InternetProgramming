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
    return render_template("base.html",
                           myDict = myDict,
                           nums = nums)

@app.route("/form")
def formControl():
    args = request.args
    num = request.args["numCount"]
    num = int(num)
    nums = []
    for i in range(num):
        nums.append(i+1)
    return render_template("chooseNums.html",
                            target = num,
                            numList = nums)


if __name__ == "__main__":
    app.run(debug=True)
