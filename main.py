from naive_bayes import naive_bayes_classifier
from XG_boost import XG_boost_classifier
from Random_Forest import Random_Forest_classifier
from evaluations import evaluation
from EMA import EMA
from ensemble import ensemble
from MACD_and_SSL import MACD_SSL
from MACD import MACD
from SSL import SSL

# print("naive_bayes :")
# result = naive_bayes_classifier.classifier()
# print(evaluation.evaluation(result, data='evaluations/test.csv'), "\n")

# print("XG_boost :")
# result = XG_boost_classifier.classifier()
# print(evaluation.evaluation(result, data='evaluations/test.csv'), "\n")

# print("Random_Forest :")
# result = Random_Forest_classifier.classifier()
# print(evaluation.evaluation(result, data='evaluations/test.csv'), "\n")

emaA , emaC = EMA()

ensembleA , ensembleC = ensemble()

macd_sslA , macd_sslC = MACD_SSL()

macdA , macdC = MACD()

sslA , sslC = SSL()

print("EMA : ".center(12), "|" , f"Accuracy : {emaA}".center(17) ,"|", f"Confidence : {emaC}".center(15))
print("ensemble : ".center(12), "|" , f"Accuracy : {ensembleA}".center(17) ,"|", f"Confidence : {ensembleC}".center(15))
print("MACD_SSL : ".center(12), "|" , f"Accuracy : {macd_sslA}".center(17) ,"|", f"Confidence : {macd_sslC}".center(15))
print("MACD : ".center(12), "|" , f"Accuracy : {macdA}".center(17) ,"|", f"Confidence : {macdC}".center(15))
print("SSL : ".center(12), "|" , f"Accuracy : {sslA}".center(17) ,"|", f"Confidence : {sslC}".center(15))