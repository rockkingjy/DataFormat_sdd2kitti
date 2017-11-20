import cv2
import os
import glob

originalfolder = "/home/rk/Amy/data/stanford_campus_dataset/videos/"
destinationfolder = "/home/rk/Amy/data/stanford_campus_dataset_kitti/"

# convert video to image
def video2image(ori,des):
    vidcap = cv2.VideoCapture(ori)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
        success,image = vidcap.read()
        print 'Read a new frame: ', success, 'count:', count
        cv2.imwrite(des + "%d.png" % count, image)     # save frame as PNG file
        count += 1

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
        video2image(originalfolder+subfolder[i]+"/"+subsubfolder[j]+"/"+"video.mov", 
            destinationfolder+subfolder[i]+"/"+subsubfolder[j]+"/")

