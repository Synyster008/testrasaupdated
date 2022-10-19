
from typing import Any, Text, Dict, List, Union

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


from rasa_sdk import Action

import time
import datetime
import pandas as pd
from pprint import pprint
from datetime import datetime
from datetime import timedelta
from rasa_sdk.events import ReminderScheduled
from rasa_sdk.events import (
	SlotSet,
	UserUtteranceReverted,
	ConversationPaused,
	EventType,
	AllSlotsReset
)
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import chart_studio.plotly as py
import plotly.graph_objs as go


class ActionIterate(Action):
	def name(self):
		return 'action_itr'
	def run(self,dispatcher,tracker,domain):
		list=[]
		list.append("Arm Circles")
		list.append("Lunges")
		list.append("Jumping Jacks")
		list.append("High stepping")
		list.append("Side Planks")
		list.append("Squats")
		iter=int(tracker.get_slot('iterator'))
		#lst.extend([5, 6, 7])
		print("Func iterate, list[iter]",list[iter])
		
		SlotSet("iterator",iter)
		print("Func iterate,iterator",iter)
		iter += 1
		return[SlotSet("ex_type_slot",list[iter]),SlotSet("iterator",str(iter))]

class ActionExr2(Action):
	def name(self):
		return 'action_exr2'
	def run(self,dispatcher,tracker,domain):
		print("Before")
		data=pd.read_csv("Daily_Fitness.csv",encoding='unicode_escape',engine="python")		
		df=pd.DataFrame(data)
		ex_name=tracker.get_slot('ex_type_slot')
		print("slot",ex_name)
		data=df[df["name"].str.contains(str(ex_name))]
		print("data",data)
		
		
		for i,j in data.iterrows():
			link= j['info_link']
			#dispatcher.utter_message(link)

			#buttons = [{"title": "FACED DIFFICULTY", "payload":link}]
			print(j['name'],"\n",j['description'],"\nReps:",j['reps'],
				"Calorie:",j['calorie'],"\nGif:",j['gif'],"\nReadMore",j['info_link'])
			dispatcher.utter_message(str(j['name'])+"\n"+j['description']+"\nReps:"+str(j['reps'])+
				"  Calorie:"+str(j['calorie'])+"\nGif:"+str(j['gif'])+"\n")
			#dispatcher.utter_message("abc:\n",buttons)


### functions for cardio workout
class ActionIterate_C(Action):
	def name(self):
		return 'action_itr_c'
	def run(self,dispatcher,tracker,domain):
		list=[]
		iterc=int(tracker.get_slot('iterator_c'))
		list.extend(["Skaters", "Squat jump", "Burpees","Bicycle crunches","Flutter kicks"])
		print("Func iterate, list[iter]",list[iterc])
		
		SlotSet("iterator_c",iterc)
		print("Func iterate,iterator",iterc)
		iterc += 1
		return[SlotSet("ex_type_slot_c",list[iterc]),SlotSet("iterator_c",str(iterc))]

class ActionExrC(Action):
	def name(self):
		return 'action_exr_c'
	def run(self,dispatcher,tracker,domain):
		print("Before")
		data=pd.read_csv("Cardio.csv",engine="python")		
		df=pd.DataFrame(data)
		ex_name=tracker.get_slot('ex_type_slot_c')
		print("slot",ex_name)
		data=df[df["name"].str.contains(str(ex_name))]
		print("data",data)
		for i,j in data.iterrows():
			print(j['name'],"\n",j['description'],"\nReps:",j['reps'],
				"Calorie:",j['calorie'],"\nGif:",j['gif'],"\nReadMore",j['info_link'])
			dispatcher.utter_message(str(j['name'])+"\n"+j['description']+"\n"+str(j['gif']))

### functions for yoga
class ActionIterate_Y(Action):
	def name(self):
		return 'action_itr_y'
	def run(self,dispatcher,tracker,domain):
		list=[]
		itery=int(tracker.get_slot('iterator_y'))
		list.extend(["Paschimottanasana", "Urdhva mukha svanasana", "Ardha chandrasana","Dhanurasana"," Ustrasana","Urdhva dhanurasana"])
		print("Func iterate, list[iter]",list[itery])
		
		SlotSet("iterator_y",itery)
		print("Func iterate,iterator",itery)
		itery += 1
		return[SlotSet("ex_type_slot_y",list[itery]),SlotSet("iterator_y",str(itery))]

