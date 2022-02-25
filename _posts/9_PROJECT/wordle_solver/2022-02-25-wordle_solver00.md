---
title: wordle solver 만들어보기 - basic
category: projet
tags: wordle python pypy 
--- 

## wordle solver 만들어보기 - basic

- 요즘 친구들과 [wordle](https://www.nytimes.com/games/wordle/index.html) 게임을 하고 있습니다. 그냥 5 문자로 된 word를 맞추는 게임인데요, 이게 하루에 1기기로 1번만 할 수 있어서인지 모르겠지만 꽤 오랫동안 매일 해오고 있습니다.

## About Wordle

- wordle은 Josh Wardle이라는 사람이 만든 게임인데요(자신의 이름과 비슷하죠), 게임 자체는 앞서 말한 것처럼 랜덤으로 나오는 5개 문자의 단어를 맞추는 간단한 방식이고, 사용자가 유효한(사전에 존재하는 단어만 유효. aeiou와 같은 무작위 방식은 불가함) 단어를 입력하면 해당 단어가 목적 단어에 비해 얼마나 다른지를 알려줍니다.
- 이 때 1) 목적 단어에 해당 문자 자체가 없다. 2) 목적 단어에 해당 문자가 있으나 위치가 다르다. 3) 목적 단어에 해당 문자가 있고 위치도 동일하다 라는 세 가지 정보값을 줍니다. 즉, 6번의 기회 내에 최대한 정보 값을 많이 획득해서 단어를 맞추는 것이 목표입니다.
- 원래는 개인이 운영했으나, 현재는 Newyork Times에서 구입해서 사용하고 있습니다.
- 다양한 언어로 파생된 Wordle들이 있으나, 한국어로 된 단어는 없는 것으로 보입니다. 이는 초성 / 중성 / 종성으로 구분된 한국 단어 특성상 wordle과 동일한 게임을 맞추는 것이 쉽지 않기 때문이 아닐까 생각해봅니다.

## Wordle Solver 만들기

