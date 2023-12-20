import pandas as pd

#tags
usability_tags = [
    'i-unexpected-fees',
    'i-unwanted-sign-up',
    'i-unnoticed-left-out-fields', 
    'i-missing-sign-up-link-in-popup', 'i-unwanted-marketing-consent',
    'i-small-unreadable-elements', 'i-bad-website-overall',
    'i-buy-button-wrong-label', 'i-no-shipping-on-product-page',
    'i-intrusive-popups-overall',
    'i-unexpected-pre-filled-fields', 'i-unclickable-product-image',
    'i-default-white-tshirt', 'i-unreadable-website-overall',
    'i-black-filter-wrong-color', 'i-missing-payment-methods',
    'i-sort-not-found', 'i-search-problems',
    'i-cart-notification-missing',
    'i-missing-checkout-link-in-popup'
]
sentiment_tags = ['s-neu', 's-neg', 's-pos']
topic_tags = ['t-act', 't-imp', 't-obs', 't-prop', 't-exp', 't-know']
info_tags = ['info-high', 'info-med', 'info-low', 'info-none']
task_tags = [
    'ti-complicated-scenario', 'ti-unresponsive/unclickable', 
    'ti-scroll-problems', 'ti-repetetive-ai', 'ti-task-description-overlap'
]
repeat_tags = ['repeat-cross', 'repeat-followup']
question_tags = ['question-none', 'question-skip', 'content-unrelated']

info_tags_convert = {'info-none': 0, 'info-low': 1, 'info-med': 2, 'info-high': 3}
topic_tags_convert = {'t-act': 0, 't-imp': 1, 't-obs': 2, 't-prop': 3, 't-exp': 4, 't-know': 5}
sentiment_tags_convert = {'s-neu': 0, 's-neg': -1, 's-pos': 1}

#columns
answer_columns = ['pre1', 'pre1F1', 'pre1F2', 'pre1F3', 'pre2', 'pre2F1', 'pre2F2', 'pre2F3', 'T1Q1', 'T1Q1F1', 'T1Q1F2', 'T1Q1F3', 'T1Q2', 'T1Q2F1', 'T1Q2F2', 'T1Q2F3', 'T1Q3', 'T1Q3F1', 'T1Q3F2', 'T1Q3F3', 'T2Q1', 'T2Q1F1', 'T2Q1F2', 'T2Q1F3', 'T2Q2', 'T2Q2F1', 'T2Q2F2', 'T2Q2F3', 'T2Q3', 'T2Q3F1', 'T2Q3F2', 'T2Q3F3', 'post1', 'post1F1', 'post1F2', 'post1F3']
note_columns = ['pre1Note', 'pre1F1Note', 'pre1F2Note', 'pre1F3Note', 'pre2Note', 'pre2F1Note', 'pre2F2Note', 'pre2F3Note', 'T1Q1Note', 'T1Q1F1Note', 'T1Q1F2Note', 'T1Q1F3Note', 'T1Q2Note', 'T1Q2F1Note', 'T1Q2F2Note', 'T1Q2F3Note', 'T1Q3Note', 'T1Q3F1Note', 'T1Q3F2Note', 'T1Q3F3Note', 'T2Q1Note', 'T2Q1F1Note', 'T2Q1F2Note', 'T2Q1F3Note', 'T2Q2Note', 'T2Q2F1Note', 'T2Q2F2Note', 'T2Q2F3Note', 'T2Q3Note', 'T2Q3F1Note', 'T2Q3F2Note', 'T2Q3F3Note', 'post1Note', 'post1F1Note', 'post1F2Note', 'post1F3Note']
base_note_columns = ['pre1Note', 'pre2Note', 'T1Q1Note', 'T1Q2Note', 'T1Q3Note', 'T2Q1Note', 'T2Q2Note', 'T2Q3Note', 'post1Note']
task_note_columns = ['T1Q1Note', 'T1Q1F1Note', 'T1Q1F2Note', 'T1Q1F3Note', 'T1Q2Note',
       'T1Q2F1Note', 'T1Q2F2Note', 'T1Q2F3Note', 'T1Q3Note', 'T1Q3F1Note',
       'T1Q3F2Note', 'T1Q3F3Note', 'T2Q1Note', 'T2Q1F1Note', 'T2Q1F2Note',
       'T2Q1F3Note', 'T2Q2Note', 'T2Q2F1Note', 'T2Q2F2Note', 'T2Q2F3Note',
       'T2Q3Note', 'T2Q3F1Note', 'T2Q3F2Note', 'T2Q3F3Note']
