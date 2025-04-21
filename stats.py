def num_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    character_count = {}
    for char in text:
        if char.lower() in character_count:
            character_count[char.lower()] +=1
        else:
            character_count[char.lower()] = 1
    return character_count

def get_count(dict):
    return dict["count"]

def char_sort(dict):
    #takes the dictionary of character counts and creates
    # a list of dictionaries with 2 pairs: character and count
    char_list = []
    for a in dict:
        char_list.append({"character":a, "count":dict[a]})
    char_list.sort(reverse= True,  key = get_count)
    return char_list

