import numpy as np 
import pandas as pd
import csv
import os
import sys

df = pd.read_csv('Test/list.csv')
df = df.astype(int)
port_nos = np.asarray(df)
File_path = 'Test/dict.csv'
rand_range = np.arange(10000,65535)

while True:
    try:
        with open(File_path) as csv_file:
            reader = csv.reader(csv_file)
            student_dict = dict(reader)
            print(student_dict)
            break
    except FileNotFoundError:
        total_student = input("Enter the number of students: ")
        while True:
            try:
                total_student = int(total_student)
                break
            except ValueError:
                print("Number of students must be an integer")
                total_student = input("Enter the number of students: ")

        for i in range(len(df)):
            if port_nos[i] in rand_range:
                rand_range = np.delete(rand_range, np.where(rand_range == port_nos[i]))

        student_dict = {}

        for i in range(total_student):
            student_id = np.random.choice(rand_range)
            student_dict[i] = student_id
            container_name = 'student'+str(i)
            port_num = str(student_id)
            container_RAM_size = '512m'
            os.system('./test2.sh '+container_name+' '+port_num+' '+container_RAM_size+'')
      
        with open(File_path, 'w') as csv_file:  
            writer = csv.writer(csv_file)
            for key, value in student_dict.items():
                writer.writerow([key, value])



