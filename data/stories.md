## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## happy ticket path
* request_ticket
   - ticket_form
   - form{"name": "ticket_form"}
   - form{"name": null}
* goodbye
  - utter_goodbye

## ticket path2
* request_ticket{"date_time":"明天","end":"成都"}
   - ticket_form
   - form{"name": "ticket_form"}
   - form{"name": null}
* goodbye
  - utter_goodbye
  
## ticket unknow interrupt
* request_ticket{"date_time":"周四","end":"深圳"}
   - ticket_form
   - form{"name": "ticket_form"}
* bot_challenge
   - utter_iamabot 
   - ticket_form
* complain
   - utter_complain
   - ticket_form
   - form{"name": null}

## ticket unknow interrupt2
* request_ticket
   - ticket_form
   - form{"name": "ticket_form"}
* inform
   - ticket_form 
* complain
   - utter_complain
   - ticket_form
   - form{"name": null}
   
   
## bot challenge
* bot_challenge
  - utter_iamabot
  - ticket_form
  - form{"name": null}
* goodbye
  - utter_goodbye