#!/bin/bash
filename='./SMILES-LSTM/temp/smiles_cleansed'
n=1
while read line; do
  if [ $n -eq 1 ] 
  then
    cid=$line
  else
    python ./SMILES-LSTM/mol_dqn/chemgraph/multi_obj_opt.py --model_dir="./save" --hparams="./SMILES-LSTM/mol_dqn/chemgraph/configs/multi_obj_dqn.json" --start_molecule="$cid" --target_molecule="$line" --similarity_weight=0.0 
  fi
  n=$((n+1))
done < $filename
