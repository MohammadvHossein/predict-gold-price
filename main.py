from naive_bayes import naive_bayes_classifier
from evaluations import evaluation

result = naive_bayes_classifier.classifier()
print(evaluation.evaluation(result ,data='evaluations/test.csv'))

