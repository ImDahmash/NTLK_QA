import re

# Takes a list containing all the questions from the question file and returns three lists
# 1. containing the question as is
# 2. containing the cleansed question i.e without the 'Question:'#

def question_parser(question_list):

    questionID_list=[]
    q_list=[]
    # print len(question_list)
    for i in range(0, len(question_list)):
        q_list.append ( question_list[ i ] )

        # print i, q_list[i]

    # print 'Cleansed Q List is :',cleansedQ_list

    return q_list