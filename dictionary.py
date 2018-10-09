# Dictionaries

# {} for dictionaries, [] for lists.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# print(thisdict)
# print(thisdict["model"])
# print(thisdict.get("model")) # This is cool as it returns "None" if the key is not present (i.e. print(thisdict.get("engine size").
# print(thisdict.get("engine size", 0)) # You can also give it a default value if the key is not present. In this case, the default value would be 0.

# for k in thisdict:
#     print(k) # Gives you keys in thisdict.
    
# for v in thisdict.values():
#     print(v) # Gives you the value in thisdict.
    
for k, v in thisdict.items():
    # print(k) # Gives you keys.
    # print(v) # Gives you values.
    print(k, v) # Gives you keys and values side by side.
    
