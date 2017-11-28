import os
import time
total = os.listdir("./../Hulth-edgelists/")
path = "./../Hulth-edgelists/"
edgelist_files = [filename for filename in total if 'normal.edgelist' in filename]

for window_size in range(3,15) :
    print "Window Size = ",window_size
    for filename in edgelist_files :
        filepath =  path+filename
        rates_file = filename+"rates.txt"
        pava_file = filename+"pavafit.txt"
        cuts_file = filename+"cuts.txt"
        exact_file = filename+"exact.txt"
        command = "./exactDF 8 500 "+ filepath + " " +rates_file + " " + pava_file + " " + cuts_file + " " + exact_file
        print "Executing ",command
        os.system(command)
        time.sleep(5)
