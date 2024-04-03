import string


sen_num = int(input())


def gen_words_list(sen_num: int):
    words_lists = []
    for _ in range(sen_num):
        sen = input()
        clean_sen = sen.translate(
            str.maketrans(string.punctuation, " " * len(string.punctuation))
        )
        words = [word.lower() for word in clean_sen.split()]
        words_lists.append(words)
    return words_lists


def get_sentiments(pos_words: list, neg_words: list, words: list):
    pos_socre, neg_score = 0, 0
    # print(words)
    for word in words:
        if word in pos_words:
            pos_socre += 1
        elif word in neg_words:
            neg_score += 1

    # print(pos_socre, neg_score)
    return str(pos_socre - neg_score)


def output_score(score_list: list):
    score_str = ",".join(score_list)
    print(score_str)


words_lists = gen_words_list(sen_num)
pos_words = ["good", "best", "awesome", "excellent", "wonderful"]
neg_words = ["bad", "worst", "stupid", "shame"]
scores = []
for words in words_lists:
    scores.append(get_sentiments(pos_words, neg_words, words))
output_score(scores)
