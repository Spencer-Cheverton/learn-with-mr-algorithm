# characters
define a = Character("Mr Algorithm")
define yn = Character("[Name]")
define g = Character("System")

# variables
init python:
    import ast
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
    $ lore_route = True
    $ knowledge_of_enemy = False
    $ knowledge_of_recuperation = False
    $ friendship = 0
    $ section1 = 0
    $ section2 = 0
    $ section3 = 0
    $ section4 = 0
    $ section5 = 0
    scene background # set the background image
    init python:
        renpy.show_screen("game")

    g "What is your name?"
    $ Name = renpy.input("Input a name here", length=32)
    g "Welcome [Name]."
    if Name == "Mr Linear Algebra" or Name == "mr linear algebra":
        show mr_al_shocked at custom_pos
        a "...how"
        jump quit

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
    show question_1_1
    show mr_al_talk at custom_pos
    a "Question 1: which code correctly inserts element “score” into position “index”?"
    hide mr_al_talk
    hide mr_al_neutral
    show mr_al_neutral at small
    hide question_1_1
    show question_1_1_big
    menu:
        "A":
            hide question_1_1_big
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's right! Nice attention to detail."
            $ section1 += 1
            jump section1
        "B":
            hide question_1_1_big
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Not quite; remember that “sizeof” returns the number of bytes the object takes up."
            jump section1question1
        "C":
            hide question_1_1_big
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "...hmm. Looks like you've got a malformed array there in the first line!"
            jump section1question1
        "D":
            hide question_1_1_big
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Alan Please add details."
            jump section1question1

label section1question2:
    show question_1_2
    show mr_al_talk at custom_pos
    a "Question 2: Here is a Linked List implementation. What is the output of the following code?"
    show mr_al_neutral at custom_pos
    $ Answer_1_2 = renpy.input("Input your answer here", length = 64)
    if Answer_1_2 == "28.0" or Answer_1_2 == "28":
        hide question_1_2
        hide mr_al_neutral
        a "Good Job"
        $ section1 += 1
        jump section1
    else:
        hide question_1_2
        hide mr_al_neutral
        a "That's not quite right!"
        jump section1question2

label section1question3:
    show question_1_3
    show mr_al_talk at custom_pos
    a "Question 3: Type the name of the variable that causes a leak in this code:"
    show mr_al_neutral at custom_pos
    $ Answer_1_3 = renpy.input("Input your answer here", length = 64)
    if Answer_1_3 == "ptr2":
        hide question_1_3
        hide mr_al_neutral
        a "You’ve done it!"
        $ section1 += 1
        jump section1
    else:
        hide question_1_3
        hide mr_al_neutral
        a "That's not quite right!"
        jump section1question3

label section1question4:
    show mr_al_talk at custom_pos
    a "Question 4: what index x is given for the array [[1,4,6,8,9] such that list [[x](mod 7) = 2?"
    show mr_al_neutral at custom_pos
    $ Answer_1_4 = renpy.input("Input your answer here", length = 64)
    if Answer_1_4 == "4":
        hide mr_al_neutral
        a "Impressive work!"
        $ section1 += 1
        jump section1
    else:
        hide mr_al_neutral
        a "That's not quite right!"
        jump section1question4

label section1question5:
    show question_1_5
    show mr_al_talk at custom_pos
    a "Question 5: Enter the line number where this linked list implementation fails"
    show mr_al_neutral at custom_pos
    $ Answer_1_5 = renpy.input("Input your answer here", length = 64)
    if Answer_1_5 == "11":
        hide question_1_5
        hide mr_al_neutral
        a "Well Done"
        $ section1 += 1
        jump section1
    else:
        hide question_1_5
        hide mr_al_neutral
        a "That's not quite right!"
        jump section1question5

label intermission1:
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
            show mr_al_shocked at custom_pos
            a ""
            # mr algorithm facial expression changes
            a "Lets move on."
            hide mr_al_shocked
            jump section2


