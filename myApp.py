from flask import Flask

#check type for vars
def check_type(my_name = None, my_id = None):
    # names should exist
    if not my_name:
        return False
    else:
        if not isinstance(my_name, str):
            raise TypeError('_str must be a string')
        if my_id:
            if not isinstance(my_id, (int, str)):
                return False
            if isinstance(my_id, str):
                if not my_id.isdigit():
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