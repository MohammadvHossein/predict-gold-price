from naive_bayes import naive_bayes_classifier
from evaluations import evaluation

result = naive_bayes_classifier.classifier()
print(evaluation.evaluation(result ,data='evaluation_data_test.csv'))

