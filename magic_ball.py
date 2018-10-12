# "Magic 8 Ball with a List" game 

from random import shuffle # this part we will learn letter

messages = ['It is certain', 'It is decidedly so',  'Yes definitely',  
            'Reply hazy try again', 'Ask again later', 'Concentrate and ask again', 
            'My reply is no', 'Outlook not so good', 'Very doubtful']

shuffle(messages) # this function will mix the elements of the list

input("Ask a question to a ball and press any key to get your prediction")

print(messages[0])
