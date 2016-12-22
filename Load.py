
from datetime import datetime
import How
import What
import When
import Where
import Which
import Why
import questionprocessing
import NamedEntity
import Who

sentences = ""
# stop_words = set ( stopwords.words ( "english" ) )
stop_words_list_stanford =['a','an','and','are','as','at','be','buy','for','from',
                           'has','he','in','is','it','its','of','on','that','the',
                          'to','was','were','will','with']
stop_words = set (stop_words_list_stanford)
stop_words.update( [ '.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '#' ])

# grammar = r"""
#   NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and noun
#       {<NNP>+}                # chunk sequences of proper nouns
# """
grammar = r"""
  NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
  CLAUSE: {<NP><VP>}           # Chunk NP, VP
  """

#Global lists
non_stop_words = [ ]
answer_list=[]
question_list=[]
bigrams = [ ]
NER_list=[]


# import re
# pattern = "\.?(?P<sentence>.*?Obama.*?)\."
# match = re.search(pattern, sentences)
# if match != None:
#     print match.group("sentence")

# Psragraph ............

master_person_list = [ ]
master_org_list = [ ]
master_loc_list = [ ]
master_month_list = [ ]
master_time_list = [ ]
master_money_list = [ ]
master_percent_list = [ ]
master_prof_list = [ ]

with open('Pargh.txt', 'r') as parghFile:
    sentence = parghFile.readlines( )

for j in range (0, len(sentence)):
    sentence [j] = sentence[j].replace ( "\n", "")

hline_date = datetime.now().strftime ('%B %d, %Y')
print 'Time now: ', hline_date
################## Removing the stopwords from each sentence using NLTK's stopwords list ###################
stopwords_free_sentences_list = [ ]
for sent in sentence:
    for w in sent.split ( ):
        if w.lower ( ) not in stop_words_list_stanford:
            non_stop_words.append ( w )
    temp = ' '.join ( non_stop_words )
    stopwords_free_sentences_list.append ( temp )
    non_stop_words = [ ]

for i in range ( 0, len ( sentence ) ):
    temp_str = sentence[ i ]
    temp_str = temp_str.strip ( )
    temp_str = temp_str.replace ( ',', '' ).replace ( '!', '' ).replace( '.', '')

sent_person_list, sent_org_list, sent_loc_list, sent_month_list, sent_time_list, sent_money_list, sent_percent_list, sent_prof_list = NamedEntity.named_entity_recognition (
    temp_str )

master_person_list.append ( sent_person_list )
# print master_person_list
master_org_list.append ( sent_org_list )
# print master_org_list
master_loc_list.append ( sent_loc_list )
# print master_loc_list
master_month_list.append ( sent_month_list )  # month and weekday names + season names
master_month_list
# print master_month_list
master_time_list.append ( sent_time_list )
# print master_time_list
master_money_list.append ( sent_money_list )
# print master_money_list
master_percent_list.append ( sent_percent_list )
# print master_percent_list
master_prof_list.append ( sent_prof_list )
# print master_prof_list

### Questions ..........
with open('Question.txt', 'r') as questionFile:
    question = questionFile.readlines()

for i in range ( 0, len ( question)):
    question[ i ] = question[ i ].replace ( "\n", "" )
print question

qList = questionprocessing.question_parser ( question )

################## Removing the stopwords from each question using NLTK's stopwords list ###################
stopwords_free_questions_list = [ ]
for sent in qList:
    for w in sent.split ( ):
        if w.lower ( ) not in stop_words_list_stanford:
            non_stop_words.append ( w )
    temp = ' '.join ( non_stop_words )
    stopwords_free_questions_list.append ( temp )
    non_stop_words = [ ]

################### CATEGORIZING THE QUESTION AS WH0, WHAT, WHEN , WHY , WHERE OR HOW  ########################
print 'Results :'
for i in range ( 0, len ( qList ) ):
    result = ""
    qWords = qList[ i ].split ( )
    q_flag = 0
    for j in range ( 0, len ( qWords ) ):
        if qWords[ j ].lower ( ) == 'who' or qWords[ j ].lower ( ) == 'whom' or qWords[ j ].lower ( ) == 'whose':
            q_flag = 1
            result = Who.answering_who ( qList[ i ], stopwords_free_questions_list[ i ], sentence,
                                         stopwords_free_sentences_list, master_person_list,
                                         master_prof_list )  # stopwords_free_sentences_list

            break
        elif qWords[ j ].lower ( ) == 'what':
            q_flag = 1
            result = What.answering_what ( qList[ i ], stopwords_free_questions_list[ i ], sentence,
                                           stopwords_free_sentences_list, master_time_list,
                                           master_person_list )  # stopwords_free_sentences_list
            break
        elif qWords[ j ].lower ( ) == 'when':
            q_flag = 1
            result = When.answering_when ( qList[ i ], stopwords_free_questions_list[ i ], sentence,
                                           stopwords_free_sentences_list, hline_date, master_month_list,
                                           master_time_list )  # stopwords_free_sentences_list

            break
        elif qWords[ j ].lower ( ) == 'where':
            q_flag = 1
            result = Where.answering_where ( qList[ i ], stopwords_free_questions_list[ i ], sentence,
                                             stopwords_free_sentences_list, hline_date,
                                             master_loc_list )  # stopwords_free_sentences_list

            break
        elif qWords[ j ].lower ( ) == 'why':
            q_flag = 1
            result = Why.answering_why ( qList[ i ], stopwords_free_questions_list[ i ], sentence,
                                         stopwords_free_sentences_list )  # stopwords_free_sentences_list

            break
        elif qWords[ j ].lower ( ) == 'how':
            q_flag = 1
            result = How.answering_how ( qList[ i ], stopwords_free_questions_list[ i ], sentence,
                                         stopwords_free_sentences_list, master_time_list,
                                         master_percent_list )  # stopwords_free_sentences_list
            break
        elif qWords[ j ].lower ( ) == 'which':
            q_flag = 1
            result = Which.answering_which ( qList[ i ], stopwords_free_questions_list[ i ], sentence,
                                             stopwords_free_sentences_list )
            break
        else:
            answer_list.append ( 'No answer' )
            # print 'Answer:  No answer'+'\n'
    if q_flag == 0:
        print 'Answer: No answer' + '\n'
    else:
        print 'Answer: ', result + '\n'




