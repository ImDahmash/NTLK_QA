import nltk
from nltk.tag import StanfordPOSTagger

def pos_person_tagging(sentence):

    #Setting the path and jar files for the POS Tagger

    # english_postagger=StanfordPOSTagger('stanford-postagger-2014-08-27/models/english-bidirectional-distsim.tagger','stanford-postagger-2014-08-27/stanford-postagger.jar')
    english_postagger = StanfordPOSTagger ( 'C:\Python27\Lib\stanford-pos\models\english-bidirectional-distsim.tagger',
                             'C:\Python27\Lib\stanford-pos\stanford-postagger.jar', encoding='utf-8' )
    NP_list=[]

    POS_list=english_postagger.tag(sentence.split())

    for i in range(0, len(POS_list)):
        if POS_list[i][1] in ['NNS','NNP','NNPS']:
            NP_list.append(POS_list[i][0])


    return NP_list



def pos_noun_tagging(sentence):

    #Setting the path and jar files for the POS Tagger

    english_postagger=StanfordPOSTagger( 'C:\Python27\Lib\stanford-pos\models\english-bidirectional-distsim.tagger',
                             'C:\Python27\Lib\stanford-pos\stanford-postagger.jar', encoding='utf-8' )
    NP_list=[]

    POS_list=english_postagger.tag(sentence.split())

    for i in range(0, len(POS_list)):
        if i==0:
            if POS_list[i][1] in ['JJ']:
                NP_list.append(POS_list[i][0])
        if POS_list[i][1] in ['NN','NNS','NNP','NNPS']:
            NP_list.append(POS_list[i][0])



    return NP_list

def pos_NNP_tagging(sentence):

    #Setting the path and jar files for the POS Tagger

    english_postagger=StanfordPOSTagger( 'C:\Python27\Lib\stanford-pos\models\english-bidirectional-distsim.tagger',
                             'C:\Python27\Lib\stanford-pos\stanford-postagger.jar', encoding='utf-8' )

    NP_list=[]

    POS_list=english_postagger.tag(sentence.split())

    for i in range(0, len(POS_list)):
        if POS_list[i][1] in ['NNP','NNPS']:
            NP_list.append(POS_list[i][0])


    return NP_list




def pos_tagging(sentence):

    english_postagger=StanfordPOSTagger( 'C:\Python27\Lib\stanford-pos\models\english-bidirectional-distsim.tagger',
                             'C:\Python27\Lib\stanford-pos\stanford-postagger.jar', encoding='utf-8' )

    VP_list=[]

    POS_list=english_postagger.tag(sentence.split())

    '''for i in range(0, len(POS_list)):
        if POS_list[i][1] in ['NNS','NNP','NNPS']:
            NP_list.append(POS_list[i][0])'''


    return POS_list