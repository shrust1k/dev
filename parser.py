FILE = "/home/shrust1k/infoLoad/iswiki-20250120-pages-articles.xml" #xml to parse
FOLDER = "../infoLoad/smallerXMLS3" # folder for output, where smaller xmlxs will appear


with open(FILE, "r") as f:
    counter = 0
    
    write = False
    create_new_file = False
    fw = open(f"{FOLDER}/smaller_xml_{counter}.xml", "w")
    line = f.readline()
    while line:
        if create_new_file:
            fw = open(f"{FOLDER}/smaller_xml_{counter}.xml", "w")
            create_new_file = False

        if (line.strip() == "<page>"):
            fw.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            write = True

        if (write == True):
            fw.write(line)

        if (line.strip() == "</page>"):
            write = False
            create_new_file = True
            counter += 1
        line = f.readline()
  
