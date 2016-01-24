import os
import datetime
def dash_print(file  , length): # this function is for printing dash in the txt file 
    for i in range(length):
        file.write("-")
    file.write("\n")
def show(code_list): # this function print output
    for i in code_list:
        print(i)
def find_directory(folder_list,direct='.\\'): # a function for finding hierarchical folders
    folder=os.listdir(direct) # get list directory of folders
    sub_folder_list=[] # empty folder
    for i in range(len(folder)): # this for find sub folder
        if folder[i].find(".")==-1:
            sub_folder_list.append(direct+".\\"+folder[i]+"\\")
    folder_list.extend(sub_folder_list) # update master folder list
    for item in range(len(sub_folder_list)): # run again find_directory for sub folders
        find_directory(folder_list,sub_folder_list[item])
#---------------------------------------------------------------------------------------
def main():
    folder_list=['.\\'] # create master folder_list
    find_directory(folder_list) # run find_drectory
    file=open("line_log.txt","a") # open a txt file for log as appending
    line_length=0
    print_list=[]
    total=0
    counter=0
    for j in range(len(folder_list)): # find each python files in each direction and count lines
        folder=os.listdir(folder_list[j])
        for i in range(len(folder)):
            if folder[i].find(".py")!=-1 and folder[i]!="line_counter.py" and folder[i].find(".pyd")==-1:
                c_file=open(folder_list[j]+folder[i],"r")
                counter=counter+1
                for line in c_file:
                    if len(line)>1 :
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

    main()
    

            
        
