## greet
* greet
    - utter_greet
    - utter_ask_info

## info taking form
* personalize_healthcare   
    - utter_ready
* pos
    - information_form
    - form{"name": "information_form"}    
    - form{"name": null}

* personalize_healthcare   
   - utter_ready
* neg
    - utter_thank1
	


## news_path
* ask_news
- action_news


## exr_path_h1
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h1
- action_itr_h1
- slot{"ex_type_slot_h1":"Walking"}
- action_exr_h1
- utter_new_exr
- action_listen
* done_intent
- action_itr_h1
- slot{"ex_type_slot_h1":"BREATHE DEEPLY"}
- action_exr_h1
- utter_new_exr
- action_listen
* done_intent
- action_itr_h1
- slot{"ex_type_slot_h1":"Pranayama"}
- action_exr_h1
- utter_new_exr
- action_listen
* done_intent
- action_itr_h1
- slot{"ex_type_slot_h1":"SUKHASANA"}
- action_exr_h1
- utter_new_exr
- action_listen
* done_intent
- action_itr_h1
- slot{"ex_type_slot_h1":"Seated Shoulder Squeeze"}
- action_exr_h1
- utter_quit

## exr_path_h1
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h1
- action_itr_h1
- slot{"ex_type_slot_h1":"Walking"}
- action_exr_h1
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path_h1
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h1
- action_itr_h1
- slot{"ex_type_slot_h1":"Walking"}
- action_exr_h1
- utter_new_exr
- action_listen
* done_intent
- action_itr_h1
- slot{"ex_type_slot_h1":"BREATHE DEEPLY"}
- action_exr_h1
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path_h1
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h1
- action_itr_h1
- slot{"ex_type_slot_h1":"Walking"}
- action_exr_h1
- utter_new_exr
- action_listen
* done_intent
- action_itr_h1
- slot{"ex_type_slot_h1":"BREATHE DEEPLY"}
- action_exr_h1
- utter_new_exr
- action_listen
* done_intent
- action_itr_h1
- slot{"ex_type_slot_h1":"Pranayama"}
- action_exr_h1
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path_h1
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h1
- action_itr_h1
- slot{"ex_type_slot_h1":"Walking"}
- action_exr_h1
- utter_new_exr
- action_listen
* done_intent
- action_itr_h1
- slot{"ex_type_slot_h1":"BREATHE DEEPLY"}
- action_exr_h1
- utter_new_exr
- action_listen
* done_intent
- action_itr_h1
- slot{"ex_type_slot_h1":"Pranayama"}
- action_exr_h1
- utter_new_exr
- action_listen
* done_intent
- action_itr_h1
- slot{"ex_type_slot_h1":"SUKHASANA"}
- action_exr_h1
- utter_new_exr
- action_listen
* quit_intent
- utter_quit



## exr_path_h2
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h2
- action_itr_h2
- slot{"ex_type_slot_h2":"Nadi Shodhan"}
- action_exr_h2
- utter_new_exr
- action_listen
* done_intent
- action_itr_h2
- slot{"ex_type_slot_h2":"Kapal Bhati"}
- action_exr_h2
- utter_new_exr
- action_listen
* done_intent
- action_itr_h2
- slot{"ex_type_slot_h2":"Balasana"}
- action_exr_h2
- utter_new_exr
- action_listen
* done_intent
- action_itr_h2
- slot{"ex_type_slot_h2":"Badhakonasana"}
- action_exr_h2
- utter_new_exr
- action_listen
* done_intent
- action_itr_h2
- slot{"ex_type_slot_h2":"Shavasana"}
- action_exr_h2
- utter_quit

