def string(str_list):
    longest_length = 0
    for word in str_list:
        if len(word) > longest_length:
            longest_length = len(word)
    if len(word) == longest_length:
        print(word)
string(['Goa', 'G.O.A.T'])