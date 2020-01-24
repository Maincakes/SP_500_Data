import pickle

# example_dict = {1: 'a', 2: 'd', 3: '3'}
#
# pickle_out = open('dict.pickle', 'wb')
# pickle.dump(example_dict, pickle_out)
# pickle_out.close()

pickle_in = open('dict.pickle', 'rb')
example_dict = pickle.load(pickle_in)

print(example_dict)