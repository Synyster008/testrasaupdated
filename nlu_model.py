import sys,os
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
from rasa_nlu import config

def train_nlu(data, config, model_dir):
	training_data = load_data(data)
	trainer = Trainer(RasaNLUModelConfig(config))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'HC BOT')
	
'''def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/weatherbot')
	#print(interpreter.parse("I am planning my holiday in Chennai, I wonder what is the weather out there."))
'''	
if __name__ == '__main__':
	#train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
    training_data = load_data('./data/data.json')
    trainer = Trainer(config.load('config_.json'))
    trainer.train(training_data)
    model_directory = trainer.persist('./models/nlu' ,  fixed_model_name = 'HC BOT')
    #run_nlu()