- 우선, wordle 을 풀어주는 문제를 만들기 위해서는 wordle처럼 영단어 리스트들을 가지고 있어야 합니다. [github - dwyl - english-words](https://github.com/dwyl/english-words)에 영어단어가 정리되어 있어 해당 단어를 가져와서 사용해봤습니다. 그중에서 alphabet만으로 구성된 단어 목록이 있어서 해당 txt파일을 사용했습니다.
- wordle에서 단어를 추측할 때는 여러 가지 방법이 있겠으나, 다음 3가지로 구분된다고 생각합니다.
  1. 아직 확인되지 않은(Unknown)문자가 단어에 포함되는지를 확인한다.
  2. 위치를 모르는 문자의 위치를 확인한다.
  3. 위치가 확인된 문자가 있다면, 해당 문자를 고정하고 단어를 추측한다.
- 즉, 어떤 단어를 추측할 때면 위 세 방식에 대한 weight에 따라서 추측하는 단어가 달라집니다. 1번 weight가 높다면 최대한 문자들이 겹치지 않는 단어들을 찾아서 단어 후보군을 빠르게 찾을 테고, 2번weight 가 높은 사람이라면, 존재하는 문자를 파악했다면 최대한 해당 문자를 유지한 상태로 단어를 추측해나갈 것 같습니다.
- 따라서, 위 방식에 대해서 weight를 다르게 세팅할 수 있도록 하여 개발하면 될것 같습니다.
- 사실 이게 다라서 뭐 더 말할 내용이 없네요. 위 내용 대로 개발을 진행했습니다. Code는 가장 밑에 정리하였습니다.

### optimal parameter

- 아래 3 방식에 대한 weight를 0.1 ~ 1.0으로 변경해 가면서 100개의 problem을 랜덤으로 풀고 어떤 경우에 평균 trial 수가 제일 적은지 돌려봤습니다.
  1. 아직 확인되지 않은(Unknown)문자가 단어에 포함되는지를 확인한다(`exc_c`)
  2. 위치를 모르는 문자의 위치를 확인한다(`idx_c`)
  3. 위치가 확인된 문자가 있다면, 해당 문자를 고정하고 단어를 추측한다(`cor_c`)
- 알고리즘을 거지같이 짠 관계로 더 많은 실험을 하지는 못했습니다만, 아래 실험이 맞다는 전제 하에서 보면 대략 "위치까지 파악이 되었다면 최대한 위치를 고정한 상태로 단어를 추정하는 것이 좋다", "단어 포함 정보는 위치 정보에 비해 2 ~ 4 배 정도의 가치를 가진다"와 같은 내용이 있네요. 뭐 좀 더 실험해보면 재밌겠지만 귀찮아요 하하하

```
param: exc_c: 0.50 idx_c: 0.20 cor_c: 1.00 result: 4.98 
param: exc_c: 0.20 idx_c: 0.10 cor_c: 0.80 result: 5.02 
param: exc_c: 0.20 idx_c: 0.10 cor_c: 0.90 result: 5.02 
param: exc_c: 0.20 idx_c: 0.10 cor_c: 1.00 result: 5.02 
param: exc_c: 0.30 idx_c: 0.10 cor_c: 0.70 result: 5.02 
param: exc_c: 0.30 idx_c: 0.10 cor_c: 0.80 result: 5.02 
param: exc_c: 0.30 idx_c: 0.10 cor_c: 0.90 result: 5.02 
param: exc_c: 0.30 idx_c: 0.10 cor_c: 1.00 result: 5.02 
param: exc_c: 0.40 idx_c: 0.10 cor_c: 0.90 result: 5.02 
param: exc_c: 0.40 idx_c: 0.10 cor_c: 1.00 result: 5.02 
```

## wrap-up

- 이번 개발에서는 각 문자에 대한 weight를 동일하게 세팅했는데요. 문자 별로 포함된 단어의 수가 다르기 때문에, 단어의 수가 많은 문자를 먼저 확인해주는 것이 더 이롭습니다. 가령 a가 포함된 단어가 10,000개이고, b가 포함된 단어가 1,000 개라면, a를 먼저 확인해주는 것이 이로울 수 있죠.
- 실제로는 Step별로 전략이 달라집니다. 초기 ~2번까지는 최대한 문자를 많이 걸르는 방식으로 진행하고 이후에는 위치를 확인하는 방식으로 진행하는 것이 효율적이죠. 하지만, 현재 알고리즘에서는 step에 따른 차이가 반영되어 있지 않습니다. 물론 초기에는 INDEX_SCORE가 0에 가까운 반면 뒤 쪽에서는 INDEX_SCORE 값이 달라지게 되므로 조금씩은 step에 따른 차이가 반영되기는 합니다.
- 강화학습 기법으로 좀 더 만들어볼 수 있지 않을까 싶은데, 강화학습 기초도 까먹은지 오래되어서 못할것 같네요 호호. 그래도 다음에 한번 해봐야겠습니다.
- 이게 한번 단어를 추측할때마다, 모든 사전을 뒤지는 방식으로 개발을 하다보니, 속도에서 꽤 문제가 있습니다. 그래서 python을 쓰다가 pypy3로 변경해서 하니까 조금 더 빨라지더군요. multiprocessing을사용한다면 더 빨라질 수도 있을 것 같습니다만, 이것 또한...안 써본지 오래되어서 기억안나네요 호호호.


## Code 

```python
"""
- wordle solver
"""
import random
import time
import json


def read_words_alpha(word_len: int = 5, excluded_words: list = []) -> list:
    """
    - word_len 길이에 속하고, excluded_words에 속하지 않는 단어만 리턴
    """
    return_lst = list()
    with open("words_alpha.txt", "r") as f:
        for i, each_line in enumerate(f.readlines()):
            word = each_line.strip()
            if (len(word) == word_len) and (word not in excluded_words):
                return_lst.append(word)
    return return_lst


def find_words_excluding_char(
        total_words: list, ex_char: str = "", limit_n: int = 5):
    """
    - ex_char를 보유하지 않은 단어들만 출력
    """
    word_print_count = 0
    return_w_lst = list()
    for each_word in total_words:
        if len(set(each_word).intersection(set(ex_char))) == 0:
            if len(set(each_word)) == 5:
                print(each_word)
                return_w_lst.append(each_word)
                word_print_count += 1
                if word_print_count == limit_n:
                    break
    return return_w_lst


def current_state_of_word(target_word: str, guess_word: str) -> list:
    """
    target_word와 guess_word를 비교하여 정보를 리턴
    - 2: char, index equal
    - 1: char equal
    - 0: None
    """
    return_lst = list()
    for ca, cb in zip(target_word, guess_word):
        if ca == cb:
            return_lst.append(2)
        else:
            if cb in set(target_word):
                return_lst.append(1)
            else:
                return_lst.append(0)
    return return_lst


class WordleSolver:
    def __init__(self):
        self.total_words = read_words_alpha(5, [])
        self.exclude_char = set()
        self.candidate_char = set()
        self.index_exclude_dict = {
            i: set() for i in range(0, 5)
        }
        self.target_word = ["_" for i in range(0, 5)]
        self.excluded_words = []

    def refresh(self):
        self.exclude_char = set()
        self.candidate_char = set()
        self.index_exclude_dict = {
            i: set() for i in range(0, 5)
        }
        self.target_word = ["_" for i in range(0, 5)]
        self.excluded_words = []

    def set_constant(self, exclude_c=1.0, index_c=0.2, correct_c=5.0):
        """
        - word를 검색할 때 획득할 수 있는 정보들에 대한 weight
        """
        self.EXCLUDE_C = exclude_c
        self.INDEX_C = index_c
        self.CORRECT_C = correct_c

    def print_self(self):
        print(f"exclude_char: {self.exclude_char}")
        print(f"candidate_char: {self.candidate_char}")
        print(f"index_exclude_dict: {self.index_exclude_dict}")

    def scoring_word(self, word: str) -> int:
        """
        - 각 정보에 대한 weight를 사용하여 단어의 정보획득량을 계산
        """
        return_score = 0.0
        # EXCLUDE_C
        before_exclude = len(self.exclude_char)
        after__exclude = len(self.exclude_char.union(set(word)))
        exclude_score = (after__exclude - before_exclude) * self.EXCLUDE_C
        exclude_score = exclude_score / ((27 - before_exclude) / 27)
        return_score += exclude_score

        # INDEX_C
        index_count = 0
        for i, c in enumerate(word):
            if c != self.target_word[i]:
                if c in self.candidate_char:
                    if c not in self.index_exclude_dict[i]:
                        index_count += 1
        index_score = index_count * self.INDEX_C
        index_score *= len(self.candidate_char)
        return_score += index_score

        # CORRECT_C
        correct_count = 0
        for i, c in enumerate(self.target_word):
            if word[i] == c:
                correct_count += 1
        return_score += correct_count * self.CORRECT_C
        return return_score

    def updating_info(self, guess_word: str, feedback: list):
        """
        - feedback: guess list
        """
        self.excluded_words.append(guess_word)
        for i, (c, f) in enumerate(zip(guess_word, feedback)):
            if f == 2:
                self.candidate_char.update(c)
                self.target_word[i] = c
            elif f == 1:
                self.candidate_char.update(c)
                self.index_exclude_dict[i].update(c)
            elif f == 0:
                self.exclude_char.update(c)
                for i in range(0, 5):
                    self.index_exclude_dict[i].update(c)
            else:
                print("ERROR")

    def guessing_word(self) -> str:
        """
        - 전체 단어 pool중에서 가장 정보 획득량(score)이 높은 단어를 리턴
        """
        random_index = random.randint(0, len(self.total_words))
        guess_word = self.total_words[random_index]
        guess_score = self.scoring_word(guess_word)

        for curr_word in self.total_words:
            curr_score = self.scoring_word(curr_word)
            if curr_word not in self.excluded_words:
                if guess_score < curr_score:
                    guess_word = curr_word
                    guess_score = curr_score
            else:
                continue
        if False:
            print(f"{guess_word}, {guess_score:7.3f}")
        return guess_word


if __name__ == "__main__":
    wordle_solver = WordleSolver()

    total_words = read_words_alpha()

    file_name = f"log/result.json"
    wf = open(file_name, "w")
    result_list = list()

    """
    - exc_c, idx_c, cor_c 에 대한 Grid Search 를 진행하여
    평균적인 trial 수를 json파일에 저장한다.
    """
    problem_n = 50
    param_range = [i * 0.1 for i in range(1, 11)]

    for exc_c in param_range:
        for idx_c in param_range:
            for cor_c in param_range:
                start_time = time.time()
                param_and_result_dict = dict()
                param_and_result_dict['param'] = {
                    'exc_c': exc_c, 'idx_c': idx_c, 'cor_c': cor_c
                }
                wordle_solver.set_constant(exc_c, idx_c, cor_c)
                log = f"== EXC_C: {exc_c:6.2f}, IDX_C: {idx_c:6.2f}, COR_C: {cor_c: 6.2f} ::::  "
                print(log, end="")

                trial_lst = list()
                for each_problem in range(0, problem_n):
                    random.seed(each_problem)
                    wordle_solver.refresh()

                    target_index = random.randint(0, len(total_words))
                    target_word = total_words[target_index]
                    # print(target_word)
                    trial_to_success = 0

                    # auto input
                    for each_trial in range(0, 100):
                        trial_to_success += 1
                        # print(f"== Trial {each_trial: 2d} :: ", end="")
                        predicted_word = wordle_solver.guessing_word()
                        feedback = current_state_of_word(target_word, predicted_word)
                        wordle_solver.updating_info(predicted_word, feedback)

                        if predicted_word == target_word:
                            break
                    if False:
                        print(f"== Problem: {each_problem:2d} :: {target_word} :: ", end="")
                        print(f"Trial to success: {trial_to_success:3d}")
                    trial_lst.append(trial_to_success)
                avg_trial = sum(trial_lst) / problem_n
                param_and_result_dict['result'] = avg_trial
                result_list.append(param_and_result_dict)

                log = f"Avg. Trial: {avg_trial: 6.2f} "
                print(log, end="")
                print(f"== {time.time() - start_time:.2f} seconds")
    json.dump(result_list, wf, indent=4)

    # find_words_excluding_char(total_words, "fghtoceansurlypowerkemps", limit_n=10)
```

## Reference

- [wikipedia - wordle](https://en.wikipedia.org/wiki/Wordle)
