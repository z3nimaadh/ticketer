import requests
import json
import random
from random import randint
import sqlite3

#payload = {'ticket': {'subject': 'Configuration Help', 'comment': {'body': 'I have a problem'}, 'ticket_form_id':745328,'priority': 'normal', 'requester_id':23050130487, "tags":["bug_report"]}}

#payload_1 = {'ticket': {'subject': 'Dispute', 'comment': {'body': 'I have a problem'}, 'ticket_form_id':745328,'priority': 'normal', 'requester_id':20566203908}}
#payload_2 = {'ticket': {'subject': 'Services Question', 'comment': {'body': 'I have a problem'}, 'ticket_form_id':745328,'priority': 'normal', 'requester_id':20566203908, "tags":["services"]}}
#payload_3 = {'ticket': {'subject': 'Installation problem', 'comment': {'body': 'I need help with an installation'}, 'ticket_form_id':745328,'priority': 'urgent', 'requester_id':20566203908, "tags":["installation"]}}
#payload_4 = {'ticket': {'subject': 'HELP ME PLEASE', 'comment': {'body': 'I need help doing the thing'}, 'ticket_form_id':745328,'priority': 'normal', 'requester_id':20566203908, "tags":["help"]}}
#payload_5 = {'ticket': {'subject': 'HELP ME PLEASE', 'comment': {'body': 'I need help doing the thing'}, 'ticket_form_id':745328,'priority': 'normal', 'requester_id':20566203908, "tags":["help"]}}

#ticket_types = [payload_1,payload_2,payload_3,payload_4,payload_5]

#payload_1 = {'ticket': {'subject': 'Configuration Help', 'comment': {'body': 'I have a problem'}, 'priority': 'normal', 'requester_id':116021645572}}
#payload_2 = {'ticket': {'subject': 'Services Question', 'comment': {'body': 'I have a problem'}, 'priority': 'normal', 'requester_id':116021645572, "tags":["services"]}}
#payload_3 = {'ticket': {'subject': 'Installation problem', 'comment': {'body': 'I need help with an installation'}, 'priority': 'urgent', 'requester_id':116021645572, "tags":["installation"]}}
#payload_4 = {'ticket': {'subject': 'HELP ME PLEASE', 'comment': {'body': 'I need help doing the thing'}, 'priority': 'normal', 'requester_id':116021645572, "tags":["help"]}}

#ticket_types = [payload_1,payload_2,payload_3,payload_4]




#r = requests.post('https://z3nimaadh.zendesk.com/api/v2/tickets.json', json=payload, auth=('isiddiqui@zendesk.com/token','Ip6fldKPtz7DuZhCKtl3yuu2ttRZwJ7ynaL0L9tw'))

#print(r.status_code)
#print(r.text)

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

def gen_json(query):
    cur.execute('SELECT * from userdata_subdomain WHERE userdata_subdomain.subdomain = '+query+'')
    userdata = cur.fetchone()
    
    subdomain = str(userdata[1])
    username = str(userdata[2])
    token = str(userdata[3])
    r_id = str(userdata[6])
    reqs = r_id.split(",")
    re_l = len(reqs)
    descriptions = userdata[4]
    subject = userdata[5]
    descriptions_parsed = descriptions.split(",")
    dp_l = len(descriptions_parsed)
    subjects_parsed = subject.split(",")
    sp_l = len(subjects_parsed)

    rand_pll = []
    r_count = 0
    while r_count < 10:
        rand_desc = descriptions_parsed[randint(0,dp_l-1)]
        rand_subj = subjects_parsed[randint(0,sp_l-1)]
        rand_req = reqs[randint(0,re_l-1)]
        rand_pll.append({'ticket': {'subject':rand_subj, 'comment': {'body':rand_desc}, 'requester_id':int(rand_req),'priority': 'normal' }})
        r_count = r_count + 1
    
    return [subdomain,username,token,rand_pll]



def create_tickets():
    count = 0
    while count < 5:
        r = requests.post('https://'+g_j[0]+'.zendesk.com/api/v2/tickets.json', json=g_j[3][randint(0,(len(g_j[3])-1))], auth=(g_j[1]+'/token',g_j[2]))
        count = count + 1
        print(r.status_code)
        print(r.text)
        print ("TICKET CREATED\n...")


cur.execute('SELECT * from userdata_subdomain')
all_rows = cur.fetchall()
for row in all_rows:
    print(row[1])
    sd = row[1]
    g_j = gen_json("'"+sd+"'")
    create_tickets()




#sub_inp = input("Enter subdomain: ")
#g_j = gen_json("'"+sub_inp+"'")
#print(g_j[0])
#print(g_j[3])


'''count = 0
while count < 10:
    r = requests.post('https://'+g_j[0]+'.zendesk.com/api/v2/tickets.json', json=g_j[3][randint(0,(len(g_j[3])-1))], auth=(g_j[1]+'/token',g_j[2]))
    count = count + 1
    print(r.status_code)
    print(r.text)
    print ("TICKET CREATED\n...")

#'requester_id':20566203908,

#brandon
#r = requests.post('https://z3nbrandonbest.zendesk.com/api/v2/tickets.json', json=payload, auth=('bbest@zendesk.com/token','ZJ89rx4nnD238TNbj7YJP6Qj2IR6DziTeNJGLiU9'))

#mark
#r = requests.post('https://z3nmarkmcdonnell.zendesk.com/api/v2/tickets.json', json=payload, auth=('mmcdonnell@zendesk.com/token','PHWIEZtlELnajGGsuhTk0IiUTVi3XbsZuC7knmWF'))
#r = requests.post('https://z3nimaadh.zendesk.com/api/v2/tickets.json', json=payload, auth=('isiddiqui@zendesk.com/token','Ip6fldKPtz7DuZhCKtl3yuu2ttRZwJ7ynaL0L9tw'))

#alice
#r = requests.post('https://z3nalicehr.zendesk.com/api/v2/tickets.json', json=a2_ticket_types[randint(0,8)], auth=('alegan+3@zendesk.com/token','dn7jEFG0igSWmjstPpolaIx7qdsTXikqK53XeEfE'))

'''