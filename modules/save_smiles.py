from cid_to_smiles import *

def main(pbdids):
    smiles = get_smiles(pdbids)
    with open("../temp/extracted_smiles", "w") as f:
        for smile in smiles:
            f.write(smile + "\n")

if __name__ == "__main__":
    with open("../temp/pdbids_predicted", "r") as f:
        pdbids = [pdbid.rstrip() for pdbid in f]
        print("Predicted PDBIDS", pdbids)
        main(pdbids)
