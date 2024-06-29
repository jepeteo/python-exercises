import pickle
import json

tDictionary = {
    "1": "A",
    "2": "B",
    "3": "C"
}

# json solution
def save_dict_json(dict_to_save, file_path):
    with open(file_path, 'w') as f:
        json.dump(dict_to_save, f)

def load_dict_json(file_path):
    with open(file_path) as f:
        return json.load(f)

# pickle solution | proposed by instructor | save files in binary mode using pickle | TODO: check more about this
def save_dict_binary(dict_to_save, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(dict_to_save, f)
        
def load_dict_binary(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)



save_dict_json(tDictionary, "test_dictionary.json")
print(load_dict_json("test_dictionary.json"))

save_dict_binary(tDictionary,"test_dictionary.pickle")
print(load_dict_binary("test_dictionary.pickle"))