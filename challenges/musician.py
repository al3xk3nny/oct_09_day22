# Create a dictionary to represent a musician. The musician has a name, nationality, instrument, proficiency (1-100)

# musician = {
#     "name": "Dave",
#     "nationality": "American",
#     "instrument": "guitar",
#     "proficiency": 75
# }

# Now create a list, using the dictionary using the Beatles.

# beatles = [
#     {
#     "name": "John",
#     "nationality": "American",
#     "instrument": "guitar",
#     "proficiency": 100
#     },
#     {
#     "name": "Paul",
#     "nationality": "American",
#     "instrument": "bass",
#     "proficiency": 55
#     },
#     {
#     "name": "George",
#     "nationality": "American",
#     "instrument": "guitar",
#     "proficiency": 65
#     },
#     {
#     "name": "Ringo",
#     "nationality": "American",
#     "instrument": "drums",
#     "proficiency": 55
#     }
#     ]
    
# Now loop through the Beatles and print their names.

# for b in beatles:
#     print(b.get("name"))
    
# IMPORTANT; Lists are looked up by position. Dictionaries are looked up by name.

# Now turn into a dictionary and give each sub dictionary a name. Then nest a list in one of the key:vales.

# beatles = {
#     "john": {
#         "name": "John",
#         "nationality": "American",
#         "instruments":  [
#                         {"instrument": "guitar", "proficiency": 45},
#                         {"instrument": "drums", "proficiency": 55}
#                         ]
#     },
#     "paul": {
#         "name": "Paul;",
#         "nationality": "American",
#         "instruments":  [
#                         {"instrument": "bass", "proficiency": 55},
#                         {"instrument": "guitar", "proficiency": 35}
#                         ]
#     },
#     "george": {
#         "name": "George",
#         "nationality": "American",
#         "instruments":  [
#                         {"instrument": "guitar", "proficiency": 75},
#                         {"instrument": "drums", "proficiency":25}
#                         ]
#     },
#     "ringo": {
#         "name": "ringo",
#         "nationality": "American",
#         "instruments":  [
#                         {"instrument": "drums", "proficiency": 55},
#                         {"instrument": "guitar", "proficiency": 45}
#                         ]
#     }
# }

# Now find the proficiency of paul's guitar playing.

# print(beatles["paul"]["instruments"][1].get("proficiency", 0))

# ...we have a problem. We need to know that guitar is at position index 1. How do we solve this problem.

# ...we need to change the inner list to a dictionary and assign keys and values.

beatles = {
    "john": {
        "name": "John",
        "nationality": "American",
        "instruments":  {
                        "guitar": 45,
                        "drums": 55
                        }
    },
    "paul": {
        "name": "Paul;",
        "nationality": "American",
        "instruments":  {
                        "bass": 55,
                        "guitar": 35
                        }
    },
    "george": {
        "name": "George",
        "nationality": "American",
        "instruments":  {
                        "guitar": 75,
                        "drums": 25
                        }
    },
    "ringo": {
        "name": "ringo",
        "nationality": "American",
        "instruments":  {
                        "drums": 55,
                        "guitar": 45
                        }
    }
}

# print(beatles["paul"]["instruments"].get("guitar", 0))

# Printing proficiency in all instruments.

# paul = beatles["paul"]
# pauls_instruments = paul["instruments"]
# for i, p in pauls_instruments.items():
#     print("Paul's skill level with the {0} is {1}".format(i, p))
#     print("----")

# Printing proficiency in all instruments with default 0. In other words, what if the musician doesn't play the guitar.

# musician = beatles["ringo"]
# instruments = musician["instruments"]
# guitar_prof = instruments.get("guitar", 0)
# print(guitar_prof)

# ...we can also access this data via a function.

def show_instrument_proficiency(name):
    musician = beatles[name]
    instruments = musician["instruments"]
    
    print(musician['name'])
    print("----------")
    for i, p in instruments.items():
        print("Proficiency in {0} is {1}".format(i, p))    
    
show_instrument_proficiency("george")