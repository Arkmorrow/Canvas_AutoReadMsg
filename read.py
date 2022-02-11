# Using Canvas v1 API to access an Announcement and 
# mark it as readimport jsonimport requestsimport osimport datetimeimport time
# Initialize some important variables:
import os
import datetime
import requests
import time


HOME_DIR = os.path.expanduser("~")
API_FILE = os.path.join(HOME_DIR,".instructure",".instructure.json")


auth = {"Authorization": "Bearer " + "replace it to your canvas api token"}
MY_DOMAIN = "https://canvas.sydney.edu.au"
start_date = datetime.datetime(2021,1,1).isoformat() 
# Necessary to list all announcements
#Get all courses
courses = requests.get(MY_DOMAIN + "/api/v1/courses", headers=auth)
    
def mark_announcement_read(course_id, disc_id):        
    conn_str = MY_DOMAIN + "/api/v1/courses/" + str(course_id) + "/discussion_topics/" + str(disc_id) + "/read.json"
    requests.put(conn_str, headers={**auth, **{"Content-Length": "0"}})
    
#for course in courses.json():    
#course_id = course["id"]
for i in range(0,100):
    course_id = 2806  
    nowtime = datetime.datetime.now() - datetime.timedelta(days=i)
    print(nowtime)
    # Retrieve all announcements that have been published in the course:    
    params = {"context_codes[]": "course_" + str(course_id), "start_date": start_date, "end_date": nowtime.isoformat()}    
    announcements = requests.get(MY_DOMAIN + "/api/v1/announcements", headers=auth, params=params)        
    for announcement in announcements.json():        
        # Delete the offending announcements        
        if announcement["read_state"] == "unread":            
            disc_id = announcement["id"]            
            # print(announcement["title"])            
            # # Mark the offending announcement as read            
            mark_announcement_read(course_id, disc_id)            
            print("Marked " + announcement["title"] + " as read.")            
            time.sleep(1)
            print("Done.")
                