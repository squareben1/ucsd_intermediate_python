
def isInt(string):
    try: 
        if isinstance(int(string), int):
            return True
    except:
        return False 
