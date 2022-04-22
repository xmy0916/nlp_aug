# nlp aug

Some easy nlp aug func...

- random delete word
- random delete char
- random delete symbol
- random swag word
- random retranslation
- random synonym substitution # need scientific internet


## examples
example: only use one aug func
```python
from aug_func import func_list
import random

if __name__ == '__main__':
    sentences = "爱打篮球的男生喜欢什么样的女生"
    func = random.choice(func_list)
    print(func(sentences, prob=1.0))
```

example: use all aug func
```python
from aug_func import func_list
import random

if __name__ == '__main__':
    sentences = "爱打篮球的男生喜欢什么样的女生"
    for func in func_list:
        sentences = func(sentences, prob=random.random())
    print(sentences)
```