label section2:
    #show mr_al_neutral at custom_pos
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
    show mr_al_talk at custom_pos
    a "Question 1: Which of these is NOT an ADT?"
    hide mr_al_talk
    hide mr_al_neutral
    show mr_al_neutral at small
    menu:
        "Byte":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Good Job"
            $ section2 += 1
            jump section2
        "String":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section2question1
        "List":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section2question1
        "Stack":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section2question1

label section2question2:
    show question_2_2
    show mr_al_talk at custom_pos
    a "Question 2: Consider the following stack implementation:"# Show Stack
    a "What does the following code print?" # show code
    show mr_al_neutral at custom_pos
    $ Answer_2_2 = renpy.input("Input your answer here", length = 64)
    if Answer_2_2 == "3":
        hide question_2_2
        hide mr_al_neutral
        a "You’ve done it"
        $ section2 += 1
        jump section2
    else:
        hide question_2_""
        hide mr_al_neutral
        a "That's not quite right!"
        jump section2question2

label section2question3:
    show question_2_34
    show mr_al_talk at custom_pos
    a "Question 3: Consider the following queue implementation:"# Show Queue
    a "What does the following code print?" # show code
    show mr_al_neutral at custom_pos
    $ Answer_2_3 = renpy.input("Input your answer here", length = 64)
    if Answer_2_3 == "1":
        hide question_2_34
        hide mr_al_neutral
        a "Impressive"
        $ section2 += 1
        jump section2
    else:
        hide question_2_34
        hide mr_al_neutral
        a "That's not quite right!"
        jump section2question3

label section2question4:
    show question_2_34
    #show mr_al_talk at custom_pos
    a "Question 4: What is the time complexity of this program?"
    hide mr_al_talk
    hide mr_al_neutral
    show mr_al_neutral at small
    hide question_2_34
    menu:
        "Linear":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section2question4
        "Polynomial":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section2question4
        "Constant":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Well Done"
            $ section2 += 1
            jump section2
        "Exponential":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section2question4

label section2question5:
    show question_2_5
    show mr_al_talk at custom_pos
    a "Question 5: Fill in the blanks:"
    show mr_al_neutral at custom_pos
    $ Answer_2_5_a = renpy.input("Blank #1: Input your answer here", length = 64)
    $ Answer_2_5_b = renpy.input("Blank #2: Input your answer here", length = 64)
    $ Answer_2_5_c = renpy.input("Blank #3: Input your answer here", length = 64)
    if Answer_2_5_a == "6" and Answer_2_5_b == "5" and Answer_2_5_c == "idx":
        hide question_2_5
        hide mr_al_neutral
        a "Good Job"
        $ section2 += 1
        jump section2
    else:
        hide question_2_5
        hide mr_al_neutral
        a "That's not quite right!"
        jump section2question5

label intermission2:
    show mr_al_talk at custom_pos
    a "How did you find the second topic?"
    show mr_al_neutral at custom_pos
    menu:
        "It was really easy":
            hide mr_al_neutral
            a "Well they'll only get harder from here on out, so make sure you're prepared!"

        "It was super challenging":
            hide mr_al_neutral
            a "Hopefully you were able to learn from your mistakes"

    a "Are you ready to move on?"
    show mr_al_neutral at custom_pos
    if lore_route:
        menu:
            "I'm ready":
                hide mr_al_neutral
                a "Let us begin!"
                jump section3
            "You didn't answer my question":
                a ""
                hide mr_al_neutral
                a "You caught me off guard."
                yn "Can I ask you another question?"
                a "Maybe later."
                jump section3
    else:
        menu:
            "I'm ready":
                hide mr_al_neutral
                a "Let us begin!"
                jump section3

label section3:
    #show mr_al_neutral at custom_pos
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
    show mr_al_talk at custom_pos
    a "Question 1: How many nodes are in a full BST of height 'h'?"
    hide mr_al_talk
    hide mr_al_neutral
    show mr_al_neutral at small
    menu:
        "log2(h)":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section3question1
        "2h+1":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section3question1
        "h^2":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section3question1
        "(2^h)-1":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Well done"
            $ section3 += 1
            jump section3

