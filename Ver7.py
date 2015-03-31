import re
import time


def review_sentiment_analysis(str_review):

    reviews = split_str_review(str_review)
    # train_set_comments = read_train_set()
    # classified_value = classify_data(train_set_comments)
    # negative_words = import_negative_words()
    # positive_words = import_positive_words()
    results = analyze_str_review(call_classified_value, call_negative_words, call_positive_words, reviews)

    return results


def split_str_review(str_review):

    reviews = re.sub("[^\w]", " ", str_review.lower()).split()

    # Detect the short-term words and make it easier to analyze
    try:
        if "don" in reviews:
            if reviews[reviews.index("don") + 1] == "t":
                reviews[reviews.index("don")] = "dont"
        elif "didn" in reviews:
            if reviews[reviews.index("didn") + 1] == "t":
                reviews[reviews.index("didn")] = "didnt"
        elif "wasn" in reviews:
            if reviews[reviews.index("wasn") + 1] == "t":
                reviews[reviews.index("wasn")] = "wasnt"
        elif "weren" in reviews:
            if reviews[reviews.index("weren") + 1] == "t":
                reviews[reviews.index("weren")] = "werent"
        elif "ain" in reviews:
            if reviews[reviews.index("ain") + 1] == "t":
                reviews[reviews.index("ain")] = "aint"
        elif "aren" in reviews:
            if reviews[reviews.index("aren") + 1] == "t":
                reviews[reviews.index("aren")] = "arent"
        elif "doesn" in reviews:
            if reviews[reviews.index("doesn") + 1] == "t":
                reviews[reviews.index("doesn")] = "doesnt"
        elif "won" in reviews:
            if reviews[reviews.index("won") + 1] == "t":
                reviews[reviews.index("won")] = "wont"
        elif "isn" in reviews:
            if reviews[reviews.index("isn") + 1] == "t":
                reviews[reviews.index("isn")] = "isnt"
        elif "hasn" in reviews:
            if reviews[reviews.index("hasn") + 1] == "t":
                reviews[reviews.index("hasn")] = "hasnt"
        elif "haven" in reviews:
            if reviews[reviews.index("haven") + 1] == "t":
                reviews[reviews.index("haven")] = "havent"
    except IndexError:
        pass

    return reviews


def read_train_set():

    # Create a list to store comments
    comment = []

    with open('24kData.txt', 'r') as f:
        for line in f:
            # split the sentence and store into a list
            line2 = re.sub("[^\w]", " ", line.lower()).split()

            # Detect the short-term words and make it easier to analyze
            try:
                if "don" in line2:
                    if line2[line2.index("don") + 1] == "t":
                        line2[line2.index("don")] = "dont"
                elif "didn" in line2:
                    if line2[line2.index("didn") + 1] == "t":
                        line2[line2.index("didn")] = "didnt"
                elif "wasn" in line2:
                    if line2[line2.index("wasn") + 1] == "t":
                        line2[line2.index("wasn")] = "wasnt"
                elif "weren" in line2:
                    if line2[line2.index("weren") + 1] == "t":
                        line2[line2.index("weren")] = "werent"
                elif "ain" in line2:
                    if line2[line2.index("ain") + 1] == "t":
                        line2[line2.index("ain")] = "aint"
                elif "aren" in line2:
                    if line2[line2.index("aren") + 1] == "t":
                        line2[line2.index("aren")] = "arent"
                elif "doesn" in line2:
                    if line2[line2.index("doesn") + 1] == "t":
                        line2[line2.index("doesn")] = "doesnt"
                elif "won" in line2:
                    if line2[line2.index("won") + 1] == "t":
                        line2[line2.index("won")] = "wont"
                elif "isn" in line2:
                    if line2[line2.index("isn") + 1] == "t":
                        line2[line2.index("isn")] = "isnt"
                elif "hasn" in line2:
                    if line2[line2.index("hasn") + 1] == "t":
                        line2[line2.index("hasn")] = "hasnt"
                elif "haven" in line2:
                    if line2[line2.index("haven") + 1] == "t":
                        line2[line2.index("haven")] = "havent"
            except IndexError:
                pass

            comment.append(line2)

    return comment


def import_negative_words():

    negative_words = {}

    with open('negative-words.txt', 'r') as n:
        for line in n:
            negative_words[line.strip().lower()] = "negative"

    negative_words["not"] = "negative"
    negative_words["dont"] = "negative"
    negative_words["wasnt"] = "negative"
    negative_words["isnt"] = "negative"
    negative_words["arent"] = "negative"
    negative_words["werent"] = "negative"
    negative_words["didnt"] = "negative"
    negative_words["wont"] = "negative"
    negative_words["doesnt"] = "negative"
    negative_words["aint"] = "negative"
    negative_words["hasnt"] = "negative"
    negative_words["havent"] = "negative"
    negative_words["never"] = "negative"

    return negative_words


def import_positive_words():

    positive_words = {}

    with open('positive-words.txt', 'r') as p:
        for line in p:
            positive_words[line.strip().lower()] = "positive"

    return positive_words


def classify_data(comments):

    words_value = {}
    value = 0.0

    for sentence in comments:
        for words in sentence:

            if sentence[0] == "1":
                value = -0.0001
            elif sentence[0] == "5":
                value = 0.0001

            if words in words_value:
                words_value[words] += value
            else:
                words_value[words] = value

    return words_value


def analyze_str_review(classified_value, negative_words,  positive_words, str_review):

    score = 0

    for words in str_review:
        if words in positive_words:
            score += 1
        elif words in negative_words:
            score -= 1

    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    elif score == 0:
        analysis_for_neutral(str_review, classified_value)


def analysis_for_neutral(str_review, classified_value):

    count_value = 0.0

    for words in str_review:
        count_value = count_value + classified_value[words]

    # average = -53.823

    if count_value >= -53.823:
        return "positive"
    elif count_value < -53.823:
        return "negative"


def test():

    accurate = 0

    with open('24kData.txt', 'r') as f:
        for line in f:

            if review_sentiment_analysis(line[1:]) == "positive":
                if line[0] == "5":
                    accurate += 1
            elif review_sentiment_analysis(line[1:]) == "negative":
                if line[0] == "1":
                    accurate += 1

    print accurate
    per = accurate/24000.00
    print per


start_time = time.time()
train_set_comments = read_train_set()
call_classified_value = classify_data(train_set_comments)
call_negative_words = import_negative_words()
call_positive_words = import_positive_words()
print("--- 1. %s seconds ---" % (time.time() - start_time))
start_time = time.time()
test()
print("--- %s seconds ---" % (time.time() - start_time))