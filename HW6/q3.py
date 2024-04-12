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

    senti_labels = [int(i) for i in input().split(",")]
    return words_lists, senti_labels


def get_sentiments(
    pos_words: list, neg_words: list, words: list, weights: tuple = (1, 1)
):
    pos_socre, neg_score = 0, 0
    # print(words)
    for word in words:
        if word in pos_words:
            pos_socre += 1
        elif word in neg_words:
            neg_score += 1

    # print(pos_socre, neg_score)
    pos_weight, neg_weight = weights
    weighted_socre = pos_weight * pos_socre - neg_weight * neg_score
    return weighted_socre


def classify_acc_cnt(senti_labels: list, scores: int):
    accuracy = 0
    # print(senti_labels, scores)
    for i in range(len(senti_labels)):
        if (senti_labels[i] == 0 and scores[i] < 0) or (
            senti_labels[i] == 1 and scores[i] >= 0
        ):
            accuracy += 1
    return accuracy


def output_score(best_score: int, weight):
    pos, neg = weight
    score_str = ",".join([str(pos), str(neg), str(best_score)])
    print(score_str)


words_lists, senti_labels = gen_words_list(sen_num)
pos_words = ["good", "best", "awesome", "excellent", "wonderful"]
neg_words = ["bad", "worst", "stupid", "shame"]
weights = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
best_acc = -1
best_weight = (-1, -1)
for weight in weights:
    scores = []
    for words in words_lists:
        scores.append(get_sentiments(pos_words, neg_words, words, weight))
    cur_acc = classify_acc_cnt(senti_labels, scores)

    if best_acc < cur_acc:
        best_acc = cur_acc
        best_weight = weight
output_score(best_acc, best_weight)
