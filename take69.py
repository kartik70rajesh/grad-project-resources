import csv

dataset = pd.read_csv("articles1.csv")
dataset= dataset.drop(columns=['id','url']

partitions = {
    #Input features
        'predictor': {
            'email': {
                'dataset': {
                    'original': dataset.a_body,
                    'cleaned': None,
                    'vectorised': None,
                    'training': None,
                    'testing': None
                },
                'tfidf': {}
            },
        },
        #Targets 
        'label': {
            'queue': {
                'dataset': {
                    'original': dataset.queue,
                    'vectorised': None,
                    'training': None,
                    'testing': None
                },
                'model': {},
                'accuracy': {},
                'label_encoder': {}
            },
            'type': {
                'dataset': {
                    'original': dataset.type,
                    'vectorised': None,
                    'training': None,
                    'testing': None
                },
                'model': {},
                'accuracy': {},
                'label_encoder': {}
            },
            'priority': {
                'dataset': {
                    'original': dataset.priority,
                    'vectorised': None,
                    'training': None,
                    'testing': None
                },
                'model': {},
                'accuracy': {},
                'label_encoder': {}


            }
        }
}