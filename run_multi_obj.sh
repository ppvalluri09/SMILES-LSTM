#!/bin/bash
generated_file='./temp/generated_smile.smi'
cid_smile="./temp/smiles_cleansed.smi"
n=1
while read line; do
  if [ $n -eq 1 ]; then
    cid=$line
  fi
  n=$((n+1))
done < $cid_smile

cd mol_dqn/chemgraph
while read line; do
    python ./multi_obj_opt.py --model_dir="./save" --hparams="./mol_dqn/chemgraph/configs/multi_obj_dqn.json" --start_molecule="$cid" --target_molecule="$line" --similarity_weight=0.0 
done < $generated_file
