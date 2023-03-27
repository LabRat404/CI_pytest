from flask import Flask

def check_type(my_name = None, my_id = None):
    # names should exist
    if not my_name:
        return False
    return True

# imagine these data is from db
myName = "Yeung Tang"
myId = "1155144676" 
### end of data

app = Flask(__name__)

@app.route("/")
def hello_world():
    if check_type(myName, myId):
        return f"<p> Hello, my name is {myName}, my sid is {myId}</p>"
    else:
        return f"<p> Hello, my name is unknow, my sid is unknow</p>"
if __name__ == "__main__":
    app.run(debug=True)