#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
names=[]
with open("Day_24/Mail Merge Project/input/Letters/starting_letter.txt")  as file_letter:
    letter=file_letter.read()
    with open("Day_24/Mail Merge Project/input/Names/invited_names.txt") as file:
        lines=file.readlines()
        for i in lines:
            names.append(i)
            with open(f"Day_24/Mail Merge Project/output/letter_for_{i.strip()}",mode="w") as file_name:
                new_letter=str(letter).replace("[name]",i)
                file_name.write(new_letter)

                

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp