import os
import sys
import face_recognition_cli
import subprocess

root_input='./input'
subprocess.call(["rm","-rf","input/.keep"])
subprocess.call(["rm","-rf","unknown/.keep"])
namelist = [ item for item in os.listdir(root_input) if os.path.isdir(os.path.join(root_input, item)) ]
# print namelist 
# => ['madhu', 'amartya', 'ankit']


subprocess.call(["chmod","+x","copy_file.sh"])
subprocess.call(["chmod","+x","make_dir.sh"])
print "Making subdirectory 'known'..."
subprocess.call(["./make_dir.sh","known"])
subprocess.call(["./make_dir.sh","output"])
print "subdirectory 'known' online."

for direc in namelist:
	# print direc
	# => ankit
	# print root_input
	photolist = [ item for item in os.listdir(root_input+'/'+direc+'/') ]
	# print photolist
	# => ['20180522_154354.jpg', '20180520_155704.jpg', '20180520_155454.jpg']

	root_known = './known'
	for i,photo in enumerate(photolist):
		tmp = photo.split('.')
		photo_name = tmp[0]
		photo_ext = tmp[1]
		subprocess.call(["./copy_file.sh","input/"+direc+"/"+photo,"known/"+str(i)+"_"+direc+"."+photo_ext])
		# print ""

print "Sample photos obtained from the input directory."
print "Starting the processing of the obtained photos..."


# oup_from_face_recog = (subprocess.check_output([sys.executable, "face_recognition_cli.py","./known/","./unknown/"])).split('\n')
oup_from_face_recog = face_recognition_cli.main("./known","./unknown",1,0.55,False)

print "Processing of the obtained photos completed."
print "Starting the grouping of the obtained photos in the respective folders..."
# print "0001"
# print oup_from_face_recog
for i,data in enumerate(oup_from_face_recog):
	# print "fgfg"
	# print data
	if (data[0]).startswith("WARNING") or len(data)<2 or len(data)>2:
		continue
	else:
		# tmp = data.split(',')
		# unknown_file_name_path = tmp[0]
		# unknown_file_name = unknown_file_name_path.split('/')[2]
		# known_folder = (tmp[1].split('_'))[1]
		# subprocess.call(["./make_dir.sh","output/"+known_folder])
		# subprocess.call(["./copy_file.sh",unknown_file_name_path,"output/"+known_folder+"/"+unknown_file_name])
		unknown_file_name_path = data[0]
		unknown_file_name = unknown_file_name_path.split('/')[2]
		known_folder = (data[1].split('_'))[1]
		subprocess.call(["./make_dir.sh","output/"+known_folder])
		subprocess.call(["./copy_file.sh",unknown_file_name_path,"output/"+known_folder+"/"+unknown_file_name])
subprocess.call(["rm","-rf","output/person/"])
subprocess.call(["rm","-rf","output/persons/"])
subprocess.call(["rm","-rf","known/"])
subprocess.call(["touch","input/.keep"])
subprocess.call(["touch","unknown/.keep"])
print "Grouping of the obtained photos in the respective folders completed."
print "Find the folders in the 'output' folder."

