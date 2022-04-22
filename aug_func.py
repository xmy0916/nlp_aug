import random
import jieba

same_dict = {}
with open("data/synonym.txt", "r") as r:
    lines = r.readlines()
    print("loading same words...")
    for line in lines:
        words = line.strip("\n").split(" ")
        same_dict[words[0]] = words[1:]


# 随机删除单词
def random_delete_word(sentence, prob):
    if random.random() > prob:
        return sentence
    else:
        words = list(jieba.cut(sentence))
        delete_index = random.randint(0, len(words)-1)
        del words[delete_index]
        sentence = "".join(words)
    return sentence


# 随机删除字符
def random_delete_char(sentence, prob):
    if random.random() > prob:
        return sentence
    else:
        sentence = list(sentence)
        delete_index = random.randint(0, len(sentence)-1)
        del sentence[delete_index]
        sentence = "".join(sentence)
    return sentence


# 随机交换单词
def random_swap_word(sentence, prob):
    if random.random() > prob:
        return sentence
    else:
        words = list(jieba.cut(sentence))
        if len(words) == 1:
            return sentence
        index1 = random.randint(0, len(words)-1)
        index2 = random.randint(0, len(words)-1)
        while index2 == index1:
            index2 = random.randint(0, len(words)-1)
        words[index1], words[index2] = words[index2], words[index1]
        sentence = "".join(words)
    return sentence


# 随机删除全部符号
def random_delete_symbol(sentence, prob):
    if random.random() > prob:
        return sentence
    else:
        tmp = []
        for c in sentence:
            if '\u4e00' <= c <= '\u9fa5':
                tmp.append(c)
        sentence = "".join(tmp)
    return sentence


# 随机同义词替换
def random_change_same_word(sentence, prob):
    if random.random() > prob:
        return sentence
    else:
        words = list(jieba.cut(sentence))
        index = random.randint(0, len(words)-1)
        if words[index] in same_dict.keys():
            words[index] = random.choice(same_dict[words[index]])
        sentence = "".join(words)
    return sentence


# 随机回译
# 没加到func list中，因为要翻墙才能用...
def random_googletrans(sentence, prob):
    if random.random() > prob:
        return sentence
    else:
        from googletrans import Translator
        t_from='zh-cn'
        t_to='en'
        translator = Translator()
        s = translator.translate(text=sentence, dest=t_to,src=t_from)
        eng = s.text
        s = translator.translate(text=eng, dest=t_from,src=t_to)
        return s.text


func_list = [
    random_delete_word, 
    random_delete_char, 
    random_swap_word, 
    random_delete_symbol, 
    random_change_same_word,
    # random_googletrans  # 要翻墙才能用...
]
