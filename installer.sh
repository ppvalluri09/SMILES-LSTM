git clone https://github.com/ppvalluri09/SMILES-LSTM/
mv SMILES-LSTM/* ./
rm -rf SMILES-LSTM

git clone https://github.com/rdkit/rdkit
git clone https://github.com/openai/baselines.git

wget -c https://repo.continuum.io/miniconda/Miniconda3-py37_4.8.3-Linux-x86_64.sh
chmod +x Miniconda3-py37_4.8.3-Linux-x86_64.sh
time bash ./Miniconda3-py37_4.8.3-Linux-x86_64.sh -b -f -p /usr/local
time conda install -q -y -c conda-forge rdkit

pip install absl-py
pip install gym
pip install scipy

git clone https://github.com/topazape/LSTM_Chem
pip install -q bunch
pip install -r "./SMILES-LSTM/LSTM_Chem/requirements.txt"