class ActionExrY(Action):
	def name(self):
		return 'action_exr_y'
	def run(self,dispatcher,tracker,domain):
		print("Before")
		data=pd.read_csv("Yoga.csv",engine="python")		
		df=pd.DataFrame(data)
		ex_name=tracker.get_slot('ex_type_slot_y')
		print("slot",ex_name)
		data=df[df["name"].str.contains(str(ex_name))]
		print("data",data)
		for i,j in data.iterrows():
			print(j['name'],"\n",j['description'],"\nGif:",j['gif'],"ReadMore",j['info_link'])
			dispatcher.utter_message(str(j['name'])+j['description']+str(j['gif'])+"\n Benefits:"+j['benefits'])


class ActionGraph(Action):
	def name(self):
		return 'action_graph'
	def run(self,dispatcher,tracker,domain):
		random_x = np.linspace(0, 2, 100)
		random_y1 = [23,45,66,78,99,100]
		random_y2 = [20,40,70,72,95,110]
		
		x=["BP","A","B","C"]
		

		today=datetime.today().strftime('%Y-%m-%d')
		trace0 = go.Scatter(x=["BP","A","B","C","D"], y=random_y1,
							mode='lines+markers',
							name=today)


		trace1 = go.Scatter(x=["BP","A","B","C","D"], y=random_y2,
							mode='lines+markers',
							name=today)
		data = [trace0, trace1]
		#data = [trace1]
		str1=py.plot(data, filename = 'basic')
		print(str1)
		dispatcher.utter_message(str1)


class ActionQuery(Action):
	def name(self):
		return 'action_query'
	def run(self,dispatcher,tracker,domain):
		try: 
			from googlesearch import search 
		except ImportError: 
			print("No module named 'google' found") 
		q=tracker.get_slot('query_slot')
		print(q)
		#query = "Diabetes test packages with fees"	

		for j in search(q, tld="com", num=5, stop=1, pause=5): 
			print(j) 
			buttons = [{"title": "BOOK NOW ", "payload": j}]
			dispatcher.utter_message(buttons)


class ActionRecipe(Action):
	def name(self):
		return 'action_recipe'
	def run(self,dispatcher,tracker,domain):
		cal=tracker.get_slot('calorietype')
		print(cal)
		mainIng=tracker.get_slot('ing')
		print(mainIng)
		diet=tracker.get_slot('diettype')
		print(diet)
		pref=tracker.get_slot('foodpreftype')
		print(pref)
		r = requests.get("https://api.edamam.com/search?q="+mainIng+
		"&app_id=65915dbb&app_key=b34c4ac5a893035e6894b2ae1945c83e&from=0&to=5&calories="+cal+"&health="+pref)
		data=r.json()
		data2= data['hits']
		""" results=[]
		results1=[]
		k=0
		for i,j in data.iterrows():
			results.append(j)
			results1.append(results[k].to_string())
			k+=1 """


		for x in data2:
			data3=x['recipe']
			#dispatcher.utter_message(str(data3['label'])+"\n"+str(data3['shareAs']))
			print(data3['label'],"\n", data3['shareAs'])
			df=pd.DataFrame(data3['ingredientLines'])
			for i in df:
				print(df[i].to_string(index=False))
				df=pd.DataFrame(data3['totalNutrients'])
				print(df.transpose())
				df4=df.transpose()
				df4['quantity']=(df4['quantity'].map('{:,.2f}'.format)).astype(str)
				df4['new'] = df4[['quantity', 'unit']].apply(lambda x: ''.join(x), axis=1)
				print(df4['new'])
				""" results=[]
				results1=[]
				k=0
				for i,j in df.iterrows():

					results.append(j)
					results1.append(results[k].to_string())
					k+=1 """
				dispatcher.utter_message(str(data3['label'])+"\n"+str(data3['shareAs'])+"\n"+str(df4['new']))


