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

            res = ""
            x = [numhour, nummin, numsecond]
            y = [" hour/s ", " minute/s ", " second/s "]
            for i in range (0, 3):
                res += bool(x[i]) * (str(x[i]) + y[i])
            
            if res == "":
                res = str(number) + " milisecond/s" 
            #res = res + (bool(not(numhour or nummin or numsecond)) * (str(number) + " milisecond/s "))
            
            return render_template("result.html", developer_name = 'E2014_Devin', milliseconds = number, result = res)
            
if __name__ == '__main__':
    app.run(debug = True)
    #app.run(host='0.0.0.0', port=80)