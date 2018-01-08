import nltk
def ie_preprocess(document):
    result=[]
    with open(document, 'r', encoding='latin2') as f:
        for l in f:
            result=l.strip()
            #print(result)
            sentences1 = nltk.sent_tokenize(result)
            sentences2 = [nltk.word_tokenize(sent) for sent in sentences1]
            sentences3 = [nltk.pos_tag(sent) for sent in sentences2]
            #return (sentences3)
            final_result=[]
            for s in sentences3:
                grammar = "NP: {<DT>?<JJ>*<NN>}"
                cp = nltk.RegexpParser(grammar)
                final_result.append(cp.parse(s))
            return (final_result)

#going to try using unigram chunker:
class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
                      for sent in train_sents]
        self.tagger = nltk.UnigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                     in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)

#evaluation result using UnigramChunker - testing on sample text
test_sents = (ie_preprocess_test('/Users/chidam/Desktop/Uganda-sample-testing.txt'))
train_sents = (ie_preprocess('/Users/chidam/Desktop/Africa-sample-training.txt'))
unigram_chunker = UnigramChunker(train_sents)
print(unigram_chunker.evaluate(test_sents))

#sentence.leaves - for training data - verifying tags on leaves
postags = sorted(set(pos for sent in train_sents for (word,pos) in sent.leaves()))
print(unigram_chunker.tagger.tag(postags))
