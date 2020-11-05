import os

contents = open("./temp/smiles_cleansed", "r").read().split("\n")
cid = contents[0]
for smile in contents[1:]:
    if smile != "":
        #  command = f'python3 multi_obj_opt.py --model_dir="./models/" --hparams="./mol_dqn/chemgraph/configs/multi_obj_dqn.json" --start_molecule="{cid}" --target_molecule="{smile}" --similarity_weight=0.0'
        command = f'python3 ./target_sas.py --model_dir="./models/" --hparams="./mol_dqn/chemgraph/configs/target_sas.json" --start_molecule="{smile}" --loss_type="l2" --target_sas=2.5'
        os.system(command)
