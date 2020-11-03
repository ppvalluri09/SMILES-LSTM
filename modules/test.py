import sys
from infer import *

if __name__ == "__main__":
    try:
        cid = str(sys.argv[1])
    except:
        cid = "2000"
    
    predictions = predict(cid)
    print(predictions)
