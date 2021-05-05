import pandas as pd

data = pd.read_csv("d:/AtPolyDB/genotype.ped", sep=' ', header=None, engine = 'python',iterator=True)

loop = True
chunkSize = 100
chunks = []
index=0
while loop:
    try:
        print(index)
        chunk = data.get_chunk(chunkSize)
        chunks.append(chunk)
        index+=1

    except StopIteration:
        loop = False
        print("Iteration is stopped.")
print('Merge Chunks Start')
data = pd.concat(chunks, ignore_index= True)
print('Merge Chunks End')
data = data.drop(data.columns[[5]], axis=1)
e=data.iloc[:7,:7]
print(e)

print('Read Phenotype Start')
first_column = pd.read_csv('C:/AtPolyDB/phenotypes.pheno', header='infer', usecols=['FT10'], sep=' ')##FT10 can be chenged to Emco5

print(first_column)
idx = 5
print('Insert Phenotype')
data.insert(loc=idx,column='FT10',value=first_column)##column='phenotype name'
f=data.iloc[:7,:7]
print(f)
print('Write Genotype')
data.to_csv('d:/AtPolyDB/genotype_with_FT10.ped', sep=' ', header=None, index=None, na_rep='NaN')
print('Write Genotype End')