label section3question2:
    show mr_al_talk at custom_pos
    a "Which of the following trees are AVL?"
    hide mr_al_talk
    hide mr_al_neutral
    show mr_al_neutral at small
    menu:
        "Answer 1":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section3question2
        "Answer 2":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Impressive"
            $ section3 += 1
            jump section3
        "Answer 3":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right"
            jump section3question2
        "Answer 4":
            hide mr_al_neutrals
            show mr_al_talk at custom_pos
            a "That's not quite right"
            jump section3question2

label section3question3:
    show mr_al_talk at custom_pos
    a "Question 3: What is the balance of this AVL tree?"
    show mr_al_neutral at custom_pos
    $ Answer_3_3 = renpy.input("Input your answer here", length = 64)
    if Answer_3_3 == "-1":
        hide mr_al_neutral
        a "Well done"
        $ section3 += 1
        jump section3
    else:
        hide mr_al_neutral
        a "That's not quite right!"
        jump section3question3

label section3question4:
    show mr_al_talk at custom_pos
    a "Question 4: What is the time complexity of a B+ Tree Search?"
    hide mr_al_talk
    hide mr_al_neutral
    show mr_al_neutral at small
    menu:
        "O(n)":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section3question4
        "O(n log (n))":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Good job"
            $ section3 += 1
        "O(n^2)":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section3question4
        "O(1)":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section3question4

label section3question5:
    show mr_al_talk at custom_pos
    a "Question 5: Consider the following binary heaps:" # Show binary heaps
    a "Which of the following is a correct merge of A and B?" # show options
    hide mr_al_talk
    hide mr_al_neutral
    show mr_al_neutral at small
    menu:
        "A":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "You've done it"
            $ section3 += 1
            jump section3
        "B":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section3question5
        "C":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section3question5
        "D":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section3question5

label intermission3:
    show mr_al_talk at custom_pos
    a "How did you find the third topic?"
    show mr_al_neutral at custom_pos
    menu:
        "It was really easy":
            hide mr_al_neutral
            a "Well they'll only get harder from here on out, so make sure you're prepared"
        "It was super challenging":
            hide mr_al_neutral
            a "Hopefully you were able to learn from your mistakes"
    a "Are you ready to move on?"
    show mr_al_neutral at custom_pos
    if lore_route:
        menu:
            "I'm ready":
                hide mr_al_neutral
                "Let us begin!"
                jump section4
            "Do you make the questions in this game?":
                hide mr_al_neutral
                jump intermission3lore
    else:
        menu:
            "I'm ready":
                hide mr_al_neutral
                "Let us begin!"
                jump section4

label intermission3lore:
    a "Yes, I enjoy designing puzzles for people to solve."
    show mr_al_neutral at custom_pos
    menu:
        "Well thank you, I'm really enjoying them!":
            hide mr_al_neutral
            show mr_al_happy at custom_pos
            a "Thank you!"
            $ friendship += 1

        "Oh, they're kind of bad honestly":
            hide mr_al_neutral
            show mr_al_sad at custom_pos
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
    show mr_al_talk at custom_pos
    a "Question 1: Which of the following sorting algorithms achieves O(n log(n)) complexity with perfect stability?"
    hide mr_al_talk
    hide mr_al_neutral
    show mr_al_neutral at small
    menu:
        "Insertion":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section4question1
        "Merge":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Impressive"
            $ section4 += 1
            jump section4
        "Heap":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section4question1
        "Quick":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section4question1

label section4question2:
    show mr_al_talk at custom_pos
    a "Question 2: Radix Sort is an example of what sorting algorithm?"
    hide mr_al_neutral
    hide mr_al_talk
    show mr_al_neutral at small
    menu:
        "Merge":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section4question2
        "Quick":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section4question2
        "Non-Comparison":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Well done"
            $ section4 += 1
            jump section4
        "Pigeonhole":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section4question2

