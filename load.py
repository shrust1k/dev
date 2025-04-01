import pycps
import xml.etree.cElementTree as ET
import os
import time 

FILES = "../infoLoad/smallerXMLS3" #  where you take xmls 
INCLUDE_TAGS = ["title","url","host","text","ext_link_count","int_link_count", "type"]

con = pycps.Connection(
url='tcp://172.20.230.46', # !
storage='hebrew', # !
user='root',
password = 'password',
account= 'placeholder')

counter = 0

def send_doc_to_server(doc, id):
    con.insert({id: doc})

timer_start = time.time()
timer_file = time.time()
for file in os.listdir(FILES):
    with open("{}/{}".format(FILES, file), "r") as f:
        try:
            root = ET.parse(f)
        
            doc_to_load = dict()
            for elem in root.iter():
                doc_to_load[elem.tag] = elem.text


            send_doc_to_server(doc_to_load, counter)
            counter += 1

        except Exception:
            print(Exception)

    if (counter % 100 == 0):
        print("{} documents loaded in {} secs".format(counter, time.time()-timer_file, 5))
        timer_file = time.time()

print("{} doc loaded in {} secs".format(counter, time.time()-timer_start, 5))



    
    
