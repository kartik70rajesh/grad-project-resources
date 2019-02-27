import csv
import pandas as pd


dataset1 = pd.read_csv("Truefinal.csv",encoding = 'unicode_escape')
dataset2 = pd.read_csv("Fakefinal.csv",encoding = 'unicode_escape')

dataset1 = dataset1.drop(columns=[''])



#partitions = {
#     #Input features
#         'predictor': {
#             'email': {
#                 'dataset': {
#                     'original': dataset.a_body,
#                     'cleaned': None,
#                     'vectorised': None,
#                     'training': None,
#                     'testing': None
#                 },
#                 'tfidf': {}
#             },
#         },
#         #Targets 
#         'label': {
#             'queue': {
#                 'dataset': {
#                     'original': dataset.queue,
#                     'vectorised': None,
#                     'training': None,
#                     'testing': None
#                 },
#                 'model': {},
#                 'accuracy': {},
#                 'label_encoder': {}
#             },
#             'type': {
#                 'dataset': {
#                     'original': dataset.type,
#                     'vectorised': None,
#                     'training': None,
#                     'testing': None
#                 },
#                 'model': {},
#                 'accuracy': {},
#                 'label_encoder': {}
#             },
#             'priority': {
#                 'dataset': {
#                     'original': dataset.priority,
#                     'vectorised': None,
#                     'training': None,
#                     'testing': None
#                 },
#                 'model': {},
#                 'accuracy': {},
#                 'label_encoder': {}


#             }
#         }
# }