## exr_path_h2
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h2
- action_itr_h2
- slot{"ex_type_slot_h2":"Nadi Shodhan"}
- action_exr_h2
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path_h2
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h2
- action_itr_h2
- slot{"ex_type_slot_h2":"Nadi Shodhan"}
- action_exr_h2
- utter_new_exr
- action_listen
* done_intent
- action_itr_h2
- slot{"ex_type_slot_h2":"Kapal Bhati"}
- action_exr_h2
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path_h2
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h2
- action_itr_h2
- slot{"ex_type_slot_h2":"Nadi Shodhan"}
- action_exr_h2
- utter_new_exr
- action_listen
* done_intent
- action_itr_h2
- slot{"ex_type_slot_h2":"Kapal Bhati"}
- action_exr_h2
- utter_new_exr
- action_listen
* done_intent
- action_itr_h2
- slot{"ex_type_slot_h2":"Balasana"}
- action_exr_h2
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path_h2
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h2
- action_itr_h2
- slot{"ex_type_slot_h2":"Nadi Shodhan"}
- action_exr_h2
- utter_new_exr
- action_listen
* done_intent
- action_itr_h2
- slot{"ex_type_slot_h2":"Kapal Bhati"}
- action_exr_h2
- utter_new_exr
- action_listen
* done_intent
- action_itr_h2
- slot{"ex_type_slot_h2":"Balasana"}
- action_exr_h2
- utter_new_exr
- action_listen
* done_intent
- action_itr_h2
- slot{"ex_type_slot_h2":"Badhakonasana"}
- action_exr_h2
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path_h3
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h3
- action_itr_h3
- slot{"ex_type_slot_h3":"Heel and calf stretch"}
- action_exr_h3
- utter_new_exr
- action_listen
* done_intent
- action_itr_h3
- slot{"ex_type_slot_h3":"Quadriceps stretch"}
- action_exr_h3
- utter_new_exr
- action_listen
* done_intent
- action_itr_h3
- slot{"ex_type_slot_h3":"Calf raises"}
- action_exr_h3
- utter_new_exr
- action_listen
* done_intent
- action_itr_h3
- slot{"ex_type_slot_h3":"Leg extensions"}
- action_exr_h3
- utter_new_exr
- action_listen
* done_intent
- action_itr_h3
- slot{"ex_type_slot_h3":"Straight leg raises"}
- action_exr_h3
- utter_new_exr
- action_listen
* quit_intent
- utter_quit



## exr_path_h3
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h3
- action_itr_h3
- slot{"ex_type_slot_h3":"Heel and calf stretch"}
- action_exr_h3
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path_h3
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h3
- action_itr_h3
- slot{"ex_type_slot_h3":"Heel and calf stretch"}
- action_exr_h3
- utter_new_exr
- action_listen
* done_intent
- action_itr_h3
- slot{"ex_type_slot_h3":"Quadriceps stretch"}
- action_exr_h3
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path_h3
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h3
- action_itr_h3
- slot{"ex_type_slot_h3":"Heel and calf stretch"}
- action_exr_h3
- utter_new_exr
- action_listen
* done_intent
- action_itr_h3
- slot{"ex_type_slot_h3":"Quadriceps stretch"}
- action_exr_h3
- utter_new_exr
- action_listen
* done_intent
- action_itr_h3
- slot{"ex_type_slot_h3":"Calf raises"}
- action_exr_h3
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path_h3
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h3
- action_itr_h3
- slot{"ex_type_slot_h3":"Heel and calf stretch"}
- action_exr_h3
- utter_new_exr
- action_listen
* done_intent
- action_itr_h3
- slot{"ex_type_slot_h3":"Quadriceps stretch"}
- action_exr_h3
- utter_new_exr
- action_listen
* done_intent
- action_itr_h3
- slot{"ex_type_slot_h3":"Calf raises"}
- action_exr_h3
- utter_new_exr
- action_listen
* done_intent
- action_itr_h3
- slot{"ex_type_slot_h3":"Leg extensions"}
- action_exr_h3
- utter_new_exr
- action_listen
* quit_intent
- utter_quit




## exr_path_h4
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h4
- action_itr_h4
- slot{"ex_type_slot_h4":"Shoulder Circles"}
- action_exr_h4
- utter_new_exr
- action_listen
* done_intent
- action_itr_h4
- slot{"ex_type_slot_h4":"Head tilts"}
- action_exr_h4
- utter_new_exr
- action_listen
* done_intent
- action_itr_h4
- slot{"ex_type_slot_h4":"Chest Stretch"}
- action_exr_h4
- utter_new_exr
- action_listen
* done_intent
- action_itr_h4
- slot{"ex_type_slot_h4":"Side Bends"}
- action_exr_h4
- utter_new_exr
- action_listen
* done_intent
- action_itr_h4
- slot{"ex_type_slot_h4":"standing quadriceps stretch"}
- action_exr_h4
- utter_quit

