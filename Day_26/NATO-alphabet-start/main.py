student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}



import pandas
student_data_frame = pandas.DataFrame(student_dict)
def Gen():
    try:
        dic_2=[{row.letter:row.code for index,row in pandas.read_csv("Day_26\\NATO-alphabet-start\\nato_phonetic_alphabet.csv").iterrows()}[i] for i in input("Give me the words:-").upper()]
    except:
        print("Sorry Letters only")
        Gen()
    else:
        print(dic_2)
Gen()