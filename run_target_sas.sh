#!/bin/bash
filename='./SMILES-LSTM/temp/smiles_cleansed'
n=1
while read line; do
  if [ $n -ge 2 ]
  then
    python3 ./mol_dqn/chemgraph/target_sas.py --model_dir="./save" --hparams="./mol_dqn/chemgraph/configs/target_sas.json" --start_molecule="$line" --loss_type="l2" --target_sas=2.5
  fi
  n=$((n+1))
done < $filename

