import cv2
import os
import glob

originalfolder = "/home/rk/Amy/data/stanford_campus_dataset/annotations/"
destinationfolder = "/home/rk/Amy/data/stanford_campus_dataset_kitti/"

# convert txt file from stanford drone dataset to kitti format
def ssd2kitti(ori,des):
	with open(ori) as f:
	    lines = f.readlines()

	for i in range(len(lines)):
		items = lines[i].split()
		outputfile = open(des+items[5]+".txt","a+") 
		wline = ""
		wline += items[9].strip('"')
		wline += " "
		wline += "0"
		wline += " "
		truncated = 0
		if items[6]=='1':
			truncated = 3
		if items[7]=='1':
			truncated = 1
		wline += str(truncated)
		wline += " "
		wline += "0"
		wline += " "
		wline += items[1]
		wline += " "
		wline += items[2]
		wline += " "
		wline += items[3]
		wline += " "
		wline += items[4]
		wline += " "
		wline += "0 "
		wline += "0 "
		wline += "0 "
		wline += "0 "
		wline += "0 "
		wline += "0 "
		wline += "0 "
		wline += "\n"
		#print wline
		outputfile.write(wline)
		outputfile.close()

# create the destination folder if not exist
if not os.path.exists(destinationfolder):
    os.makedirs(destinationfolder)

subfolder=[]
for i in range(len(glob.glob(originalfolder+"*"))):
    subfolder.append(os.path.basename(sorted(glob.glob(originalfolder+"*"))[i]))
    subsubfolder=[]
    for j in range(len(glob.glob(originalfolder+subfolder[-1]+"/"+"*"))):
        subsubfolder.append(os.path.basename(sorted(glob.glob(originalfolder+subfolder[-1]+"/"+"*"))[j]))       
    print "Now proceeding " + subfolder[i] + "..."
    # create the subfolder and the subsubfoleder of the destinationfolder if not exist
    if not os.path.exists(destinationfolder+subfolder[i]+"/"):
        os.makedirs(destinationfolder+subfolder[i]+"/")
        for j in range(len(subsubfolder)):
            if not os.path.exists(destinationfolder+subfolder[i]+"/"+subsubfolder[j]+"/"):
                os.makedirs(destinationfolder+subfolder[i]+"/"+subsubfolder[j]+"/")
    for j in range(len(subsubfolder)):
        print "Now proceeding " + subsubfolder[j]
        ssd2kitti(originalfolder+subfolder[i]+"/"+subsubfolder[j]+"/"+"annotations.txt", 
            destinationfolder+subfolder[i]+"/"+subsubfolder[j]+"/")


