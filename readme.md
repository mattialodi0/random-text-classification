# Random text classification

The goal of this project is to develop a simple and fast LM to dect fake vs real strings (where fake ones are generated at random) that will be used for real-time evaluation.

## Ngram Model
The simplest possible model, not particularly effective

| model | top_k | acc | prec | rec | F1 | adv100@10 | adv@10060 | adv100@110 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2-gram | 150 | 0.9900 | 0.9823 | 0.9980 | 0.9901 | 1 | 1 | 1 |
| 3-gram | 150 | 0.9570 | 0.9224 | 0.9980 | 0.9587 | 0.9 | 0.99 | 1 |
| 4-gram | 150 | 0.9620 | 0.9342 | 0.9940 | 0.9632 | 0.4 | 0.71 | 0.72 |
| 5-gram | 150 | 0.9760 | 0.9830 | 0.9680 | 0.9758 | 0.05 | 0.16 | 0.26 |
| 6-gram | 150 | 0.9670 | / | / | 0.9659 | / | 0.3 | 0.1 |

## 1d CNN
A simple model composed of an embedding layer, 3 1d CNN layers, a dropout layer and a linear layer.
Here the focus is on the training, to make the model generalize better.

### base training
| model | epochs | lr | acc | prec | rec | F1 | adv@10 | adv@60 | adv@110 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 layers, 128 filters | 5 | 1e-3 | 1 | 1 | 1 | 1 | 1 | 0.7 | 0 |

### second training
| model | epochs | lr | acc | prec | rec | F1 | adv@10 | adv@60 | adv@110 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 layers, 128 filters | 10 | 1e-3 | 1 | 1 | 1 | 1 | 1 | 0.6 | 0.1 |

### boosted training
| model | epochs | lr | acc | prec | rec | F1 | adv@10 | adv@60 | adv@110 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 layers, 128 filters | 5 | 1e-3 | 1 | 1 | 1 | 1  | 1 | 0.5 | 0.1 |


## Transformer
The transformer is the slowest and most complex model but can't acheive the results of the 1d CNN
| model | epochs | lr | acc | prec | rec | F1 | auc | adv100@10 | adv100@60 | adv100@110 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 layers, 256 hidden dim | 5 | 1e-4 | 0.7670 | 0.6955 | 0.9500 | 0.8030 |  0.8290 | 1 | 1 | 0.8 |



<br/>
* advX@Y is the result of the adversarial attack iterated X times with string length Y, the lowest score the better.