import sqlite3
import pandas as pd
import pubchempy as pc
from tqdm import tqdm
from collections import OrderedDict
import os

def get_smiles(pdbids, cid=None, limit=-1):
    connection = sqlite3.connect("../../automated_in_silico_identification/build2/DB/drugs.db")
    df = pd.read_sql('SELECT * from drugs_interaction_processed;', connection)
    df = df[df["pbdid"].isin(pdbids)]
    cids = []
    if cid is not None:
        cids += [cid]
    cids += df["cid"].unique().tolist()
    if limit == -1:
        limit = len(cids) + 1
    print("Converting,", len(cids), "CIDs, to SMILES format")
    if os.path.isfile("../temp/extracted_smiles"):
        print("File found, replacing existing file")
        os.system("rm ../temp/extracted_smiles")
    with open("../temp/extracted_smiles", "w") as f:
        for cid in tqdm(cids[:limit], total=len(cids[:limit]), leave=True):
            f.write(pc.Compound.from_cid(cid).canonical_smiles + "\n")
