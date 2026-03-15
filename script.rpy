# characters
define a = Character("Mr Algorithm")
define yn = Character("[Name]")
define g = Character("System")

# variables
init python:
    lore_route = True
    knowledge_of_enemy = False
    knowledge_of_recuperation = False
    friendship = 0
    section1 = 0
    section2 = 0
    section3 = 0
    section4 = 0
    section5 = 0
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
    Answer_5_2 = ""
    Answer_5_3 = ""

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
    hide mr_al_talk
    hide mr_al_neutral
    show mr_al_neutral at small

    menu:
        "A":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's right! Nice attention to detail."
            $ section1 += 1
            jump section1
        "B":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Not quite; remember that “sizeof” returns the number of bytes the object takes up."
            jump section1question1
        "C":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "...hmm. Looks like you've got a malformed array there in the first line!"
            jump section1question1
        "D":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Alan Please add details."
            jump section1question1

label section1question2:
    show mr_al_talk at custom_pos
    a "Question 2: Here is a Linked List implementation. What is the output of the following code?"
    show mr_al_neutral at custom_pos
    $ Answer_1_2 = renpy.input("Input your answer here", length = 64)
    if Answer_1_2 == "28.0" or Answer_1_2 == "28":
        hide mr_al_neutral
        a "Good Job"
        $ section1 += 1
        jump section1
    else:
        hide mr_al_neutral
        a "That's not quite right!"
        jump section1question2

label section1question3:
    show mr_al_talk at custom_pos
    a "Question 3: Type the name of the variable that causes a leak in this code:"
    show mr_al_neutral at custom_pos
    $ Answer_1_3 = renpy.input("Input your answer here", length = 64)
    if Answer_1_3 == "ptr2":
        hide mr_al_neutral
        a "You’ve done it!"
        $ section1 += 1
        jump section1
    else:
        hide mr_al_neutral
        a "That's not quite right!"
        jump section1question3

label section1question4:
    show mr_al_talk at custom_pos
    a "Question 4: Fill in the blank to pass this test:"
    show mr_al_neutral at custom_pos
    $ Answer_1_4 = renpy.input("Input your answer here", length = 64)
    #python:
        #input_list = list(Answer_1_4)
        #if (input_list[0] % 2 == 1) and (my_list[1]) and (my_list[-1] % 5 == 4) and len(my_list > 4):
            #correct = True
    $ correct = True # remove later
    if correct:
        hide mr_al_neutral
        a "Impressive work!"
        $ section1 += 1
        $ correct = False
        jump section1
    else:
        hide mr_al_neutral
        a "That's not quite right!"
        jump section1question4

label section1question5:
    show mr_al_neutral at custom_pos
    a "Question 5: Enter the line number where this linked list implementation fails"
    show mr_al_neutral at custom_pos
    $ Answer_1_5 = renpy.input("Input your answer here", length = 64)
    if Answer_1_5 == "11":
        hide mr_al_neutral
        a "Well Done"
        $ section1 += 1
        jump section1
    else:
        hide mr_al_neutral
        a "That's not quite right!"
        jump section1question5

label intermission1:
    hide mr_al_neutral
    show mr_al_talk at custom_pos
    a "How did you find the first topic?"
    hide mr_al_talk
    show mr_al_neutral at custom_pos
    menu:
        "It was really easy":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Well, they'll only get harder from here on out, so make sure you're prepared!"

        "It was super challenging":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Hopefully you were able to learn from your mistakes" # something along these lines

    a "Are you ready to move on?"
    hide mr_al_talk
    show mr_al_neutral at custom_pos
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
    a "Question 1: Which of these is NOT an ADT?"
    menu:
        "Byte":
            a "Good Job"
            $ section2 += 1
            jump section2
        "String":
            a "That's not quite right!"
            jump section2question1
        "List":
            a "That's not quite right!"
            jump section2question1
        "Stack":
            a "That's not quite right!"
            jump section2question1

label section2question2:
    a "Question 2: Consider the following stack implementation:"# Show Stack
    a "What does the following code print?" # show code
    $ Answer_2_2 = renpy.input("Input your answer here", length = 64)
    if Answer_2_2 == "3":
        a "You’ve done it"
        $ section2 += 1
        jump section2
    else:
        a "That's not quite right!"
        jump section2question2

label section2question3:
    a "Question 3: Consider the following queue implementation:"# Show Queue
    a "What does the following code print?" # show code
    $ Answer_2_3 = renpy.input("Input your answer here", length = 64)
    if Answer_2_3 == "1":
        a "Impressive"
        $ section2 += 1
        jump section2
    else:
        a "That's not quite right!"
        jump section2question3

label section2question4:
    a "Question 4: What is the time complexity of this program?"
    menu:
        "Linear":
            a "That's not quite right!"
            jump section2question4
        "Polynomial":
            a "That's not quite right!"
            jump section2question4
        "Constant":
            a "Well Done"
            $ section2 += 1
            jump section2
        "Exponential":
            a "That's not quite right!"
            jump section2question4