pre_note_columns = ['pre1Note', 'pre1F1Note', 'pre1F2Note', 'pre1F3Note', 'pre2Note', 'pre2F1Note', 'pre2F2Note', 'pre2F3Note']
post_note_columns = ['post1Note', 'post1F1Note', 'post1F2Note', 'post1F3Note']
base_task_note_columns = ['T1Q1Note', 'T1Q2Note','T1Q3Note', 'T2Q1Note', 'T2Q2Note', 'T2Q3Note']
follow_up_columns = ['pre1F1Note', 'pre1F2Note', 'pre1F3Note', 'pre2F1Note', 'pre2F2Note', 'pre2F3Note', 'T1Q1F1Note', 'T1Q1F2Note', 'T1Q1F3Note', 'T1Q2F1Note', 'T1Q2F2Note', 'T1Q2F3Note', 'T1Q3F1Note', 'T1Q3F2Note', 'T1Q3F3Note', 'T2Q1F1Note', 'T2Q1F2Note', 'T2Q1F3Note', 'T2Q2F1Note', 'T2Q2F2Note', 'T2Q2F3Note', 'T2Q3F1Note', 'T2Q3F2Note', 'T2Q3F3Note', 'post1F1Note', 'post1F2Note', 'post1F3Note']
follow_up_task_columns = ['T1Q1F1Note', 'T1Q1F2Note', 'T1Q1F3Note', 'T1Q2F1Note', 'T1Q2F2Note', 'T1Q2F3Note', 'T1Q3F1Note', 'T1Q3F2Note', 'T1Q3F3Note', 'T2Q1F1Note', 'T2Q1F2Note', 'T2Q1F3Note', 'T2Q2F1Note', 'T2Q2F2Note', 'T2Q2F3Note', 'T2Q3F1Note', 'T2Q3F2Note', 'T2Q3F3Note']
follow_up_1_columns = ['pre1F1Note', 'pre2F1Note', 'T1Q1F1Note', 'T1Q2F1Note', 'T1Q3F1Note', 'T2Q1F1Note', 'T2Q2F1Note', 'T2Q3F1Note', 'post1F1Note']
follow_up_1_task_columns = ['T1Q1F1Note', 'T1Q2F1Note', 'T1Q3F1Note', 'T2Q1F1Note', 'T2Q2F1Note', 'T2Q3F1Note']
follow_up_2_columns = ['pre1F2Note', 'pre2F2Note', 'T1Q1F2Note', 'T1Q2F2Note', 'T1Q3F2Note', 'T2Q1F2Note', 'T2Q2F2Note', 'T2Q3F2Note', 'post1F2Note']
follow_up_2_task_columns = ['T1Q1F2Note', 'T1Q2F2Note', 'T1Q3F2Note', 'T2Q1F2Note', 'T2Q2F2Note', 'T2Q3F2Note']
follow_up_3_columns = ['pre1F3Note', 'pre2F3Note', 'T1Q1F3Note', 'T1Q2F3Note', 'T1Q3F3Note', 'T2Q1F3Note', 'T2Q2F3Note', 'T2Q3F3Note', 'post1F3Note']
follow_up_3_task_columns = ['T1Q1F3Note', 'T1Q2F3Note', 'T1Q3F3Note', 'T2Q1F3Note', 'T2Q2F3Note', 'T2Q3F3Note']
count_columns = ['pre1WordCount', 'pre1F1WordCount', 'pre1F2WordCount', 'pre1F3WordCount', 'pre2WordCount', 'pre2F1WordCount', 'pre2F2WordCount', 'pre2F3WordCount', 'T1Q1WordCount', 'T1Q1F1WordCount', 'T1Q1F2WordCount', 'T1Q1F3WordCount', 'T1Q2WordCount', 'T1Q2F1WordCount', 'T1Q2F2WordCount', 'T1Q2F3WordCount', 'T1Q3WordCount', 'T1Q3F1WordCount', 'T1Q3F2WordCount', 'T1Q3F3WordCount', 'T2Q1WordCount', 'T2Q1F1WordCount', 'T2Q1F2WordCount', 'T2Q1F3WordCount', 'T2Q2WordCount', 'T2Q2F1WordCount', 'T2Q2F2WordCount', 'T2Q2F3WordCount', 'T2Q3WordCount', 'T2Q3F1WordCount', 'T2Q3F2WordCount', 'T2Q3F3WordCount', 'post1WordCount', 'post1F1WordCount', 'post1F2WordCount', 'post1F3WordCount']
sentiment_columns = ['pre1Sentiment', 'pre1F1Sentiment', 'pre1F2Sentiment', 'pre1F3Sentiment', 'pre2Sentiment', 'pre2F1Sentiment', 'pre2F2Sentiment', 'pre2F3Sentiment', 'T1Q1Sentiment', 'T1Q1F1Sentiment', 'T1Q1F2Sentiment', 'T1Q1F3Sentiment', 'T1Q2Sentiment', 'T1Q2F1Sentiment', 'T1Q2F2Sentiment', 'T1Q2F3Sentiment', 'T1Q3Sentiment', 'T1Q3F1Sentiment', 'T1Q3F2Sentiment', 'T1Q3F3Sentiment', 'T2Q1Sentiment', 'T2Q1F1Sentiment', 'T2Q1F2Sentiment', 'T2Q1F3Sentiment', 'T2Q2Sentiment', 'T2Q2F1Sentiment', 'T2Q2F2Sentiment', 'T2Q2F3Sentiment', 'T2Q3Sentiment', 'T2Q3F1Sentiment', 'T2Q3F2Sentiment', 'T2Q3F3Sentiment', 'post1Sentiment', 'post1F1Sentiment', 'post1F2Sentiment', 'post1F3Sentiment']

