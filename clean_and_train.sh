if [ ! -f ./temp/smiles_cleansed.smi ]; then
  python3 "./LSTM_Chem/cleanup_smiles.py" "./temp/extracted_smiles" "./temp/smiles_cleansed.smi"
else
  echo "File found, replacing old file"
  rm ./temp/smiles_cleansed.smi
  python3 "./LSTM_Chem/cleanup_smiles.py" "./temp/extracted_smiles" "./temp/smiles_cleansed.smi"
fi

cd LSTM_Chem
python3 train.py
cd ..
