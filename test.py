from datetime import datetime
# from nltk import StanfordPOSTagger
#
# english_postagger = StanfordPOSTagger ( 'C:\Python27\Lib\stanford-pos\models\english-bidirectional-distsim.tagger',
#                                         'C:\Python27\Lib\stanford-pos\stanford-postagger.jar', encoding='utf-8' )
# result = english_postagger.tag('Barak Obama is the president of USA.')
# print result

from nltk import StanfordNERTagger

st = StanfordNERTagger('C:\Python27\Lib\stanford-ner\classifiers\english.conll.4class.distsim.crf.ser.gz',
                       'C:\Python27\Lib\stanford-ner\stanford-ner.jar', encoding='utf-8')
r=st.tag('Obama''wife is the best woman in USA people.'.split())
print(r)




#
# tagger = ner.HttpNER(host='localhost', port=80)
# st = tagger.get_entities('Rami Eid is studying at Stony Brook University in NY')
# print st