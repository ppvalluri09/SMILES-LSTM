import numpy as np
import matplotlib.pyplot as plt
import os
import argparse

from lstm_chem.utils.config import process_config
from lstm_chem.model import LSTMChem
from lstm_chem.generator import LSTMChemGenerator

from rdkit import RDLogger, Chem, DataStructs
from rdkit.Chem import AllChem, Descriptors

RDLogger.DisableLog("rdApp.*")

def get_valid_molecules(smiles: list) -> list:
    valid_mols = []
    for smi in smiles:
        mol = Chem.MolFromSmiles(smi)
        if mol is not None:
            valid_mols.append(mol)
    print("Percentage of Valid Molecules, out of", len(smiles), "generated smiles:", f"{(len(valid_mols)/len(smiles))*100} %")
    valid_smiles = [Chem.MolToSmiles(mol) for mol in valid_mols]
    return valid_mols, valid_smiles

def save_to_file(smiles:list, filename:str):
    try:
        with open(f"../temp/{filename}.smi", "w") as f:
            for smi in smiles:
                f.write(smi + "\n")
    except Exception as e:
        print("[ERROR]", str(e))

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--model_dir", type=str, help="Directory of the saved model", default=os.listdir("./experiments")[-1])
    parser.add_argument("--num_samples", type=int, help="Num of samples to be generated", default=30000)

    args = parser.parse_args()
    MODEL_DIR = args.model_dir
    num_samples = args.num_samples

    CONFIG_FILE = f"./experiments/{MODEL_DIR}/LSTM_Chem/config.json"
    config = process_config(CONFIG_FILE)

    modeler = LSTMChem(config, session="generate")

    generator = LSTMChemGenerator(modeler)
    sampled_smiles = generator.sample(num=num_samples)

    valid_mols, valid_smiles = get_valid_molecules(sampled_smiles)
    save_to_file(valid_smiles, "generated_smile")