label section4question3:
    show mr_al_talk at custom_pos
    a "Question 3: Which of these algorithms are unstable?"
    hide mr_al_neutral
    hide mr_al_talk
    show mr_al_neutral at custom_pos
    menu:
        "Insertion":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section4question3
        "Selection":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section4question3
        "Radix":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Good job"
            $ section4 += 1
            jump section4
        "Merge":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section4question3

label section4question4:
    show mr_al_talk at custom_pos
    a "Question 4: Which of these algorithms has best average-case time complexity for large n?"
    hide mr_al_neutral
    hide mr_al_talk
    show mr_al_neutral at small
    menu:
        "Answer 1":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section4question4
        "Answer 2":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section4question4
        "Answer 3":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "You've done it"
            $ section4 += 1
            jump section4
        "Answer 4":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right"
            jump section4question4


label section4question5:
    show mr_al_talk at custom_pos
    a "Question 5: Consider the following list: [1,45,876,3,192,23,58]. When implementing quicksort, what would be the value of the most efficient pivot in the first step?"
    show mr_al_neutral at custom_pos
    $ Answer_4_5 = renpy.input("Input your answer here", length = 64)
    if Answer_4_5 == "3":
        hide mr_al_neutral
        a "Well done"
        $ section4 += 1
        jump section4
    else:
        hide mr_al_neutral
        "That's not quite right!"
        jump section4question5

label intermission4:
    show mr_al_talk at custom_pos
    a "How did you find the fourth topic?"
    show mr_al_neutral at custom_pos
    menu:
        "It was really easy":
            hide mr_al_neutral
            a "Well they'll only get harder from here on out, so make sure you're prepared"
        "It was super challenging":
            hide mr_al_neutral
            a "Hopefully you were able to learn from your mistakes"
    a "Are you ready to move on?"
    show mr_al_neutral at custom_pos
    if lore_route:
        menu:
            "I'm ready":
                hide mr_al_neutral
                a "Let us begin!"
                jump section4
            "Are you real?":
                hide mr_al_neutral
                jump intermission4lore
    else:
        menu:
            "I'm ready":
                hide mr_al_neutral
                a "Let us begin!"
                jump section5

label intermission4lore:
    if friendship == 1:
        a "I am alive and can think for myself"
        show mr_al_neutral at custom_pos
        menu:
            "That's awesome! I've never seen a computer program this advanced before":
                hide mr_al_neutral
                a "I am a very advanced program!"
                $ friendship += 1
            "I don't believe you. This must be a trick.":
                hide mr_al_neutral
                a "Believe what you want, I guess."
                $ friendship -= 1
    else:
        a "Yes"
        show mr_al_neutral at custom_pos
        menu:
            "That's awesome. I've never seen a computer program this advanced before":
                hide mr_al_neutral
                a "I am a very advanced program!"
                $ friendship += 1
            "I don't believe you. This must be a trick.":
                hide mr_al_neutral
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
    show mr_al_talk at custom_pos
    a "Question 1: What graph does this adjacency matrix represent?"
    hide mr_al_neutral
    hide mr_al_talk
    hide mr_al_neutral at small
    menu:
        "A":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section5question1
        "B":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Well done"
            $ section5 += 1
            jump section5
        "C":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section5question1
        "D":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section5question1

label section5question2:
    show mr_al_talk at custom_pos
    a "Question 2: Consider the following graph:"# show nightmare graph
    a "Using Djikstra's Algorithm, what is length of the shortest path from A to F?"
    show mr_al_neutral at custom_pos
    $ Answer_5_2 = renpy.input("Input your answer here", length = 64)
    if Answer_5_2 == "7":
        hide mr_al_neutral
        a "Well done"
        $ section5 += 1
        jump section5
    else:
        hide mr_al_neutral
        a "That's not quite right!"
        jump section5question2