## exr_path_h4
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h4
- action_itr_h4
- slot{"ex_type_slot_h4":"Shoulder Circles"}
- action_exr_h4
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path_h4
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h4
- action_itr_h4
- slot{"ex_type_slot_h4":"Shoulder Circles"}
- action_exr_h4
- utter_new_exr
- action_listen
* done_intent
- action_itr_h4
- slot{"ex_type_slot_h4":"Head tilts"}
- action_exr_h4
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path_h4
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h4
- action_itr_h4
- slot{"ex_type_slot_h4":"Shoulder Circles"}
- action_exr_h4
- utter_new_exr
- action_listen
* done_intent
- action_itr_h4
- slot{"ex_type_slot_h4":"Head tilts"}
- action_exr_h4
- utter_new_exr
- action_listen
* done_intent
- action_itr_h4
- slot{"ex_type_slot_h4":"Chest Stretch"}
- action_exr_h4
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path_h4
* ask_exr
- utter_ask_exr_type
* show_health-specific
- utter_health_specific
* show_h4
- action_itr_h4
- slot{"ex_type_slot_h4":"Shoulder Circles"}
- action_exr_h4
- utter_new_exr
- action_listen
* done_intent
- action_itr_h4
- slot{"ex_type_slot_h4":"Head tilts"}
- action_exr_h4
- utter_new_exr
- action_listen
* done_intent
- action_itr_h4
- slot{"ex_type_slot_h4":"Chest Stretch"}
- action_exr_h4
- utter_new_exr
- action_listen
* done_intent
- action_itr_h4
- slot{"ex_type_slot_h4":"Side Bends"}
- action_exr_h4
- utter_new_exr
- action_listen
* quit_intent
- utter_quit

## exr_path
* ask_exr
- utter_ask_exr_type
* show_daily_routine
- action_itr
- slot{"ex_type_slot":"Arm Circles"}
- action_exr2
- utter_new_exr
- action_listen
* done_intent
- action_itr
- slot{"ex_type_slot":"Lunges"}
- action_exr2
- utter_new_exr
- action_listen
* done_intent
- action_itr
- slot{"ex_type_slot":"Jumping Jacks"}
- action_exr2
- utter_new_exr
- action_listen
* done_intent
- action_itr
- slot{"ex_type_slot":"High stepping"}
- action_exr2
- utter_new_exr
- action_listen
* done_intent
- action_itr
- slot{"ex_type_slot":"Side Planks"}
- action_exr2
- utter_new_exr
- action_listen
* done_intent
- action_itr
- slot{"ex_type_slot":"Squats"}
- action_exr2
- utter_quit


## exr_path2
* ask_exr
- utter_ask_exr_type
* show_daily_routine
- action_itr
- slot{"ex_type_slot":"Arm Circles"}
- action_exr2
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path
* ask_exr
- utter_ask_exr_type
* show_daily_routine
- action_itr
- slot{"ex_type_slot":"Arm Circles"}
- action_exr2
- utter_new_exr
- action_listen
* done_intent
- action_itr
- slot{"ex_type_slot":"Lunges"}
- action_exr2
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path3
* ask_exr
- utter_ask_exr_type
* show_daily_routine
- action_itr
- slot{"ex_type_slot":"Arm Circles"}
- action_exr2
- utter_new_exr
- action_listen
* done_intent
- action_itr
- slot{"ex_type_slot":"Lunges"}
- action_exr2
- utter_new_exr
- action_listen
* done_intent
- action_itr
- slot{"ex_type_slot":"Jumping Jacks"}
- action_exr2
- utter_new_exr
- action_listen
* done_intent
- utter_quit

