from nltk import wordnet

animals=wordnet.N['animal'][0].closure(wordnet.HYPONYM, depth=3)
for a in animals:
    print a
#print [word for synset in animals for word in synset if word in wordnet.V]