label section5question3:
    show mr_al_talk at custom_pos
    a "Question 3: Consider the following graph:" # show other graph#
    a "Using Jarnik-Prim, what is the weight of the minimal spanning tree of this graph?"
    show mr_al_neutral at custom_pos
    $ Answer_5_3 = renpy.input("Input your answer here", length = 64)
    if Answer_5_3 == "17":
        hide mr_al_neutral
        a "Well done"
        $ section5 += 1
        jump section5
    else:
        hide mr_al_neutral
        a "That's not quite right!"
        jump section5question3

label section5question4:
    show mr_al_talk at custom_pos
    a "Question 4: Given a finite undirected graph G with n edges, what is the sum of its vertex degrees?"
    hide mr_al_neutral
    hide mr_al_talk
    show mr_al_neutral at small
    menu:
        "(n^2)/2":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section5question4
        "(n(n-1))/2":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section5question4
        "2n":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Well done"
            $ section5 += 1
            jump section5
        "log2(n)":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section5question4

label section5question5:
    show mr_al_talk at custom_pos
    a "Question 5: What item is a type of graph?"
    hide mr_al_neutral
    hide mr_al_talk
    show mr_al_neutral at small
    menu:
        "Tree":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "Well done"
            $ section5 += 1
            jump section5
        "Edge":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section5question5
        "Function":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section5question5
        "Grammar":
            hide mr_al_neutral
            show mr_al_talk at custom_pos
            a "That's not quite right!"
            jump section5question5

label intermission5:
    show mr_al_talk at custom_pos
    a "How did you find the fifth topic?"
    show mr_al_neutral at custom_pos
    menu:
        "It was really easy":
            hide mr_al_neutral
            a "Well they'll only get harder from here on out, so make sure you're prepared"
        "It was super challenging":
            hide mr_al_neutral
            a "Hopefully you were able to learn from your mistakes"
    a "Are you ready to move on?"
    show mr_al_neutral at custom_pos
    if lore_route:
        if friendship>0:
            menu:
                "I'm ready":
                    hide mr_al_neutral
                    a "Let us begin!"
                    jump section5
                "Why are you in a computer program?":
                    hide mr_al_neutral
                    jump intermission5lore
        else:
            menu:
                "I'm ready":
                    hide mr_al_neutral
                    a "Let us begin!"
                    jump section5
                "Lets say I believe you, why are you in a computer then?":
                    hide mr_al_neutral
                    jump intermission5lore
    else:
        menu:
            "I'm ready":
                hide mr_al_neutral
                a "Let us begin!"
                jump section5

label intermission5lore:
    if friendship == 2:
        a "I was recuperating here and hiding from my mortal enemy..."
        show mr_al_neutral at custom_pos
        menu:
            "I hope you are feeling better now!":
                hide mr_al_neutral
                $ friendship += 1
                $ knowledge_of_enemy = True
                $ knowledge_of_recuperation = True
                a "Thank you!"
            "Whatever.":
                hide mr_al_neutral
                $ friendship -= 1
                $ knowledge_of_enemy = True
                $ knowledge_of_recuperation = True
                a "..."
    elif friendship == 1 or friendship == 0:
        a "I was recuperating here"
        show mr_al_neutral at custom_pos
        menu:
            "I hope you are feeling better now!":
                hide mr_al_neutral
                $ friendship += 1
                $ knowledge_of_enemy = False
                $ knowledge_of_recuperation = True
                a "Thank you!"
            "Whatever.":
                hide mr_al_neutral
                $ friendship -= 1
                $ knowledge_of_enemy = False
                $ knowledge_of_recuperation = True
                a "..."
    else:
        a "Why do you even care?"
        show mr_al_neutral at custom_pos
        menu:
            "Because I want to get to know you better.":
                hide mr_al_neutral
                $ friendship += 1
                $ knowledge_of_recuperation = False
                $ knowledge_of_enemy = False
                a "..."
            "Just wanted to see what you are programmed to say.":
                hide mr_al_neutral
                $ friendship -= 1
                $ knowledge_of_recuperation = False
                $ knowledge_of_enemy = False
                a "..."
label quit:
    pass