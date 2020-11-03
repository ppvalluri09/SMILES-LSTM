import sys
from infer import predict

test = False

if __name__ == "__main__":
    cid = str(sys.argv[1])
    if test:
        predictions = dict(open("../temp/predictions", "r").read())
        predictions = predictions["predicted_pbdids"]
    else:
        predictions = predict(cid)
        with open("../temp/predictions", "w") as f:
            f.write(predictions)
        predictions = predictions.get("predicted_pbdids", [])

        with open("../temp/cid", "w") as f:
            f.write(cid + "\n")
    with open(f"../temp/predicted_pdbids", "w") as f:
        for pred in predictions:
            f.write(pred + "\n")
    get_smiles(predictions, cid=cid)
