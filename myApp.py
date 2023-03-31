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
            if not (isinstance(my_id, int) or (isinstance(my_id, str) and my_id.isdigit())):
            #if not (isinstance(my_id, int)):
                return False
        return True

def check_name(my_name = None):
    # names should exist
    if not my_name:
        return False
    else:
        if not isinstance(my_name, str):
            raise TypeError('_str must be a string')
        if (my_name[-1] == ' '):
            return False
        if (not my_name.isprintable):
            return False
        return True

def check_name_len(my_name = None):
    # names should exist
    if not my_name:
        return False
    else:
        if not isinstance(my_name, str):
            raise TypeError('_str must be a string')
        if (len(my_name.encode('utf-8'))>20):
            return False
        return True

def check_sid_len(my_id = None):
    # names should exist
    if not my_id:
        return False
    if my_id:
        #check if string !10 chracter
        if (len(str(my_id))!=10):
            return False
        #check if contain space 
        if (not  str(my_id).isdigit()):
            return False
        if not (isinstance(my_id, int) or (isinstance(my_id, str) and my_id.isdigit())):
        #if not (isinstance(my_id, int)):
            return False
        #check length of the id
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
    app.run()