#help functions
INFO = 0
REPEAT = 1
ISSUES = 2
TASK_ISSUES = 3
SENTIMENT = 4
SKIP = 5
SKIP_NOQUESTION = 6
REPEAT_NOINFO = 7
TOPIC = 8
REPEAT_NOINFO_CROSS = 9
REPEAT_NOINFO_FOLLOW = 10
UNRELATED = 11
NO_QUESTION = 12

def getInfoCell(input, code):
    tag_list = input.split(',')
    if code == INFO:
        return info_tags_convert[list(filter(lambda x: x in info_tags, tag_list))[0]]
    elif code == REPEAT:
        return len(list(filter(lambda x: x in repeat_tags, tag_list))) > 0
    elif code == ISSUES:
        return len(list(filter(lambda x: x in usability_tags, tag_list)))
    elif code == TASK_ISSUES:
        return len(list(filter(lambda x: x in task_tags, tag_list)))
    elif code == SENTIMENT:
        sentiment = list(filter(lambda x: x in sentiment_tags, tag_list))
        return sentiment_tags_convert[sentiment[0]] if len(sentiment) > 0 else 0
    elif code == SKIP:
        return len(list(filter(lambda x: x == 'question-skip', tag_list))) > 0
    elif code == SKIP_NOQUESTION:
        return len(list(filter(lambda x: x == 'question-skip' or x == 'question-none', tag_list))) > 0
    elif code == REPEAT_NOINFO:
        return 'info-none' in tag_list and ('repeat-cross' in tag_list or 'repeat-followup' in tag_list)
    elif code == TOPIC:
        topics = list(filter(lambda x: x in topic_tags, tag_list))
        return [topic_tags_convert[x] for x in topics]
    elif code == REPEAT_NOINFO_CROSS:
        return 'info-none' in tag_list and 'repeat-cross' in tag_list
    elif code == REPEAT_NOINFO_FOLLOW:
        return 'info-none' in tag_list and 'repeat-followup' in tag_list
    elif code == UNRELATED:
        return 'info-none' in tag_list and 'content-unrelated' in tag_list
    elif code == NO_QUESTION:
        return 'info-none' in tag_list and 'question-none' in tag_list

def getInfo(data, code):
    result = data[['id', 'variant'] + note_columns].copy(deep=True)
    return result.map(
        lambda x: getInfoCell(x, code) if type(x) == str and x not in ['ai', 'no-ai'] else x,
        na_action='ignore'
    )

def my_count(input_data, bins=False):
    task_column_group_names = [
        'All notes', 'All task notes', 'All pre notes', 'All post notes',
        'All base notes', 'All follow-up notes', 
        'All base task notes', 'All follow-up task notes',
        'First follow-up task notes', 'Second follow-up task notes', 'Third follow-up task notes'
    ]
    output = pd.Series()
    for index, columns in enumerate([
        note_columns, task_note_columns, pre_note_columns, post_note_columns,
        base_note_columns, follow_up_columns,
        base_task_note_columns, follow_up_task_columns, 
        follow_up_1_task_columns, follow_up_2_task_columns, follow_up_3_task_columns
    ]):
        if(bins != False):
            sum = [0 for x in bins]
            for column in columns:
                counts = input_data[column].value_counts()
                for i, bin in enumerate(bins):
                    sum[i] += counts[bin] if bin in counts else 0
            to_append = pd.Series({task_column_group_names[index] : sum})
            output = pd.concat([output, to_append]) if not output.empty else to_append
        else:
            sum = 0
            for column in columns:
                sum += input_data[column].sum()
            to_append = pd.Series({task_column_group_names[index] : sum})
            output = pd.concat([output, to_append]) if not output.empty else to_append
    if(bins != False):
        for column in task_note_columns:
            sum = [0 for x in bins]
            counts = input_data[column].value_counts()
            for bin in bins:
                sum[bin] += counts[bin] if bin in counts else 0
            to_append = pd.Series({column : sum})
            output = pd.concat([output, to_append]) if not output.empty else to_append
    else:
        for column in task_note_columns:
            to_append = pd.Series({column : input_data[column].sum()})
            output = pd.concat([output, to_append]) if not output.empty else to_append
    return output