label section2question5:
    a "Question 5: Fill in the blanks:"
    $ Answer_2_5_a = renpy.input("Blank #1: Input your answer here", length = 64)
    $ Answer_2_5_b = renpy.input("Blank #2: Input your answer here", length = 64)
    $ Answer_2_5_c = renpy.input("Blank #3: Input your answer here", length = 64)
    if Answer_2_5_a == "6" and Answer_2_5_b == "5" and Answer_2_5_c == "idx":
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
    a "Question 1: How many nodes are in a full BST of height 'h'?"
    menu:
        "log2(h)":
            a "That's not quite right!"
            jump section3question1
        "2h+1":
            a "That's not quite right!"
            jump section3question1
        "h^2":
            a "That's not quite right!"
            jump section3question1
        "(2^h)-1":
            a "Well done"
            $ section3 += 1
            jump section3
label section3question2:
    a "Which of the following trees are AVL?"
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
    a "Question 3: What is the balance of this AVL tree?"
    $ Answer_3_3 = renpy.input("Input your answer here", length = 64)
    if Answer_3_3 == "-1":
        a "Well done"
        $ section3 += 1
        jump section3
    else:
        a "That's not quite right!"
        jump section3question3

label section3question4:
    a "Question 4: What is the time complexity of a B+ Tree Search?"
    menu:
        "O(n)":
            a "That's not quite right!"
            jump section3question4
        "O(n log (n))":
            a "Good job"
            $ section3 += 1
        "O(n^2)":
            a "That's not quite right!"
            jump section3question4
        "O(1)":
            a "That's not quite right!"
            jump section3question4

label section3question5:
    a "Question 5: Consider the following binary heaps:" # Show binary heaps
    a "Which of the following is a correct merge of A and B?" # show options
    menu:
        "A":
            a "You've done it"
            $ section3 += 1
            jump section3
        "B":
            a "That's not quite right!"
            jump section3question5
        "C":
            a "That's not quite right!"
            jump section3question5
        "D":
            a "That's not quite right!"
            jump section3question5

label intermission3:
    a "How did you find the third topic?"
    menu:
        "It was really easy":
            a "Well they'll only get harder from here on out, so make sure you're prepared"
        "It was super challenging":
            a "Hopefully you were able to learn from your mistakes"
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
    a "Question 1: Which of the following sorting algorithms achieves O(n log(n)) complexity with perfect stability?"
    menu:
        "Insertion":
            a "That's not quite right!"
            jump section4question1
        "Merge":
            a "Impressive"
            $ section4 += 1
            jump section4
        "Heap":
            a "That's not quite right!"
            jump section4question1
        "Quick":
            a "That's not quite right!"
            jump section4question1

label section4question2:
    a "Question 2: Radix Sort is an example of what sorting algorithm?"
    menu:
        "Merge":
            a "That's not quite right!"
            jump section4question2
        "Quick":
            a "That's not quite right!"
            jump section4question2
        "Non-Comparison":
            a "Well done"
            $ section4 += 1
            jump section4
        "Pigeonhole":
            a "That's not quite right!"
            jump section4question2

label section4question3:
    a "Question 3: Which of these algorithms are unstable?"
    menu:
        "Insertion":
            a "That's not quite right!"
            jump section4question3
        "Selection":
            a "That's not quite right!"
            jump section4question3
        "Radix":
            a "Good job"
            $ section4 += 1
            jump section4
        "Merge":
            a "That's not quite right!"
            jump section4question3

label section4question4:
    a "Question 4: Which of these algorithms has best average-case time complexity for large n?"
    menu:
        "Answer 1":
            a "That's not quite right!"
            jump section4question4
        "Answer 2":
            a "That's not quite right!"
            jump section4question4
        "Answer 3":
            a "You've done it"
            $ section4 += 1
            jump section4
        "Answer 4":
            a "That's not quite right"
            jump section4question4


label section4question5:
    a "Question 5: Consider the following list: [1,45,876,3,192,23,58]. When implementing quicksort, what would be the value of the most efficient pivot in the first step?"
    $ Answer_4_5 = renpy.input("Input your answer here", length = 64)
    if Answer_4_5 == "3":
        a "Well done"
        $ section4 += 1
        jump section4
    else:
        "That's not quite right!"
        jump section4question5

label intermission4:
    a "How did you find the fourth topic?"
    menu:
        "It was really easy":
            a "Well they'll only get harder from here on out, so make sure you're prepared"
        "It was super challenging":
            a "Hopefully you were able to learn from your mistakes"
    a "Are you ready to move on?"

    if lore_route:
        menu:
            "I'm ready":
                a "Let us begin!"
                jump section4
            "Are you real?":
                jump intermission4lore
    else:
        menu:
            "I'm ready":
                a "Let us begin!"
                jump section5

