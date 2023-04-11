import time # Allows for short delays between outputs to allow for a smoother CLI experience

class Class:
    '''
    Represents a class in school for a specific person
    '''

    
    def __init__(self, name: str):
        '''
        Initializes the class

        :param str name: The name of the class
        '''
        self.name = name
        self.scores = []
        self.average = 0
        self.highest = 0
        self.lowest = 0
    

    def add_score(self, score: int):
        '''
        Adds a score to the class.

        :param int score: The score that is to be added
        '''
        self.scores.append(score)

        # Updates the current average by taking the sum of all the scores in self.scores
        # and dividing that by the number of elements in self.scores
        self.average = sum(self.scores)/len(self.scores)

        self.average = round(self.average) # The average is then rounded
        
        self.highest = max(self.scores)
        self.lowest = min(self.scores)


def display(classes):
    '''
    Displays all of the relevant information for each of the classes

    More specifically, displays the total average score across all the classes
    then for each class displays the class name, scores, average, highest score, 
    and lowest score.

    :param list classes: A list of all of the Class objects
    '''
    total = 0
    for i in classes:
        total += i.average
    
    total_average = round(total/len(classes))
    print(f"\nTotal Average: {total_average}")
    time.sleep(1)
    print("\nClasses:")
    time.sleep(1)

    # Prints all of the relevant information in each class
    for i in classes:
        print() # Blank space
        print(f"Name: {i.name}")    
        print(f"Scores: {i.scores}")
        print(f"Current Average: {i.average}")
        print(f"Highest Score {i.highest}")
        print(f"Lowest Score {i.lowest}")
        print() # Blank space
        time.sleep(.6)


classes = []
print("Before you start entering scores, you must name your classes\n")
for i in range(1, 6):
    print(f"Enter the name for class #{i}")
    class_name = input('')
    classes.append(Class(class_name))

# The program loop uses uses infinite loops to allow for the user to retry data entry in the case of invalid data
# Otherwise the loops are broken out of using break statements
while True:
    # Displays all the class information
    display(classes)
    time.sleep(1)
    while True:
        print("\nWhich class would you like to add a score to?\n")
        
        class_index = 1
        for i in classes:
            print(f"{class_index}. {i.name}")
            class_index += 1
        menu_choice = input("").replace(' ', '')

        if menu_choice in ['1', '2', '3', '4', '5']:
            break
        else:
            print("\nSorry! That wasn't an option.")
    
    while True:
        print("\nInput Score Below:")
        score = input("")
        
        # If the entered score is numeric, adds the score to the class selected in the
        # menu beforhand (it has to be classes[int(menu_choice)-1] because indecies start
        # at 0)
        if score.isnumeric():
            classes[int(menu_choice)-1].add_score(int(score))
            break
        else:
            print("\nScore must be a number")
