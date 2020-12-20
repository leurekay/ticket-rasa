

## happy ticket path
* request_ticket
   - ticket_form
   - form{"name": "ticket_form"}
   - form{"name": null}
* faq
  - respond_faq

## ticket path2
* request_ticket{"date_time":"明天","end":"成都"}
   - ticket_form
   - form{"name": "ticket_form"}
   - form{"name": null}
* faq
  - respond_faq
  
## ticket unknow interrupt
* request_ticket{"date_time":"周四","end":"深圳"}
   - ticket_form
   - form{"name": "ticket_form"}
* faq
   - respond_faq 
   - ticket_form
* faq
   - respond_faq
   - ticket_form
   - form{"name": null}

## ticket unknow interrupt2
* request_ticket
   - ticket_form
   - form{"name": "ticket_form"}
* inform
   - ticket_form 
* faq
   - respond_faq
   - ticket_form
   - form{"name": null}
   
   
## bot challenge
* faq
  - respond_faq
* faq
  - respond_faq
* request_ticket
   - ticket_form
   - form{"name": "ticket_form"}
* inform
   - ticket_form 
* faq
   - respond_faq
   - ticket_form
   - form{"name": null}

## bot challenge2
* faq
  - respond_faq
* request_ticket
   - ticket_form
   - form{"name": "ticket_form"}
* inform
   - ticket_form 
* faq
   - respond_faq
   - ticket_form
   - form{"name": null}