## exr_path4
* ask_exr
- utter_ask_exr_type
* show_daily_routine
- action_itr
- slot{"ex_type_slot":"Arm Circles"}
- action_exr2
- utter_new_exr
- action_listen
* done_intent
- action_itr
- slot{"ex_type_slot":"Lunges"}
- action_exr2
- utter_new_exr
- action_listen
* done_intent
- action_itr
- slot{"ex_type_slot":"Jumping Jacks"}
- action_exr2
- utter_new_exr
- action_listen
* done_intent
- action_itr
- slot{"ex_type_slot":"High stepping"}
- action_exr2
- utter_new_exr
- action_listen
* done_intent
- utter_quit

## exr_path5
* ask_exr
- utter_ask_exr_type
* show_daily_routine
- action_itr
- slot{"ex_type_slot":"Arm Circles"}
- action_exr2
- utter_new_exr
- action_listen
* done_intent
- action_itr
- slot{"ex_type_slot":"Lunges"}
- action_exr2
- utter_new_exr
- action_listen
* done_intent
- action_itr
- slot{"ex_type_slot":"Jumping Jacks"}
- action_exr2
- utter_new_exr
- action_listen
* done_intent
- action_itr
- slot{"ex_type_slot":"High stepping"}
- action_exr2
- utter_new_exr
- action_listen
* done_intent
- action_itr
- slot{"ex_type_slot":"Side Planks"}
- action_exr2
- utter_new_exr
- action_listen
* done_intent
- utter_quit




## exr_path_c
* ask_exr
- utter_ask_exr_type
* show_cardio
- action_itr_c
- slot{"ex_type_slot_c":"Skaters"}
- action_exr_c
- utter_new_exr
- action_listen
* done_intent
- action_itr_c
- slot{"ex_type_slot_c":"Squat jump"}
- action_exr_c
- utter_new_exr
- action_listen
* done_intent
- action_itr_c
- slot{"ex_type_slot_c":"Burpees"}
- action_exr_c
- utter_new_exr
- action_listen
* done_intent
- action_itr_c
- slot{"ex_type_slot_c":"Bicycle crunches"}
- action_exr_c
- utter_new_exr
- action_listen
* done_intent
- action_itr_c
- slot{"ex_type_slot_c":"Flutter kicks"}
- action_exr_c
- utter_quit


## exr_pathc2
* ask_exr
- utter_ask_exr_type
* show_cardio
- action_itr_c
- slot{"ex_type_slot_c":"Skaters"}
- action_exr_c
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path
* ask_exr
- utter_ask_exr_type
* show_cardio
- action_itr_c
- slot{"ex_type_slot_c":"Skaters"}
- action_exr_c
- utter_new_exr
- action_listen
* done_intent
- action_itr_c
- slot{"ex_type_slot_c":"Squat jump"}
- action_exr_c
- utter_new_exr
- action_listen
* quit_intent
- utter_quit



## exr_pathc3
* ask_exr
- utter_ask_exr_type
* ask_exr
- utter_ask_exr_type
* show_cardio
- action_itr_c
- slot{"ex_type_slot_c":"Skaters"}
- action_exr_c
- utter_new_exr
- action_listen
* done_intent
- action_itr_c
- slot{"ex_type_slot_c":"Squat jump"}
- action_exr_c
- utter_new_exr
- action_listen
* done_intent
- action_itr_c
- slot{"ex_type_slot_c":"Burpees"}
- action_exr_c
- utter_new_exr
- action_listen
* quit_intent
- utter_quit

## exr_path_c4
* ask_exr
- utter_ask_exr_type
* show_cardio
- action_itr_c
- slot{"ex_type_slot_c":"Skaters"}
- action_exr_c
- utter_new_exr
- action_listen
* done_intent
- action_itr_c
- slot{"ex_type_slot_c":"Squat jump"}
- action_exr_c
- utter_new_exr
- action_listen
* done_intent
- action_itr_c
- slot{"ex_type_slot_c":"Burpees"}
- action_exr_c
- utter_new_exr
- action_listen
* done_intent
- action_itr_c
- slot{"ex_type_slot_c":"Bicycle crunches"}
- action_exr_c
- utter_new_exr
- action_listen
* quit_intent
- utter_quit

