import pickle as pkl

f_x = open('data/ind.citeseer.test.index', 'rb')
data = pkl.load(f_x, encoding='latin1')

print(data)