# characters
define a = Character("Mr Algorithm")
define yn = Character("[Name]")
define g = Character("System")

# variables
init python:
    lore_route = True
    friendship = 0
    section1 = 0
    section2 = 0
    section3 = 0
    section4 = 0
    Answer_1_2 = ""
    Answer_1_3 = ""
    Answer_1_4 = ""
    Answer_1_5 = ""
    Answer_2_2 = ""
    Answer_2_3 = ""
    Answer_2_5 = ""
    Answer_3_1 = ""
    Answer_3_3 = ""
    Answer_4_5 = ""
# game starts here


transform custom_pos:
    zoom 1.0
    pos (0, 110)
transform small:
    zoom 0.5
    pos(0, 1070)
label start:
    scene background # set the background image
    init python:
        renpy.show_screen("game")

    g "What is your name?"
    $ Name = renpy.input("Input a name here", length=32)
    g "Welcome [Name]."

    show mr_al_talk at custom_pos # mr algorithm appears
    a "Good day to you [Name]."
    a "Today we are going to learn all about Data Structures and Algorithms."
    a "Are you ready to learn?!"
    menu:
        "Yes":
            a "Then let us begin."
            jump section1
        "No!":
            pass

label section1:
    show mr_al_neutral at custom_pos
    scene background # background may or may not differ depending on the current section
    # here something should indicate we moved to section 1 (image, not text)
    if section1 == 0:
        jump section1question1
    elif section1 == 1:
        jump section1question2
    elif section1 == 2:
        jump section1question3
    elif section1 == 3:
        jump section1question4
    elif section1 == 4:
        jump section1question5
    else:
        jump intermission1

label section1question1:
    show mr_al_talk at custom_pos
    a "Question 1: which code correctly inserts element “score” into position “index”?"
    hide mr_al_neutral
    show mr_al_neutral at small

    menu:
        "Answer 1":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's right! Nice attention to detail."
            $ section1 += 1
            jump section1
        "Answer 2":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Not quite; remember that “sizeof” returns the number of bytes the object takes up."
            jump section1question1
        "Answer 3":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "...hmm. Looks like you've got a malformed array there in the first line!"
            jump section1question1
        "Answer 4":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Alan Please add details."
            jump section1question1

label section1question2:
    hide mr_al_neutral
    show mr_al_neutral at custom_pos
    a "Question 2: Here is a Linked List implementation. What is the output of the following code?"
    $ Answer_1_2 = renpy.input("Input your answer here", length = 64)
    if Answer_1_2 == ("28.0" or "28"):
        a "Good Job"
        $ section1 += 1
        jump section1
    else:
        a "That's not quite right!"
        jump section1question2

label section1question3:
    hide mr_al_neutral
    show mr_al_neutral at custom_pos
    a "Question 3: Type the name of the variable that causes a leak in this code:"
    $ Answer_1_3 = renpy.input("Input your answer here", length = 64)
    if Answer_1_3 == "ptr2":
        a "You’ve done it!"
        $ section1 += 1
        jump section1
    else:
        a "That's not quite right!"
        jump section1question3

label section1question4:
    hide mr_al_neutral
    show mr_al_neutral at custom_pos
    a "Question 4: Fill in the blank to pass this test:"
    $ Answer_1_4 = renpy.input("Input your answer here", length = 64)
    python:
        input_list = list(Answer_1_4)
        if (input_list[0] % 2 == 1) and (my_list[1]) and (my_list[-1] % 5 == 4) and len(my_list > 4):
            correct = True
    if correct:
        a "Impressive work!"
        $ section1 += 1
        $ correct = False
        jump section1
    else:
        a "That's not quite right!"
        jump section1question4

label section1question5:
    hide mr_al_neutral
    show mr_al_neutral at custom_pos
    a "Question 5: Enter the line number where this linked list implementation fails:"
    $ Answer_1_5 = renpy.input("Input your answer here", length = 64)
    if Answer_1_5 == "11":
        a "Well Done"
        $ section1 += 1
        jump section1
    else:
        a "That's not quite right!"
        jump section1question5

label intermission1:
    a "How did you find the first topic?"
    menu:
        "It was really easy":
            a "Well, they'll only get harder from here on out, so make sure you're prepared!"

        "It was super challenging":
            a "Hopefully you were able to learn from your mistakes" # something along these lines

    a "Are you ready to move on?"
    menu:
        "I'm ready": # indicate that this choice locks the player out of the 'lore' route
            $ lore_route = False
            a "Let us begin!"
            jump section2
        "Who are you?":
            a ""
            # mr algorithm facial expression changes
            a "Lets move on."
            jump section2


label section2:
    #scene background # background may or may not differ depending on the current section
    # here something should indicate we moved to section 1 (image, not text)
    if section2 == 0:
        jump section2question1
    elif section2 == 1:
        jump section2question2
    elif section2 == 2:
        jump section2question3
    elif section2 == 3:
        jump section2question4
    elif section2 == 4:
        jump section2question5
    else:
        jump intermission2

label section2question1:
    a "Question 1"
    menu:
        "Answer 1":
            a "Good Job"
            $ section2 += 1
            jump section2
        "Answer 2":
            a "That's not quite right!"
            jump section2question1
        "Answer 3":
            a "That's not quite right!"
            jump section2question1
        "Answer 4":
            a "That's not quite right!"
            jump section2question1

label section2question2:
    a "Question 2"
    $ Answer_2_2 = renpy.input("Input your answer here", length = 64)
    if Answer_2_2 == "Skibidi":
        a "You’ve done it"
        $ section2 += 1
        jump section2
    else:
        a "That's not quite right!"
        jump section2question2

