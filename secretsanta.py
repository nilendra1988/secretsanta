import csv

import random

import datetime

import json

 

 

#this function is to write previous year santas data to a file

#in future we can use any db here in place of file

def write_to_cache_file(write_to_file_dict):

    try:

        file_path = 'D:\\SecretSanta\\yeardata.txt'

        with open(file_path, 'w') as cachefile:

            cachefile.write(write_to_file_dict)

    except Exception as e:

        print(e)

 

#this function is to write final output data to a file

#in future we can use any db here in place of file

def write_final_output(write_to_file_dict):

    try:

        file_path = 'D:\\SecretSanta\\finaloutput.txt'

        with open(file_path, 'w') as cachefile:

            cachefile.write(write_to_file_dict)

    except Exception as e:

        print(e)

#this function is to read previous year santas data

#in future we can use any db here in place of file

def read_frm_cache_file():

    try:

        file_path = 'D:\\SecretSanta\\yeardata.txt'

        with open(file_path, 'r') as cachefile:

            data=cachefile.readline()

            data = json.loads(data)

        return data

    except Exception as e:

        print(e)

       

        

#this function is to read family members name froma txt file

#in future we can use any db here in place of file

def read_family_members():

    

    with open('D:\\SecretSanta\\FamilyMembers.txt',"r") as f:

        reader = csv.reader(f,delimiter="\n")

       

        rownum=0

        family_members = []

        for row in reader:

            family_members.append(row[0])

            rownum+=1

           

        return family_members   

            

      

        

        

def main():

    family_members=read_family_members()

    #family_members = ["a","b","c","d"]

    year_period = 3

    current_year = datetime.datetime.now().year

    #current_year = 2021

    received = family_members

    remaining_santas = family_members

    ## if data exists in file read otherwise initialize the dictionary

    yearwise_data = read_frm_cache_file()

    if yearwise_data is None:

        yearwise_data = {}

    final_output="Secret Santa Result \n========================== \n"

    for r in received:

        prev_yr_santas=[]

        for i in range(year_period-1):

            try:

                prev_yr_santas.append(yearwise_data[str(r) + '_' + str(int(current_year-i))])

            except Exception:

                pass

        eligible_santas = list(set(remaining_santas) - set([r]) - set(prev_yr_santas))

        if (len(eligible_santas) == 0):

            eligible_santas = list(set(family_members) - set([r]) - set(prev_yr_santas))

        choosen_santa = random.choice(eligible_santas)

        final_output=final_output + choosen_santa + " has given gift to " + r +"\n"

        remaining_santas = list(set(remaining_santas) - set([choosen_santa]))

        yearwise_data[str(r) + '_' + str(current_year)] = str(choosen_santa)

 

    write_final_output(final_output)

    write_to_cache_file(json.dumps(yearwise_data))

 

if __name__ == '__main__':

    main()