## exr_path_y
* ask_exr
- utter_ask_exr_type
* show_yoga
- action_itr_y
- slot{"ex_type_slot_y":"Paschimottanasana"}
- action_exr_y
- utter_new_exr
- action_listen
* done_intent
- action_itr_y
- slot{"ex_type_slot_y":"Urdhva mukha svanasana"}
- action_exr_y
- utter_new_exr
- action_listen
* done_intent
- action_itr_y
- slot{"ex_type_slot_y":"Ardha chandrasana"}
- action_exr_y
- utter_new_exr
- action_listen
* done_intent
- action_itr_y
- slot{"ex_type_slot_y":"Dhanurasana"}
- action_exr_y
- utter_new_exr
- action_listen
* done_intent
- action_itr_y
- slot{"ex_type_slot_y":"Ustrasana"}
- action_exr_y
- utter_quit

## exr_path_y
* ask_exr
- utter_ask_exr_type
* show_yoga
- action_itr_y
- slot{"ex_type_slot_y":"Paschimottanasana"}
- action_exr_y
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path_y
* ask_exr
- utter_ask_exr_type
* show_yoga
- action_itr_y
- slot{"ex_type_slot_y":"Paschimottanasana"}
- action_exr_y
- utter_new_exr
- action_listen
* done_intent
- action_itr_y
- slot{"ex_type_slot_y":"Urdhva mukha svanasana"}
- action_exr_y
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path_y
* ask_exr
- utter_ask_exr_type
* show_yoga
- action_itr_y
- slot{"ex_type_slot_y":"Paschimottanasana"}
- action_exr_y
- utter_new_exr
- action_listen
* done_intent
- action_itr_y
- slot{"ex_type_slot_y":"Urdhva mukha svanasana"}
- action_exr_y
- utter_new_exr
- action_listen
* done_intent
- action_itr_y
- slot{"ex_type_slot_y":"Ardha chandrasana"}
- action_exr_y
- utter_new_exr
- action_listen
* quit_intent
- utter_quit


## exr_path_y
* ask_exr
- utter_ask_exr_type
* show_yoga
- action_itr_y
- slot{"ex_type_slot_y":"Paschimottanasana"}
- action_exr_y
- utter_new_exr
- action_listen
* done_intent
- action_itr_y
- slot{"ex_type_slot_y":"Urdhva mukha svanasana"}
- action_exr_y
- utter_new_exr
- action_listen
* done_intent
- action_itr_y
- slot{"ex_type_slot_y":"Ardha chandrasana"}
- action_exr_y
- utter_new_exr
- action_listen
* done_intent
- action_itr_y
- slot{"ex_type_slot_y":"Dhanurasana"}
- action_exr_y
- utter_new_exr
- action_listen
* quit_intent
- utter_quit




## graph path
* graph_ask
- action_graph



## query_path
* query_ask
- slot{"query_slot":"order crocin tablets"}
- action_query

## query_path
* query_ask
- slot{"query_slot":"General Physicians avaliable today"}
- action_query



## recipe_path
* recipe_ask
    - recipe_form
    - form{"name": "recipe_form"}
    - action_recipe    
    - form{"name": null}

## reminder_path
* reminder_general
    - action_reset_all_slots
    - reminder_form
    - form{"name": "reminder_form"}
    - action_add_Reminder   
    - form{"name": null}


* reminder_show
   - action_show_Reminder


<!--
## recipe_path
* recipe_ask
- utter_food_ask
* main_ing
- slot{"ing":"egg"}
- utter_calorie_pref
* calorie_intent
- slot{"calorie_type":"100-300"}
- utter_diet_ask
* diet_intent
- slot{"diet_type":"balanced"}
- utter_food_pref
* food_pref_intent
- slot{"food_pref_type":"vegan"}
- action_recipe
-->

## map path
* ask_map
- slot{"location_type":"hospitals"}
- action_map

* ask_map
- slot{"location_type":"clinics"}
- action_map

