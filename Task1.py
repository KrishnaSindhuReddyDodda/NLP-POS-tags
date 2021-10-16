import nltk
import stanza
import a1
import accu                       #accu is a file with accuracy().
from nltk.corpus import brown
print(brown.categories())         #This retrieve categories in genre of brown corpus



sent_pos_adventure = nltk.corpus.brown.tagged_sents(categories = "adventure",tagset="universal")
adv=[]
correct_adv_pos=[]
sents=nltk.corpus.brown.sents(categories="adventure")
print("sentences in adventure category...",len(sents))      #gives length of adventure category
for i in range(len(sents)):
    adv.append(sents[i])
pos_tagger=stanza.Pipeline(processors="tokenize,pos",tokenize_pretokenized=True)
output1=pos_tagger(adv)
pos1= a1.get_pos_from_stanza_output(output1)
print(pos1)
correct_pos1=a1.get_pos_from_nltk_tagged_sents(sent_pos_adventure[0:len(sent_pos_adventure)])
for i in range(len(sent_pos_adventure)):
    correct_adv_pos.append(correct_pos1[i])
print()
print()
print("correct pos for adventure catregory ...")
print(correct_adv_pos)
print()
print("accuarcay for adventure category....")
print(accu.accuracy(correct_adv_pos,pos1))
print()
print()


sent_pos_news = nltk.corpus.brown.tagged_sents(categories = "news",tagset="universal")
new=[]
correct_new_pos=[]
sents=nltk.corpus.brown.sents(categories="news")
print("sentences in news category.....",len(sents))        #gives length of news category
for i in range(len(sents)):
    new.append(sents[i])
pos_tagger=stanza.Pipeline(processors="tokenize,pos",tokenize_pretokenized=True)
output2=pos_tagger(new)
pos2= a1.get_pos_from_stanza_output(output2)
print(pos2)
correct_pos2=a1.get_pos_from_nltk_tagged_sents(sent_pos_news[0:len(sent_pos_news)])
for i in range(len(sent_pos_news)):
    correct_new_pos.append(correct_pos2[i])
print()
print()
print("correct pos for news catregory ...")
print(correct_new_pos)
print()
print("accuarcay for news category....")
print(accu.accuracy(correct_new_pos,pos2))
print()
print()

sent_pos_lore = nltk.corpus.brown.tagged_sents(categories = "lore",tagset="universal")
lore=[]
correct_lore_pos=[]
sents=nltk.corpus.brown.sents(categories="lore")
print("sentences in lore category....",len(sents))        #gives length of lore category
for i in range(len(sents)):
    lore.append(sents[i])
pos_tagger=stanza.Pipeline(processors="tokenize,pos",tokenize_pretokenized=True)
output3=pos_tagger(lore)
pos3= a1.get_pos_from_stanza_output(output3)
print(pos3)
correct_pos3=a1.get_pos_from_nltk_tagged_sents(sent_pos_lore[0:len(sent_pos_lore)])
for i in range(len(sent_pos_lore)):
    correct_lore_pos.append(correct_pos3[i])
print()
print()
print("correct pos for lore catregory ...")
print(correct_lore_pos)
print()
print("accuarcay for lore category....")           
print(accu.accuracy(correct_lore_pos,pos3))      #Gives performance of accuracy for each brown corpus categories
