from naive_bayes import naive_bayes_classifier
from XG_boost import XG_boost_classifier
from Random_Forest import Random_Forest_classifier
from evaluations import evaluation
from EMA import EMA
from ensemble import ensemble
from MACD_and_SSL import MACD_SSL
from MACD import MACD

# print("naive_bayes :")
# result = naive_bayes_classifier.classifier()
# print(evaluation.evaluation(result, data='evaluations/test.csv'), "\n")

# print("XG_boost :")
# result = XG_boost_classifier.classifier()
# print(evaluation.evaluation(result, data='evaluations/test.csv'), "\n")

# print("Random_Forest :")
# result = Random_Forest_classifier.classifier()
# print(evaluation.evaluation(result, data='evaluations/test.csv'), "\n")

EMA()

ensemble()

MACD_SSL()

MACD()