label intermission4lore:
    if friendship == 1:
        a "I am alive and can think for myself"
        menu:
            "That's awesome! I've never seen a computer program this advanced before":
                a "I am a very advanced program!"
                $ friendship += 1
            "I don't believe you. This must be a trick.":
                a "Believe what you want, I guess."
                $ friendship -= 1
    else:
        a "Yes"
        menu:
            "That's awesome. I've never seen a computer program this advanced before":
                a "I am a very advanced program!"
                $ friendship += 1
            "I don't believe you. This must be a trick.":
                a "Believe what you want, I guess."
                $ friendship -= 1
    jump section5

label section5:
    if section5 == 0:
        jump section5question1
    elif section5 == 1:
        jump section5question2
    elif section5 == 2:
        jump section5question3
    elif section5 == 3:
        jump section5question4
    elif section5 == 4:
        jump section5question5
    else:
        jump intermission5

label section5question1:
    a "Question 1: What graph does this adjacency matrix represent?"
    menu:
        "A":
            a "That's not quite right!"
            jump section5question1
        "B":
            a "Well done"
            $ section5 += 1
            jump section5
        "C":
            a "That's not quite right!"
            jump section5question1
        "D":
            a "That's not quite right!"
            jump section5question1

label section5question2:
    a "Question 2: Consider the following graph:"# show nightmare graph
    a "Using Djikstra's Algorithm, what is length of the shortest path from A to F?"
    $ Answer_5_2 = renpy.input("Input your answer here", length = 64)
    if Answer_5_2 == "7":
        a "Well done"
        $ section5 += 1
        jump section5
    else:
        a "That's not quite right!"
        jump section5question2

label section5question3:
    a "Question 3: Consider the following graph:" # show other graph#
    a "Using Jarnik-Prim, what is the weight of the minimal spanning tree of this graph?"
    $ Answer_5_3 = renpy.input("Input your answer here", length = 64)
    if Answer_5_3 == "17":
        a "Well done"
        $ section5 += 1
        jump section5
    else:
        a "That's not quite right!"
        jump section5question3

label section5question4:
    a "Question 4: Given a finite undirected graph G with n edges, what is the sum of its vertex degrees?"
    menu:
        "(n^2)/2":
            a "That's not quite right!"
            jump section5question4
        "(n(n-1))/2":
            a "That's not quite right!"
            jump section5question4
        "2n":
            a "Well done"
            $ section5 += 1
            jump section5
        "log2(n)":
            a "That's not quite right!"
            jump section5question4

label section5question5:
    a "Question 5: What item is a type of graph?"
    menu:
        "Tree":
            a "Well done"
            $ section5 += 1
            jump section5
        "Edge":
            a "That's not quite right!"
            jump section5question5
        "Function":
            a "That's not quite right!"
            jump section5question5
        "Grammar":
            a "That's not quite right!"
            jump section5question5

label intermission5:
    a "How did you find the fifth topic?"
    menu:
        "It was really easy":
            a "Well they'll only get harder from here on out, so make sure you're prepared"
        "It was super challenging":
            a "Hopefully you were able to learn from your mistakes"
    a "Are you ready to move on?"

    if lore_route:
        if friendship>0:
            menu:
                "I'm ready":
                    a "Let us begin!"
                    jump section5
                "Why are you in a computer program?":
                    jump intermission5lore
        else:
            menu:
                "I'm ready":
                    a "Let us begin!"
                    jump section5
                "Lets say I believe you, why are you in a computer then?":
                    jump intermission5lore
    else:
        menu:
            "I'm ready":
                a "Let us begin!"
                jump section5

label intermission5lore:
    if friendship == 2:
        a "I was recuperating here and hiding from my mortal enemy..."
        menu:
            "I hope you are feeling better now!":
                $ friendship += 1
                $ knowledge_of_enemy = True
                $ knowledge_of_recuperation = True
                a "Thank you!"
            "Whatever.":
                $ friendship -= 1
                $ knowledge_of_enemy = True
                $ knowledge_of_recuperation = True
                a "..."
    elif friendship == 1 or friendship == 0:
        a "I was recuperating here"
        menu:
            "I hope you are feeling better now!":
                $ friendship += 1
                $ knowledge_of_enemy = False
                $ knowledge_of_recuperation = True
                a "Thank you!"
            "Whatever.":
                $ friendship -= 1
                $ knowledge_of_enemy = False
                $ knowledge_of_recuperation = True
                a "..."
    else:
        a "Why do you even care?"
        menu:
            "Because I want to get to know you better.":
                $ friendship += 1
                $ knowledge_of_recuperation = False
                $ knowledge_of_enemy = False
                a "..."
            "Just wanted to see what you are programmed to say.":
                $ friendship -= 1
                $ knowledge_of_recuperation = False
                $ knowledge_of_enemy = False
                a "..."