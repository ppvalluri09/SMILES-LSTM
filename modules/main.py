import sys
from infer import predict
from cid_to_smiles import *

test = False

"""
running it:-

python3 main.py {CID(str)} {test(bool)}
"""

if __name__ == "__main__":
    cid = str(sys.argv[1])
    try:
        test = bool(sys.argv[2])
    except:
        test = False
        pass
    print("Testing", test)
    try:
        limit = int(sys.argv[3])
    except:
        limit=-1
        pass
    if test:
        predictions = eval(open("../temp/predictions", "r").read())
        predictions = predictions["predicted_pbdids"]
    else:
        predictions = predict(cid)
        predictions = predictions.get("predicted_pbdids")
        with open("../temp/cid", "w") as f:
            f.write(cid + "\n")
        with open(f"../temp/predicted_pdbids", "w") as f:
            for pred in predictions:
                f.write(pred + "\n")
    predictions = list(set(predictions))
    get_smiles(predictions, cid=cid, limit=limit)