label section2question3:
    a "Question 3"
    $ Answer_2_3 = renpy.input("Input your answer here", length = 64)
    if Answer_2_3 == "Skibidi":
        a "Impressive"
        $ section2 += 1
        jump section2
    else:
        a "That's not quite right!"
        jump section2question3

label section2question4:
    a "Question 4"
    menu:
        "Answer 1":
            a "That's not quite right!"
            jump section2question4
        "Answer 2":
            a "That's not quite right!"
            jump section2question4
        "Answer 3":
            a "Well Done"
            $ section2 += 1
            jump section2
        "Answer 4":
            a "That's not quite right!"
            jump section2question4

label section2question5:
    a "Question 5"
    $ Answer_2_5 = renpy.input("Input your answer here", length = 64)
    if Answer_2_5 == "Skibidi":
        a "Good Job"
        $ section2 += 1
        jump section2
    else:
        a "That's not quite right!"
        jump section2question5

label intermission2:
    a "How did you find the second topic?"
    menu:
        "It was really easy":
            a "Well they'll only get harder from here on out, so make sure you're prepared!"

        "It was super challenging":
            a "Hopefully you were able to learn from your mistakes"

    a "Are you ready to move on?"
    if lore_route:
        menu:
            "I'm ready":
                a "Let us begin!"
                jump section3
            "You didn't answer my question":
                a ""
                a "You caught me off guard."
                yn "Can I ask you another question?"
                a "Maybe later."
                jump section3
    else:
        menu:
            "I'm ready":
                a "Let us begin!"
                jump section3

label section3:
    if section3 == 0:
        jump section3question1
    elif section3 == 1:
        jump section3question2
    elif section3 == 2:
        jump section3question3
    elif section3 == 3:
        jump section3question4
    elif section3 == 4:
        jump section3question5
    else:
        jump intermission3

label section3question1:
    a "Question 1"
    $ Answer_3_1 = renpy.input("Input your answer here", length = 64)
    if Answer_3_1 == "Skibidi":
        a "You've done it"
        $ section3 += 1
        jump section3
    else:
        a "That's not quite right!"
        jump section3question1

label section3question2:
    a "Question 2"
    menu:
        "Answer 1":
            a "That's not quite right!"
            jump section3question2
        "Answer 2":
            a "Impressive"
            $ section3 += 1
            jump section3
        "Answer 3":
            a "That's not quite right"
            jump section3question2
        "Answer 4":
            a "That's not quite right"
            jump section3question2

label section3question3:
    a "Question 3"
    $ Answer_3_3 = renpy.input("Input your answer here", length = 64)
    if Answer_3_3 == "Skibidi":
        a "Well done"
        $ section3 += 1
        jump section3
    else:
        a "That's not quite right!"
        jump section3question3

label section3question4:
    a "Question 4"
    menu:
        "Answer 1":
            a "That's not quite right!"
            jump section3question4
        "Answer 2":
            a "Good job"
            $ section3 += 1
        "Answer 3":
            a "That's not quite right!"
            jump section3question4
        "Answer 4":
            a "That's not quite right!"
            jump section3question4

label section3question5:
    a "Question 5"
    menu:
        "Answer 1":
            a "You've done it"
            $ section3 += 1
            jump section3
        "Answer 2":
            a "That's not quite right!"
            jump section3question5
        "Answer 3":
            a "That's not quite right!"
            jump section3question5
        "Answer 4":
            a "That's not quite right!"
            jump section3question5

label intermission3:
    a "How did you find the third topic?"
    menu:
        "It was really easy":
            "Well they'll only get harder from here on out, so make sure you're prepared"
        "It was super challenging":
            "Hopefully you were able to learn from your mistakes"
    a "Are you ready to move on?"

    if lore_route:
        menu:
            "I'm ready":
                "Let us begin!"
                jump section4
            "Do you make the questions in this game?":
                jump intermission3lore
    else:
        menu:
            "I'm ready":
                "Let us begin!"
                jump section4

label intermission3lore:
    a "Yes, I enjoy designing puzzles for people to solve."
    menu:
        "Well thank you, I'm really enjoying them!":
            a "Thank you!"
            $ friendship += 1

        "Oh, they're kind of bad honestly":
            a "Oh... thanks for the feedback"
            $ friendship -= 1
    jump section4

label section4:
    if section4 == 0:
        jump section4question1
    elif section4 == 1:
        jump section4question2
    elif section4 == 2:
        jump section4question3
    elif section4 == 3:
        jump section4question4
    elif section4 == 4:
        jump section4question5
    else:
        jump intermission4

label section4question1:
    a "Question 1"
    menu:
        "Answer 1":
            "That's not quite right!"
            jump section4question1
        "Answer 2":
            "Impressive"
            $ section4 += 1
            jump section4
        "Answer 3":
            "That's not quite right!"
            jump section4question1
        "Answer 4":
            "That's not quite right!"
            jump section4question1

label section4question2:
    a "Question 2"
    menu:
        "Answer 1":
            "That's not quite right!"
            jump section4question2
        "Answer 2":
            "That's not quite right!"
            jump section4question2
        "Answer 3":
            "Well done"
            $ section4 += 1
            jump section4
        "Answer 4":
            "That's not quite right!"
            jump section4question2

label section4question3:
    a "Question 3"
    menu:
        "Answer 1":
            "That's not quite right!"
            jump section4question3
        "Answer 2":
            "That's not quite right!"
            jump section4question3
        "Answer 3":
            "Good job"
            $ section4 += 1
            jump section4
        "Answer 4":
            "That's not quite right!"
            jump section4question3

label section4question4:
    a "Question 4"
    menu:
        "Answer 1":
            "That's not quite right!"
            jump section4question4
        "Answer 2":
            "That's not quite right!"
            jump section4question4
        "Answer 3":
            "You've done it"