mv generate.py ./LSTM_Chem/
cd ./LSTM_Chem
python3 ./generate.py --num_samples=30000
mv generate.py ../
cd ..
