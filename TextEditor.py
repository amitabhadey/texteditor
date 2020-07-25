# =============================================================================
# Using Tkinter to develop the interface of the text editor and textstat to analyze and grade the composition
# =============================================================================

from tkinter import *
import tkinter as tk
import textstat

# =============================================================================
# Setting up the interface for the Text Editor
# =============================================================================

root = tk.Tk()

# =============================================================================
# A tkinter canvas can be used to draw in a window. You can draw several widgets in the canvas.
# The canvas has two coordinate systems: the window system (left top corner x=0,y=0) and the canvas
# coordinate system that defines where items are drawn.
# =============================================================================

canvas1 = tk.Canvas(root, width = 1000, height = 1000,  relief = 'raised')
canvas1.pack()

# =============================================================================
# Using PhotoImage to make our interface accept an image object. This way we can set a
# background image for our software.
# =============================================================================

background_image = tk.PhotoImage(file='pic.png', master=root)
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# =============================================================================
# Using Label to create a heading and instruction (creating difference with font size)
# =============================================================================

label1 = tk.Label(root, text='Neuro Text Editor', bg = "#a4de02")
label1.config(font=('helvetica', 20))
canvas1.create_window(400, 50, window=label1)

label2 = tk.Label(root, text='Create your Composition:', bg = "#a4de02")
label2.config(font=('helvetica', 10))
canvas1.create_window(400, 120, window=label2)

# =============================================================================
# Using Text to create a text box for users to type their composition.
# =============================================================================

textbox = tk.Text(root, width=100, height=10, wrap=WORD, pady=10, padx=10, bd=5, font=("Helvetica", 10))
canvas1.create_window(400, 250, window=textbox)

# =============================================================================
# The main algorithm to grade composition. Works on top of textstat library.
# Each blob of instruction converts the grade score into a string, executes a print statement
# in terminal, creates a label space to spit out the output, and uses canvas to declare coordinates
# of where the label should be displayed in the window
# =============================================================================

# =============================================================================
# The variables are prefixed with neuro because that's the name of my project
# =============================================================================

def getneurograde():

    composition = textbox.get("1.0", END)

    neuro_flesch_reading_ease = str(textstat.flesch_reading_ease(composition))
    print ('Flesch Reading Ease : ' + neuro_flesch_reading_ease)
    output1 = tk.Label(root, text= 'Flesch Reading Ease : ' + neuro_flesch_reading_ease, font=('helvetica', 10), bg = "#a4de02")
    canvas1.create_window(400, 500, window=output1)

    neuro_flesch_kincaid_grade = str (textstat.flesch_kincaid_grade(composition))
    print ('Flesch Kincaid Grade : ' + neuro_flesch_reading_ease)
    output2 = tk.Label(root, text= 'Flesch Kincaid Grade : ' + neuro_flesch_kincaid_grade ,font=('helvetica', 10), bg = "#a4de02")
    canvas1.create_window(400, 520, window=output2)

    neuro_smog_index = str (textstat.smog_index(composition))
    print ('Smog Index : ' + neuro_smog_index)
    output3 = tk.Label(root, text= 'Smog Index : ' + neuro_smog_index ,font=('helvetica', 10), bg = "#a4de02")
    canvas1.create_window(400, 540, window=output3)

    neuro_coleman_liau_index = str(textstat.coleman_liau_index(composition))
    print ('Coleman Liau Index : ' + neuro_coleman_liau_index)
    output4 = tk.Label(root, text= 'Coleman Liau Index : ' + neuro_coleman_liau_index ,font=('helvetica', 10), bg = "#a4de02")
    canvas1.create_window(400, 560, window=output4)

    neuro_automated_readability_index = str(textstat.automated_readability_index(composition))
    print ('Automated Readability Index : ' + neuro_automated_readability_index)
    output5 = tk.Label(root, text= 'Automated Readibility Index : ' + neuro_automated_readability_index ,font=('helvetica', 10), bg = "#a4de02")
    canvas1.create_window(400, 580, window=output5)

    neuro_dale_chall_readability_score = str(textstat.dale_chall_readability_score(composition))
    print ('Dale Chall Readability Score : ' + neuro_dale_chall_readability_score)
    output6 = tk.Label(root, text= 'Dale Chall Readability Score : ' + neuro_dale_chall_readability_score ,font=('helvetica', 10), bg = "#a4de02")
    canvas1.create_window(400, 600, window=output6)

    neuro_difficult_words = str(textstat.difficult_words(composition))
    print('Difficult Words : ' + neuro_difficult_words)
    output7 = tk.Label(root, text= 'Difficult Words : ' + neuro_difficult_words ,font=('helvetica', 10), bg = "#a4de02")
    canvas1.create_window(400, 620, window=output7)

    neuro_linsear_write_formula = str(textstat.linsear_write_formula(composition))
    print ('Linsear Write Formula : ' + neuro_linsear_write_formula)
    output8 = tk.Label(root, text= 'Linsear Write Formula : ' + neuro_linsear_write_formula ,font=('helvetica', 10), bg = "#a4de02")
    canvas1.create_window(400, 640, window=output8)

    neuro_gunning_fog = str(textstat.gunning_fog(composition))
    print('Gunning Fog : ' + neuro_gunning_fog)
    output9 = tk.Label(root, text= 'Gunning Fog : ' + neuro_gunning_fog ,font=('helvetica', 10), bg = "#a4de02")
    canvas1.create_window(400, 660, window=output9)

    neuro_text_standard = str(textstat.text_standard(composition))
    print('Text Standard : ' + neuro_text_standard)
    output10 = tk.Label(root, text= 'Text Standard : ' + neuro_text_standard ,font=('helvetica', 10), bg = "#a4de02")
    canvas1.create_window(400, 680, window=output10)

    word_count = len(composition.split())
    neuro_word_count = str(word_count)
    output11 = tk.Label(root, text= 'Word Count : ' + neuro_word_count ,font=('helvetica', 10), bg = "#a4de02")
    canvas1.create_window(400, 700, window=output11)

    reading_time = (60/256) * word_count
    neuro_reading_time = str(reading_time)
    output12 = tk.Label(root, text= 'Average Reading Time : ' + neuro_reading_time + ' seconds' ,font=('helvetica', 10), bg = "#a4de02")
    canvas1.create_window(400, 720, window=output12)

# =============================================================================
# Using Button to call the getneurograde function when clicked
# =============================================================================
button1 = tk.Button(text='Get Neuro Grade', command=getneurograde, bg='black', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(400, 400, window=button1)

# =============================================================================
# Using mainloop() since it is an infinite loop used to run the application, wait for an event to # occur and process the event as long as the window is not closed.
# =============================================================================

root.mainloop()
