from flask import Flask, render_template, request

app = Flask(__name__)

#@app.route("/",)
#def index():
#    return render_template('index.html', developer_name = 'E2014_Devin', not_valid = False)
    
@app.route("/", methods = ['GET', 'POST'])
def index_post():

    if request.method == 'GET':
        return render_template('index.html', developer_name = 'E2014_Devin', not_valid = False)

    else:
        number = request.form['number']
        
        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        numset = set(number)
        lennum1 = len(numset - digits)
        if lennum1 > 0:
            return render_template('index.html', developer_name = 'E2014_Devin', not_valid = True )

        number = int(number)
        if number <= 0:
            return render_template('index.html', developer_name = 'E2014_Devin', not_valid = True)
    
        else:
            number = int(number)       
            numhour = number // 3600000
            nummin = (number - (numhour * 3600000)) // 60000
            numsecond = (number - ((numhour * 3600000) + (nummin * 60000))) // 1000

            numhourst = str(numhour)
            numminst = str(nummin)
            numsecondst = str(numsecond)
            numberst = str(number)

            res = bool(numhour) * numhourst + bool(numhour) * " hour/s " + bool(nummin) * numminst + bool(nummin) * " minute/s " + bool(numsecond) * numsecondst + bool(numsecond) * " second/s " + bool(not(numhour or nummin or numsecond)) * numberst + bool(not(numhour or nummin or numsecond)) * " milisecond/s "
            
            return render_template("result.html", developer_name = 'E2014_Devin', milliseconds = number, result = res)
            
if __name__ == '__main__':
    app.run(debug = True)
    #app.run(host='0.0.0.0', port=80)