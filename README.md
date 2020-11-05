# SMILES-LSTM

SMILES LSTM

# Instructions to run

1. Extracting SMILES
  ```python3 modules/main.py <cid>```
2. Cleaning the SMILES and Training the LSTM network
  ```sh run.sh```

Checklist
  - [x] Extract the SMILES format for each CID associated with predicted targets PDBIDS
  - [x] Clean the extracted SMILES 
  - [x] Train the LSTM network
  - [x] Sample new SMILES from the trained LSTM network and save them
  - [ ] Train the RL model
  - [x] Use the samples SMILES as the target molecule to the RL model with the start molecule being the input CID
  - [ ] Examine the output of the RL model
