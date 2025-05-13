def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    textlower = text.lower()
    chardict = {}
    for char in textlower:
        if char in chardict:
            chardict[char] += 1
        else:
            chardict[char] = 1
    return chardict
    

def sort_on_num(dict):
    return dict["num"]

def sort_char_count(char_count):
    charlist = []
    for key in char_count:
        charlist.append({"char": key, "num": char_count[key]})
    charlist.sort(reverse=True, key=sort_on_num)
    return charlist