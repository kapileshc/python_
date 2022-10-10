data = [ {'id':1,'content':'this world is full of miracles and surprises.with the advent of the spritual knowledge one can understand '},
         {'id':2,'content':'the miracles and the surprises happening around himthis world is full of miracles and surprises.with the advent of the spritual knowledge one can understand and feel the reasoning for .'},
         {'id':3,'content':'this love makes life beautiful is full of miracles and surprises.with the advent of the spritual knowledge one can understand and feel the reasoning for the miracles and the surprises happening around him.'},
         {'id':4,'content':'king and kholi are friends with all the ability to fight for what is needed with the advent of the spritual knowledge one can understand and feel the reasoning for the miracles and the surprises happening around him.'},
         {'id':5,'content':'this world is full of miracles and surprises.with the advent of the spritual knowledge one can understand and feel the reasoning for the miracles and the surprises happening around him.'},
         {'id':6,'content':'this world is full of miracles and surprises.with the advent of the spritual knowledge one can understand and feel the reasoning for the miracles and the surprises happening around him.'},
         {'id':7,'content':'this world is full of miracles and surprises.with the advent of the spritual knowledge one can understand and feel the reasoning for the miracles and the surprises happening around him.'},
         {'id':8,'content':'this world is full of miracles and surprises.with the advent of the spritual knowledge one can understand and feel the reasoning for the miracles and the surprises happening around him.'},
         {'id':9,'content':'this world is full of miracles and surprises.with the advent of the spritual knowledge one can understand and feel the reasoning for the miracles and the surprises happening around him.'}]
for content in data:
    print(len(content['content']),end='\r')
    text = content['content'].split(' ')
    print(len(text))
    count = 0
    error =0
    for word in text:
        print(word)
        letters = input('Enter the word:')
        letters=letters.strip()
        if(word == letters):
            count+=1
        else:
            error +=1
    error_percentage = error/(count+error)*100
    print(error_percentage)