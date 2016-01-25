import os
import datetime
import platform
import string
def dash_print(file  , length): # this function is for printing dash in the txt file 
    for i in range(length):
        file.write("-")
    file.write("\n")
def show(code_list): # this function print output
    for i in code_list:
        print(i)
def find_directory(folder_list,direct='./'): # a function for finding hierarchical folders
    folder=os.listdir(direct) # get list directory of folders
    sub_folder_list=[] # empty folder
    for i in range(len(folder)): # this for find sub folder
        if folder[i].find(".")==-1:
            sub_folder_list.append(direct+"./"+folder[i]+"/")
    folder_list.extend(sub_folder_list) # update master folder list
    for item in range(len(sub_folder_list)): # run again find_directory for sub folders
        find_directory(folder_list,sub_folder_list[item])
def start_up(version):
    print("Pycounter By Sepand Haghighi , Version : "+version)
    print("Operating System :"+platform.system())
#---------------------------------------------------------------------------------------
def comment(line): # this function extract comment
    index=line.find("#") # search for # as comment sign
    if index!=-1: # if it's in the line 
        sub_line=line[:index] # create sub_line as prev chars
        for i in sub_line: # if there is any chars before this sign it's not comment
            if i in string.ascii_letters or i in string.punctuation:
                return False
                break
        return True
    else: # if there is no sign of # in the line , it's not a comment
        return False
def get_input(): # this function get a string from user for ignoring comment lines in count or not
    input_string=input(" Ignore Comment[1] Or Not[2]")
    if int(input_string)==1: 
        return True
    else:
        return False
def main():
    folder_list=['./'] # create master folder_list
    find_directory(folder_list) # run find_drectory
    file=open("line_log.txt","a") # open a txt file for log as appending
    line_length=0
    print_list=[]
    total=0
    counter=0
    ignore=get_input()
    for j in range(len(folder_list)): # find each python files in each direction and count lines
        folder=os.listdir(folder_list[j])
        for i in range(len(folder)):
            if folder[i].find(".py")!=-1 and folder[i]!="line_counter.py" and folder[i].find(".pyd")==-1:
                c_file=open(folder_list[j]+folder[i],"r")
                counter=counter+1
                for line in c_file:
                    if ignore==True:
                        if len(line)>1 and comment(line)==False :
                            line_length=line_length+1
                    else:
                        if len(line)>1:
                            line_length=line_length+1
                if counter>0:
                    file.write(str(counter)+"-"+folder[i]+" : "+str(line_length)+"\t"+str(folder_list[j])+"\n") # update txt log
                    print_list.append(str(counter)+"-"+folder[i]+" : "+str(line_length)+"\t"+str(folder_list[j])) # update output list
                    c_file.close()
                    total=total+line_length
                    line_length=0
    file.write("Total Lines : "+str(total)+"\n")
    dash_print(file,40)
    file.close()
    show(print_list)
    print("Total Lines : " +str(total))
if (__name__=="__main__"):
    version="1.0.0"
    start_up(version)
    main()
    #print("Something Wrong")
    

            
        