* ask_map
- slot{"location_type":"yoga trainers"}
- action_map

## sms path
* ask_sms
- action_SMS


## ip_adress
* show_ip
- action_ip

## fine path 1
* fine_normal
- utter_help

## fine path 2
* fine_ask
- utter_reply

## thanks path 1
* thanks
- utter_thank

## bot challenge
* bot_challenge
  - utter_iamabot

## bye
* goodbye
  - utter_goodbye

## handle insult
* handleinsult
  - utter_handleinsult
<!--
## reply name
* name-intent{"name":"Nikhil"}
  - slot{"name":"Nikhil"}
  - utter_greet_name
-->

* positive
    - utter_okay

* negative
    - utter_neg


## out of scope
* out_of_scope
  - utter_outofscope


## fallback
- utter_default


## New Story


* fine_ask
    - utter_reply



## reminder_story

<!--* undefined-->
<!--  - action_Get_Reminder-->



* medicine_remind
    - action_store_entity_extractor
    - action_split_date_time


## New Story

* medicine_remind{"time":"2020-01-30T15:18:00.000+00:00"}
    - action_store_entity_extractor
    - action_split_date_time
<!--* undefined-->
<!-- - action_Get_Reminder-->

## New Story
* medicine_remind{"medicine":"disprin"}
    - slot{"medicine":"disprin"}


## new story
* medicine_remind{"time":"2020-02-03T14:59:00.000+00:00"}
    - action_store_entity_extractor
    - slot{"entity_extractor":"CRFEntityExtractor"}
    - action_split_date_time
<!--* undefined-->
<!--   - action_Get_Reminder-->

* medicine_remind{"time":"2020-02-03T14:59:00.000+00:00","medicine":"disprin"}
    - slot{"medicine":"disprin"}
    - action_store_entity_extractor
    - slot{"entity_extractor":"CRFEntityExtractor"}
    - action_split_date_time
<!--* undefined-->
<!--  - action_Get_Reminder-->



## remedy story
* remedy{"ask_remedy": "cold"}
    - slot{"ask_remedy": "cold"}
    - action_remedy_csv
* remedy{"ask_remedy": "headache"}
    - slot{"ask_remedy": "headache"}
    - action_remedy_csv
* remedy{"ask_remedy": "diabetes"}
    - slot{"ask_remedy": "diabetes"}
    - action_remedy_csv
* remedy{"ask_remedy": "sore throat"}
    - slot{"ask_remedy": "Sore Throat"}
    - action_remedy_csv
* remedy{"ask_remedy": "low blood pressure"}
    - slot{"ask_remedy": "low blood pressure"}
    - action_remedy_csv
* remedy{"ask_remedy": "dark eye circles"}
    - slot{"ask_remedy": "dark eye circles"}
    - action_remedy_csv
* remedy{"ask_remedy": "constipation"}
    - slot{"ask_remedy": "constipation"}
    - action_remedy_csv
* remedy{"ask_remedy": "earache"}
    - slot{"ask_remedy": "earache"}
    - action_remedy_csv
* remedy{"ask_remedy": "stress"}
    - slot{"ask_remedy": "stress"}
    - action_remedy_csv
* remedy{"ask_remedy": "diarrhea"}
    - slot{"ask_remedy": "diarrhea"}
    - action_remedy_csv
* remedy{"ask_remedy": "backache"}
    - slot{"ask_remedy": "backache"}
    - action_remedy_csv
* remedy{"ask_remedy": "asthma"}
    - slot{"ask_remedy": "asthma"}
    - action_remedy_csv
* remedy{"ask_remedy": "acne"}
    - slot{"ask_remedy": "acne"}
    - action_remedy_csv
* remedy{"ask_remedy": "dandruff"}
    - slot{"ask_remedy": "dandruff"}
    - action_remedy_csv
* remedy{"ask_remedy": "hair loss"}
    - slot{"ask_remedy": "hair loss"}
    - action_remedy_csv
    
* remedy{"ask_remedy": "dizziness"}
    - slot{"ask_remedy": "dizziness"}
    - action_remedy_csv



