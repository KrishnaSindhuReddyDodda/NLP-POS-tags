def convert_pos(pos):
    if pos=="CCONJ":
        return "CONJ"
    elif pos=="AUX":
        return "VERB"
    elif pos=="INTJ":
        return "X"
    elif pos=="PART":
        return "PRT"
    elif pos=="PROPN":
        return "NOUN"
    elif pos=="PUNCT":
        return "."
    elif pos=="SCONJ":
        return "ADP"
    elif pos=="SYM":
        return "X"
    else:
        return pos




def get_pos_from_stanza_output(output):
    r=[]
    for s in output.sentences:
        pos=[]
        for w in s.words:
            k=[w.text,convert_pos(w.upos)]
            pos.append(k)
        r.append(pos)
    return r
