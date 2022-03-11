import pickle




data = [
    {'name': 'hkl', 'age': 29},
    {'name': 'hkl1', 'age': 23},
    {'name': 'hkl2', 'age': 26},
]

# save
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)
    
# load
with open('data.pickle', 'rb') as f:
    loaded_data = pickle.load(f)

print(loaded_data)