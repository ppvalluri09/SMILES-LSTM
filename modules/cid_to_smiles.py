import sqlite3
import pandas as pd
import pubchempy as pc
from tqdm import tqdm
from collections import OrderedDict

def get_smiles(pdbids, cid=None):
    connection = sqlite3.connect("../../automated_in_silico_identification/build2/DB/drugs.db")
    df = pd.read_sql('SELECT * from drugs_interaction_processed;', connection)
    df = df[df["pbdid"].isin(pdbids)]
    cids = []
    if cid is not None:
        cids += [cid]
    cids += df["cid"].unique().tolist()
    print("Converting,", len(cids), "CIDs, to SMILES format")
    with open("../temp/extracted_smiles", "w") as f:
        for cid in tqdm(cids[:10], total=len(cids[:10]), leave=True):
            f.write(pc.Compound.from_cid(cid).canonical_smiles + "\n")
