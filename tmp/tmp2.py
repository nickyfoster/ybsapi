'''
import numpy as np

inout_text = ['I love my beautiful cat', 'my mouse is pretty huge', 'my kitten is gorgeous']

predict_result = (np.array(
    [[0.837464, 0.927263, 0.63782833],
     [0.71536743, 0.8627383, 0.99819393],
     [0.78283, 0.9237633, 0.627152]]), np.array(['dog', 'cat', 'mouse']))


def process_n_best_results(predict_results: tuple, n: int):
    Y_pred = predict_results[0]
    class_names = predict_results[1]
    n_largests = np.argsort(-Y_pred)[:, :n]
    n_best = []

    for i in range(len(n_largests)):
        tmp = []
        for y in n_largests[i]:
            result = {}
            result['class'] = class_names[y]
            result['score'] = Y_pred[i][y]
            tmp.append(result)
        n_best.append(tmp)

    return n_best


print(process_n_best_results(predict_result, 2))
'''



# test


z = [x for x in range(5) for y in range(5)]




print(z)












