import os
import time
total = os.listdir("./../Hulth-edgelists/")
path = "./../Hulth-edgelists/"
edgelist_files = [filename for filename in total if 'normal.edgelist' in filename]

for window_size in range(3,15) :
    print "Window Size = ",window_size
    for filename in edgelist_files :
        filepath =  path+filename
	outfile = filename+"_output"
	profile = filename+"_profile"
	command = "./core "+ "-i " + filepath + " -o "+ outfile + " -m e" + " -p " + profile
        print "Executing ",command
        os.system(command)
        time.sleep(2)
