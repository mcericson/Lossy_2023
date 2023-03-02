
import random


student_names = ['annous', 'castro', 'elkarim', 'esmaeily', 'figueroa', 'mora',
'morales', 'ngu', 'pizano','rivera', 'sanchez', 'zaldana']

def review_sort(student_names):
    random.shuffle(student_names)

    text_file = open("review_1.txt", "w")

    for i in range(len(student_names)):
        text_file.write(str(i) + " " + student_names[i] + "\n")


    text_file.close()


    print (student_names)

review_sort(student_names)