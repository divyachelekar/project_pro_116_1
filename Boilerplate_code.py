#Importing flask module in the project
from flask import Flask , render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/")

#‘/’ URL is bound with first_flask function.
def first_flask():

    return "This is my first flask program"
@app.route("/me")

def myself():
    name="Divya"
    age="14"
    return render_template('index.html' , name=name , age=age)

@app.route("/father")
def father():
    father_name="Devidas"
    father_age="45"
    return render_template("father.html" , father_name=father_name , father_age=father_age)

@app.route("/mother")

def mother():
    name="Swapna"
    age="37"
    return render_template('mother.html' , mother_name=name , mother_age=age)

@app.route("/friend")

def friend():
    name="Chetana"
    age="7"
    return render_template('friend.html' , friend_name=name , friend_age=age)


#run the application on local server
if __name__ =="__main__":
    app.run(debug=True)
