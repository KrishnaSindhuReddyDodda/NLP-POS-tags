import nltk
import stanza
import a2                        #a2 is a file with get_pos_from_stanza_output(output1) that produces text and pos tag as an output
s1="I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn't really happy"
s2="Time after time"
s3="It is what it is"
s4="Researchers have investigated this issue for some time"
s5="Fear leads to anger; anger leads to hatred; hatred leads to conflict; conflict leads to suffering"

s1=s1.split(" ")
s2=s2.split(" ")
s3=s3.split(" ")
s4=s4.split(" ")
s5=s5.split(" ")

s=[s1,s2,s3,s4,s5]              #inserting all list(sentences) into another list
pos_tagger=stanza.Pipeline(processors="tokenize,pos",tokenize_pretokenized=True)
output1=pos_tagger(s)
pos1= a2.get_pos_from_stanza_output(output1)
print(pos1)
