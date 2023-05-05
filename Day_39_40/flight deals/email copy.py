from data_manager import DataManager

data=DataManager()

print(
  "Welcome to the kashif's Flight \n we found the best flight deals and email u"
)
while True:
  first_name = input('What is ur first name? :-')
  last_name = input('What is ur last name? :-')
  email_input = input('What is ur email? :-')
  if email_input == input('Type ur email again? :-'):
    email = email_input
  else:
    print("Oops Type Again")
    continue
  data.add_email(first_name,last_name,email)
  if input('Do u want to add more emails ! type (Yes/No)').lower() == 'yes':
    break
  else:
    continue