import nexmo
import json
#import geocoder
class ActionSendSMS(Action):
	def name(self):
		return 'action_SMS'
	def run(self,dispatcher,tracker,domain):
		URL = 'https://www.sms4india.com/api/v1/sendCampaign'
		req_params = {
		'apikey':'KXVMEVS3D67EWJ8UQBIIBEN05MWXXGM8',
		'secret':'3EB5RM2J4WQG21SN',
		'usetype':'stage',
		'phone': '918105128205',
		'message':"https://maps.google.com"+"?saddr=Current+Location",
		'senderid':'spandanam174@gmail.com'
		}
		response=requests.post(URL, req_params)
		print(response.text)
		dispatcher.utter_message("Message sent successfully!!!")

import webbrowser
import urllib
class ActionOpenMap(Action):
	def name(self):
		return 'action_map'
	def run(self,dispatcher,tracker,domain):
		loc_query=tracker.get_slot('location_type')
		loc_query2=str(loc_query).replace(" ", "+")
		#webbrowser.open('https://maps.google.com/?saddr=My%20Location')
		dispatcher.utter_message(text="https://www.google.com/maps/search/"+loc_query2+"+near+me")
		#dispatcher.utter_message("https://big.assets.huffingtonpost.com/3PLANKSARAH.gif")
class ActionLocationCSV(Action):
	def name(self):
		return 'action_loc_csv'
	def run(self,dispatcher,tracker,domain):
		loc_query=tracker.get_slot('location')
		dispatcher.utter_message(text="https://www.google.com/maps/search/hospitals+in+"+str(loc_query))


class ActionSetReminder(Action):
	def name(self):
		return "action_Set_Reminder"

	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_message("Okay! Your reminder has been set successfully!")
		return [ReminderScheduled( "action_Get_Reminder", datetime.now() + timedelta(minutes=1),name=None, kill_on_user_message=False, timestamp=None)]



class ActionGetReminder(Action):
	def name(self):
		return "action_Get_Reminder"

	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_message("As per the reminder you set, its time to take your medicine.") 
		medi=(tracker.get_slot('medicine'))
		dispatcher.utter_message("Please take your " +(medi) + " medicine!")
		return []

class Information_Form3(FormAction):
	"""Example of a custom form action"""

	def name(self) -> Text:
	   
		return "reminder_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:

		return ["reminder"]

	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
		
		return {
			"reminder": [self.from_entity(entity="reminder"),self.from_text(intent=None)],
		}

	
	def validate_reminder(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> Dict[Text, Any]:
	

		if 'reminder' in value or 'list' in value:
			dispatcher.utter_message("Okay! I will store this reminder!")
			print("Okay! I will store this reminder!")
			return {"reminder": value}
		else:
			dispatcher.utter_message("Your reminder has not been added")
			print("Your reminder has not been added")
			return {"reminder": None} 
        
	def submit(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> List[Dict]:
		
		
		dispatcher.utter_message("Thank you for using this service!")
		return []

class ActionResetAllSlots(Action):

    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]

class ActionAddReminder(Action):
	def name(self):
		return "action_add_Reminder"

	def run(self, dispatcher, tracker, domain):
		reminder=tracker.get_slot('reminder')
		print(reminder)
		print("Opening file for storing...")
		with open('Reminder.txt', "a+") as f:
			f.seek(0)
			data = f.read(100)
			if len(data) > 0:
				f.write("\n")
			f.write(reminder)
			print("Your reminder has been added in the list!")
			dispatcher.utter_message("Your reminder has been added in the list!")


class ActionShowReminder(Action):
	def name(self):
		return "action_show_Reminder"

	def run(self, dispatcher, tracker, domain):
		
		with open('Reminder.txt', "r") as f:
			f.seek(0)
			contents=f.read()
			print(contents)
			data = f.read(100)
			if len(data) == 0:
				dispatcher.utter_message("You don't have any reminders left for today!")

			dispatcher.utter_message("The following our the reminders as per you set!")
			dispatcher.utter_message(contents)
	


	
		
class ActionStoreEntityExtractor(Action):
	"""Takes the entity which the user wants to extract and checks
		what pipelines can be used.
	"""

	def name(self) -> Text:
		return "action_store_entity_extractor"

	def run(self, dispatcher, tracker, domain) -> List[EventType]:
		spacy_entities = ["place", "date", "name", "organisation"]
		duckling = [
			"money",
			"duration",
			"distance",
			"ordinals",
			"time",
			"amount-of-money",
			"numbers",
		]

		entity_to_extract = next(tracker.get_latest_entity_values("entity"), None)

		extractor = "CRFEntityExtractor"
		if entity_to_extract in spacy_entities:
			extractor = "SpacyEntityExtractor"
		elif entity_to_extract in duckling:
			extractor = "DucklingHTTPExtractor"

		return [SlotSet("entity_extractor", extractor)]


import dateutil.parser


class ActionGetDate(Action):

	def name(self):
		return 'action_split_date_time' #****This is used in the story!****

	def run(self, dispatcher, tracker, domain):
		time_slot= tracker.get_latest_entity_values('time')
		#dictData = next(tracker.get_latest_entity_values('time'), None)
		#date = dictData['value']
		datetime_obj = dateutil.parser.parse(next(time_slot))
		#humanDate = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
		
		timeStr = datetime_obj.strftime("%H:%M:%S")
		#datetime_object = datetime.strptime(timeStr, '%H:%M:%S')
		#time = datetime_obj.time()
		datetimeFormat = '%Y-%m-%d %H:%M:%S'
		date1 =str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
		date2 = str(datetime_obj.strftime('%Y-%m-%d %H:%M:%S'))
		diff = datetime.strptime(date1,datetimeFormat)- datetime.strptime(date2,datetimeFormat)
		sec=int(diff.total_seconds())*(-1)
		#if(sec<0):
		#	dispatcher.utter_message("Time invalid")
		#	return
		print(sec)
		dispatcher.utter_message("Okay, I got this time: " + timeStr + " and your reminder has been set successfully!")
		# + ". This is the full date: " + humanDate)
		return [ReminderScheduled("action_Get_Reminder",datetime.now() + timedelta(seconds=sec),name=None, kill_on_user_message=False, timestamp=None)]
		#return [SlotSet("time_slot", timeStr)]

		
""" class ActionLocationCSV(Action):
	def name(self):
		return 'action_loc_csv'
	def run(self,dispatcher,tracker,domain):
		df = pd.read_csv("bangloreCSV.csv")
		loc_query=tracker.get_slot('location')
		data=df[df["Address"].str.contains(str(loc_query))]
		results=[]
		results1=[]
		k=0
		for i,j in data.iterrows():
			results.append(j)
			results1.append(results[k].to_string())
			k+=1

		if(len(results)==0):
			dispatcher.utter_message("Location not found")
			return
		for x in range(k):
			print(results1[x])
		for x in range(k):
			dispatcher.utter_message(results1[x])	
		return[]

class ActionZipCode(Action):
	def name(self):
		return 'action_zip_code'
	def run(self,dispatcher,tracker,domain):
		df = pd.read_csv("bangloreCSV.csv")
		
		loc_query=tracker.get_slot('zipCode')
		data=df[df["Pin Code"]==int(loc_query)]
		results=[]
		results1=[]
		k=0
		for i,j in data.iterrows():
			results.append(j)
			results1.append(results[k].to_string())
			k+=1

		if(len(results)==0):
			dispatcher.utter_message("Zip Code not found")
			return

		for x in range(k):
			print(results1[x])
		for x in range(k):
			dispatcher.utter_message(results1[x])	
		return[]
		 """
	
class ActionExercise(Action):
	def name(self):
		return 'action_exr'
	def run(self,dispatcher,tracker,domain):
		df = pd.read_csv("Exercise.csv")
		
		exr_query=tracker.get_slot('exercise_name')
		data=df[df["Name"].str.contains(str(exr_query))]
		results=[]
		results1=[]
		k=0
		for i,j in data.iterrows():
			results.append(j['Steps'])
			results1.append(results[k].to_string())
			k+=1

		if(len(results)==0):
			dispatcher.utter_message("Exercise not found")
			return
		for x in range(k):
			print(results1[x])
		for x in range(k):
			dispatcher.utter_message(results1[x])	
		return[]
		
import json
class ActionRemedyCSV(Action):
	def name(self):
		return 'action_remedy_csv'
	def run(self,dispatcher,tracker,domain):
		#df = pd.read_csv("remedies.csv",engine='python')
		
		loc_query=tracker.get_slot('ask_remedy')
		print(loc_query)
		with open('remedy_json.json', 'r') as f:
			distros_dict = json.load(f)
		str1=loc_query.lower()
		
		for x in distros_dict:
			str2=x['Disease'].lower()
			if str1 in str2 or ((str1.count(str2))>0):
				print(str(x['Home_Remedy']))
				dispatcher.utter_message(str(x['Home_Remedy']))
	
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from time import sleep

class ActionSymptoms(Action):
	def name(self):
		return 'action_symp'
	def run(self,dispatcher,tracker,domain):
		data = pd.read_csv("Training.csv")
		df = pd.DataFrame(data)
		df2=df
		cols=df.columns
		#cols = cols[:-1]
		
		df_new=pd.DataFrame(0,index=range(1),columns=cols)
		#symptom_var=input("Enter you symptom")
		symptom_var="skin_rash"
		#df_new['prognosis']=df['prognosis']
		df3=df[df[symptom_var]==1]
		

		list_append=[]
		for index, row in df3.iterrows():
			for word in df3: 
				if(row[word]==1): 
					if(word not in list_append):
						list_append.append(word)

	
		df_check=pd.DataFrame(int(-1),index=list_append,columns=range(1))


		for index, row in df3.iterrows():
			for word in df3: 
				if(row[word]==1):					 
					if((word!=symptom_var)&(df_check.loc[word]==-1 ).bool()):
						print("X")
						dispatcher.utter_message("Do you have ",word)
						print("Y")
						ActionbtnDisplay.run(self,dispatcher,tracker,domain)
						print("Z")
						sleep(15)
						if((tracker.latest_message)['text']=="/affirm2"):
							df_new[word]=1
							df_check.loc[word]=1
						else:
							df_new[word]=0
							df_check.loc[word]=1
		
		#cols2=cols[:-1]	
		df4=df.drop('prognosis', axis=1)				
		x = data[df4.columns]
		y = data['prognosis']
		x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
		print  ("Decision Tree")
		dt = DecisionTreeClassifier()
		clf_dt=dt.fit(x_train,y_train)
		y_pred=dt.predict(data[df4.columns])
		for result in y_pred:
			print(result)
		for result in y_pred:
			dispatcher.utter_message(str(result))
		return[]


class ActionbtnDisplay(Action):
	def name(self):
		return 'action_btn_display'
	def run(self,dispatcher,tracker,domain):
		print("action button display")
		return [ReminderScheduled( "utter_symp_present", datetime.now()+timedelta(seconds=3),
		name=None, kill_on_user_message=False, timestamp=None)]

import requests
from datetime import datetime


class ActionNews(Action):
	def name(self):
		return 'action_news'
	def run(self,dispatcher,tracker,domain):
		today_date=datetime.today().strftime('%Y-%m-%d')
		url = ('http://newsapi.org/v2/everything?'
	   'q=corona&'
	   'from=today_date&'
	   'sortBy=popularity&'
	   'apiKey=1f8d2ce6263f4d76af1206023d997ee4')

		r = requests.get(url)

		data=r.json()
		df=pd.DataFrame(data)
		df2=df.head(10)
		for x in df2['articles']:
				print(str(x['description']),"\n")
				dispatcher.utter_message(x['title']+"\n"+x['description']+"\nRead More:"+x['url'])
	""" 			dispatcher.utter_message(x['description'])
				dispatcher.utter_message(x['urlToImage'])
				dispatcher.utter_message(x['url']) 


				for x in data:
					if x=="articles":
						for y in data.get(x):
							for r in y:
								print(str(y[r]),"\n")
								result = json.dumps(y[r]) 
								for m in result:
									dispatcher.utter_message(m,"\n")

						 """
						
import socket 

class ActionIP(Action):
	def name(self):
		return 'action_ip'
	def run(self,dispatcher,tracker,domain):   
		hostname = socket.gethostname()	
		IPAddr = socket.gethostbyname(hostname)	
		print("Your Computer Name is:" + hostname)	
		print("Your Computer IP Address is:" + IPAddr)  
		dispatcher.utter_message(hostname)
		dispatcher.utter_message(IPAddr)  


class Information_Form(FormAction):
	"""Example of a custom form action"""

	def name(self) -> Text:
	   
		return "information_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:

		return ["name", "gender", "age","email", "contact", "emergencycont","preconditions","preexinfo"]

	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
		
		return {
			"name": [self.from_entity(entity="name"),self.from_text(intent=None)],
			"gender": [self.from_entity(entity="gender"),self.from_text(intent=None)],
			"age": [self.from_entity(entity="age"),self.from_text(intent=None)],
			"email" : [self.from_entity(entity="email"),self.from_text(intent=None)],
			"contact": [self.from_entity(entity="contact"),self.from_text(intent=None)],
			"emergencycont": [self.from_entity(entity="emergencycont"),self.from_text(intent=None)],
			"preconditions": [self.from_entity(entity="preconditions"),self.from_text(intent=None)],
			"preexinfo": [self.from_entity(entity="preexinfo"),self.from_text(intent=None)]
		
			
		}


	@staticmethod
	def is_int(string: Text) -> bool:
		"""Check if a string is an integer"""

		try:
			int(string)
			return True
		except ValueError:
			return False

	def validate_age(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> Dict[Text, Any]:
	

		if self.is_int(value) and int(value) > 0:
			return {"age": value}
		else:
			dispatcher.utter_message("Please provide appropriate age input")
			return {"age": None}
	
	def validate_gender(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> Dict[Text, Any]:
	

		if "male" in value or "Male" in value or "m" in value or "M" in value or "female" in value or "Female" in value or "F" in value or "f"in value or "Others" in value or "Other" in value or "other" "male" in value:
			return {"gender": value}
		else:
			dispatcher.utter_message("Please provide appropriate gender input")
			return {"gender": None}
	
	def validate_email(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> Dict[Text, Any]:
	

		if "@" in value:
			return {"email": value}
		else:
			dispatcher.utter_message("Please provide appropraite email-id")
			return {"email": None}
	
	def validate_contact(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> Dict[Text, Any]:
	

		if self.is_int(value) and len(value)==10:
			return {"contact": value}
		else:
			dispatcher.utter_message("Please provide the appropriate contact number input (For Indian Regions only, without code)")
			return {"contact": None}
	
	def validate_emergencycont(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> Dict[Text, Any]:
	

		if self.is_int(value) and len(value)==10:
			return {"emergencycont": value}
		else:
			dispatcher.utter_message("Please provide the appropriate emergency contact number (For Indian Regions only, without code)")
			return {"emergencycont": None}
	
	

	def submit(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> List[Dict]:
		
		# utter submit template
		dispatcher.utter_message(template="utter_thaninit")
		return []


	  
class Information_Form2(FormAction):
	"""Example of a custom form action"""

	def name(self) -> Text:
	   
		return "recipe_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:

		return ["ing", "diettype", "foodpreftype","calorietype"]

	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
		
		return {
			"ing": [self.from_entity(entity="ing"),self.from_text(intent=None)],
			"calorietype" : [self.from_entity(entity="calorietype"),self.from_text(intent=None)],
			"foodpreftype": [self.from_entity(entity="foodpreftype"),self.from_text(intent=None)],
			"diettype": [self.from_entity(entity="diettype"),self.from_text(intent=None)]
			
			
			
		}


	def submit(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> List[Dict]:
		
		# utter submit template
		dispatcher.utter_message(template="utter_recdisp")
		return []
	  


