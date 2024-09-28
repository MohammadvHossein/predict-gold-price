from naive_bayes import naive_bayes_classifier
from XG_boost import XG_boost_classifier
from evaluations import evaluation

print("naive_bayes :")
result = naive_bayes_classifier.classifier()
print(evaluation.evaluation(result, data='evaluations/test.csv'), "\n")

print("XG_boost :")
result = XG_boost_classifier.classifier()
print(evaluation.evaluation(result, data='evaluations/test.csv'), "\n")
