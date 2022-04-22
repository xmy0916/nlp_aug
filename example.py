from aug_func import func_list
import random

if __name__ == '__main__':
    sentences = "爱打篮球的男生喜欢什么样的女生"
    func = random.choice(func_list)
    print(func(sentences, prob=1.0))