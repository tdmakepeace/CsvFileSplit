# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


def SplitFile(): 
    
    print "This script will take a csvfile and split the file, maintaining the header"
    print "This is to support the bulk export of logs in CSV format, that need to be read into"
    print "another system in smaller chunks"
    print ""
    print ""
    
#    filename = "csvSample.csv"
    filename = raw_input("Name of the file you wish to split:")

#    print split
    
    with open (filename) as f:
        lineCount = sum(1 for _ in f)
        print "number of lines: " , lineCount
        split = input("Number of lines per file:")
        NuFile = ((lineCount-1)/split)+1
        print "number of files: " , NuFile
        NuFile1 = NuFile
    
    from itertools import islice

    with open (filename) as lines:
        for header in islice(lines, 1):
            Count = 0
            while (NuFile > 0):
                NuFile = NuFile -1
                Count = Count+1
                routput =  "split_%s" % (Count)
#                print routput
                output = open(routput,"w")
                output.writelines(header,)
                for line in islice(lines, 0, split):
                    output.writelines(line,)

                output.close

if __name__ == '__main__':
    SplitFile()