# Posts a list of folders to a Microsoft Teams webhook that are more than X days old. 
import os, time, sys, pwd, requests

webhook_url = "webhook url here"
path = "/volume1/share/" #start scanning in this directory
keepDays=30 #age in days

file_list = ""

payload_title = "The following folders are more than %i days old:" %keepDays

# get top level directories more than keepDays old, add the filenames to a list.
for f in os.listdir(path):
        if not (f.startswith(".") or f.startswith("#") or f.startswith("@eaDir")):
                fp = os.path.join(path,f)
                if os.stat(fp).st_mtime <= time.time() - (keepDays * 86400):
                        file_list = file_list+f+"; "

json_payload = {}
json_payload['title'] = payload_title
json_payload['text'] = file_list

#print(json_payload)

requests.post(url=webhook_url, json=json_payload)
