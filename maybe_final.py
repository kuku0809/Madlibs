from tkinter import *
root=Tk()
root.title('Mad Libs Generator')
root.attributes('-fullscreen', True)     #setting window size to full screen
root.configure(bg='lightblue')
s1='Welcome to Mad Libs!!!\nHere you create your own stories and have a laugh while you\'re at it!'
label1=Label(root,text=s1,font=('Times',30),bg='lightblue')
label1.place(relx = 0.5,rely = 0.4,anchor = 'center')
s2='Books'
s3='Education'
s4='General'
s7='Movies'
s5='Song'
s6='Sports/News'
#clicking sound
from playsound import playsound
def play():
    playsound('click sound.wav')
ch=0
def open_nw_8():
    import pyttsx3
    def voiceChange_male():
        eng = pyttsx3.init()
        voice = eng.getProperty('voices')
        eng.setProperty('voice', voice[0].id)  # changing voice to index 1 for female voice
        eng.say(s)
        eng.runAndWait()
    def voiceChange_female():
        eng = pyttsx3.init()
        voice = eng.getProperty('voices')
        eng.setProperty('voice', voice[1].id)  # changing voice to index 1 for female voice
        eng.say(s)
        eng.runAndWait()
    top5=Toplevel(root)
    top5.geometry('750x500')
    top5.configure(bg='lightblue')
    Label(top5,text='Choose one voice',font=('Times',25),bg='lightblue').place(relx=0.5,rely=0.3,anchor='center')
    Button(top5,text='Male',command=lambda:[play(),voiceChange_male()],font=('Times',20)).place(relx=0.5,rely=0.5,anchor='center')
    Button(top5, text='Female', command=lambda:[play(),voiceChange_female()],font=('Times',20)).place(relx=0.5,rely=0.7,anchor='center')
def prog():
    global s
    import random
    bl = ['book_1.txt', 'book_2.txt', 'book_3.txt', 'book_4.txt']
    el = ['education_1.txt', 'education_2.txt', 'education_3.txt', 'education_4.txt']
    ml = ['movie_1.txt','movie_2.txt','movie_3.txt','movie_4.txt']
    gl = ['general_1.txt', 'general_2.txt', 'general_3.txt', 'general_4.txt']
    sl = ['song_1.txt', 'song_2.txt', 'song_3.txt', 'song_4.txt']
    spl = ['sports_1.txt', 'sports_2.txt', 'news_1.txt', 'news_2.txt']
    while True:
        if ch == '1':
            a = random.choice(bl)
            break
        elif ch == '2':
            a = random.choice(el)
            break
        elif ch == '3':
            a = random.choice(gl)
            break
        elif ch == '4':
            a = random.choice(sl)
            break
        elif ch == '5':
            a = random.choice(spl)
            break
        elif ch=='6':
            a=random.choice(ml)
        else:
            print('Enter valid choice')
    f = open(a, 'r')
    s = f.read()
    c_num=0
    c_nn=0
    c_adj=0
    c_vb=0
    c_animal=0
    c_unit_of_measurement=0
    c_liquid_type=0
    c_rel=0
    c_name=0
    c_plural_noun=0
    c_adverb=0
    c_year=0
    c_exclamation=0
    c_pnn=0
    c_fav_food=0
    c_position=0
    c_date=0
    c_restaurant_name=0
    c_month=0
    c_clothing_brand=0
    c_plural_pronoun=0
    c_colour=0
    c_mode_of_transport=0
    c_type_of_room=0
    c_profession=0
    c_past_verb=0
    c_location=0
    c_ing_verb=0
    c_body_part=0
    c_plural_body_pt=0
    c_weird_nm=0
    lt = s.split()
    #function for finding count
    def fun2(string, c1):
        for i in lt:
            if string in i:
                c1 += 1
        return c1
    c_num = fun2('num_', c_num)
    c_exclamation = fun2('exclamation_', c_exclamation)
    c_pnn = fun2('pnn_', c_pnn)
    c_fav_food = fun2('fav_food_', c_fav_food)
    c_date = fun2('date_', c_date)
    c_position = fun2('position_', c_position)
    c_restaurant_name = fun2('restaurant_nm_', c_restaurant_name)
    c_month = fun2('month_', c_month)
    c_clothing_brand = fun2('clothing_brand_', c_clothing_brand)
    c_plural_pronoun = fun2('plural_pronoun_', c_plural_pronoun)
    c_colour = fun2('colour_', c_colour)
    c_year = fun2('year_', c_year)
    c_mode_of_transport = fun2('mode_of_transport_', c_mode_of_transport)
    c_type_of_room = fun2('type_of_room_', c_type_of_room)
    c_profession = fun2('profession_', c_profession)
    c_weird_nm = fun2('weird_nm_', c_weird_nm)
    c_ing_verb = fun2('ing_verb', c_ing_verb)
    c_body_part = fun2('body_part_', c_body_part)
    c_plural_body_pt = fun2('plural_body_pt_', c_plural_body_pt)
    c_past_verb = fun2('past_verb_', c_past_verb)
    c_plural_noun = fun2('plural_noun_', c_plural_noun)
    c_adverb = fun2('adverb_', c_adverb)
    c_nn = fun2('nn_', c_nn)
    c_adj = fun2('adj_', c_adj)
    c_rel = fun2('rel_', c_rel)
    c_name = fun2('name_', c_name)
    c_location = fun2('location_', c_location)
    c_vb = fun2('vb_', c_vb)
    c_animal = fun2('animal_', c_animal)
    c_unit_of_measurement = fun2('unit_of_measurement_', c_unit_of_measurement)
    c_liquid_type = fun2('liquid_type_', c_liquid_type)
    l_num = []
    l_noun = []
    l_adj = []
    l_verb = []
    l_animal = []
    l_unit_of_measurement = []
    l_liquid_type = []
    l_rel = []
    l_plural_noun = []
    l_adverb = []
    l_past_verb = []
    l_name = []
    l_fav_food = []
    l_position = []
    l_date = []
    l_restaurant_name = []
    l_month = []
    l_clothing_brand = []
    l_year = []
    l_mode_of_transport = []
    l_type_of_room = []
    l_profession = []
    l_location = []
    l_ing_verb = []
    l_weird_name = []
    l_body_part = []
    l_plural_body_part = []
    l_exclamation = []
    l_pronoun = []
    l_plural_pronoun = []
    l_colour = []
    #function for inputting corresponding values
    def fun1(c, st, l):
        if c == 0:
            pass
        else:
            print('Enter', c, st + '(s)')
            for i in range(c):
                l.append(input())
    fun1(c_num, 'number', l_num)
    fun1(c_nn, 'noun', l_noun)
    fun1(c_adj, 'adjective', l_adj)
    fun1(c_vb, 'verb', l_verb)
    fun1(c_fav_food, 'favourite food', l_fav_food)
    fun1(c_date, 'date', l_date)
    fun1(c_position, 'position', l_position)
    fun1(c_restaurant_name, 'restaurant name', l_restaurant_name)
    fun1(c_month, 'month', l_month)
    fun1(c_clothing_brand, 'clothing brand', l_clothing_brand)
    fun1(c_animal, 'animal', l_animal)
    fun1(c_unit_of_measurement, 'unit of measurement', l_unit_of_measurement)
    fun1(c_liquid_type, 'type of liquid', l_liquid_type)
    fun1(c_rel, 'relative', l_rel)
    fun1(c_name, 'name', l_name)
    fun1(c_plural_noun, 'plural noun', l_plural_noun)
    fun1(c_adverb, 'adverb', l_adverb)
    fun1(c_year, 'year', l_year)
    fun1(c_exclamation, 'exclamation', l_exclamation)
    fun1(c_pnn, 'pronoun', l_pronoun)
    fun1(c_plural_pronoun, 'plural pronoun', l_plural_pronoun)
    fun1(c_colour, 'colour', l_colour)
    fun1(c_mode_of_transport, 'transport mode', l_mode_of_transport)
    fun1(c_type_of_room, 'room type', l_type_of_room)
    fun1(c_profession, 'profession', l_profession)
    fun1(c_past_verb, 'past verb', l_past_verb)
    fun1(c_location, 'location', l_location)
    fun1(c_ing_verb, 'ing verb', l_ing_verb)
    fun1(c_body_part, 'body part', l_body_part)
    fun1(c_plural_body_pt, 'plural body part', l_plural_body_part)
    fun1(c_weird_nm, 'weird name', l_weird_name)
    import random
    #function for opening a file and replacing with inputs
    def func3(st, l):
        global s
        for i in lt:
            if st in i:
                random.shuffle(l)
                a = l.pop()
                s = s.replace(i, a)
    func3('num_', l_num)
    func3('ing_verb_', l_ing_verb)
    func3('body_part_', l_body_part)
    func3('plural_body_pt', l_plural_body_part)
    func3('plural_pronoun_', l_plural_pronoun)
    func3('exclamation_', l_exclamation)
    func3('pnn_', l_pronoun)
    func3('colour_', l_colour)
    func3('past_verb_', l_past_verb)
    func3('nn_', l_noun)
    func3('year_', l_year)
    func3('mode_of transport_', l_mode_of_transport)
    func3('type_of_room', l_type_of_room)
    func3('profession_', l_profession)
    func3('adj_', l_adj)
    func3('weird_nm_', l_weird_name)
    func3('plural_noun_', l_plural_noun)
    func3('adverb_', l_adverb)
    func3('rel_', l_rel)
    func3('name_', l_name)
    func3('location_', l_location)
    func3('vb_', l_verb)
    func3('animal_', l_animal)
    func3('unit_of_measurement_', l_unit_of_measurement)
    func3('liquid_type_', l_liquid_type)
    func3('fav_food', l_fav_food)
    func3('clothing_brand_', l_clothing_brand)
    func3('date_', l_date)
    func3('position_', l_position)
    func3('restaurant_name', l_restaurant_name)
    func3('month_', l_month)
    while True:
        a = input('Press enter to view your madlib')
        if a=='':
            top4 = Toplevel(root)
            top4.geometry('1250x500')
            top4.configure(bg='lightblue')
            Label(top4, text=s,font=('Times',18),bg='lightblue').place(relx=0.5,rely=0.4,anchor='center')
            Label(top4,text='Do you want to listen to it?',font=('Times',20),bg='lightblue').place(relx=0.5,rely=0.8,anchor='center')
            Button(top4,text='Click here',command=lambda:[open_nw_8(),play()],font=('Times',20)).place(relx=0.5,rely=0.9,anchor='center')
            def quit_msg():
                frame1 = Frame(top4, highlightbackground="black", highlightcolor="black", highlightthickness=1, bd=0)
                frame1.pack()
                top4.overrideredirect(1)
                top4.geometry("1250x500")
                lbl = Label(frame1, text="Are you sure you want to quit")
                lbl.pack()
                yes_btn = Button(frame1, text="Yes", bg="light blue", fg="black", command=lambda:[play(),root.destroy()], width=10)
                yes_btn.pack(padx=10, pady=10, side=LEFT)

                def goBack():
                    frame1.destroy()
                no_btn = Button(frame1, text="No", bg="light blue", fg="black", command=lambda:[play(),goBack()],width=10)
                no_btn.pack(padx=10, pady=10, side=LEFT)
                top4.mainloop()

            e1=Button(top4, text="EXIT ", font=("Times", 14), command=lambda:[play(),quit_msg()]).place(relx=0.5,rely=0.979,anchor='center')
            break
        else:
            print('Invalid input')
def open_nw_2():
    global ch
    top2=Toplevel(root)
    top2.geometry('750x500')
    top2.configure(bg='lightblue')
    Label(top2,text="Are You Ready?",font=('Times',25),bg='lightblue').place(relx=0.5,rely=0.3,anchor='center')       
    Button(top2,text='Click me!',command=lambda:[play(),prog()], font=('Times',25)).place(relx=0.5,rely=0.5,anchor='center')  
    ch='1'
def open_nw_3():
    global ch
    top2=Toplevel(root)
    top2.geometry('750x500')
    top2.configure(bg='lightblue')
    Label(top2,text="Are You Ready?",font=('Times',25),bg='lightblue').place(relx=0.5,rely=0.3,anchor='center')       
    Button(top2,text='Click me!',command=lambda:[play(),prog()], font=('Times',25)).place(relx=0.5,rely=0.5,anchor='center')
    ch='2'
def open_nw_4():
    global ch
    top2=Toplevel(root)
    top2.geometry('750x500')
    top2.configure(bg='lightblue')
    Label(top2,text="Are You Ready?",font=('Times',25),bg='lightblue').place(relx=0.5,rely=0.3,anchor='center')       
    Button(top2,text='Click me!',command=lambda:[play(),prog()], font=('Times',25)).place(relx=0.5,rely=0.5,anchor='center')
    ch='3'
def open_nw_5():
    global ch
    top2=Toplevel(root)
    top2.geometry('750x500')
    top2.configure(bg='lightblue')
    Label(top2,text="Are You Ready?",font=('Times',25),bg='lightblue').place(relx=0.5,rely=0.3,anchor='center')       
    Button(top2,text='Click me!',command=lambda:[play(),prog()], font=('Times',25)).place(relx=0.5,rely=0.5,anchor='center')
    ch='4'
def open_nw_6():
    global ch
    top2=Toplevel(root)
    top2.geometry('750x500')
    top2.configure(bg='lightblue')
    Label(top2,text="Are You Ready?",font=('Times',25),bg='lightblue').place(relx=0.5,rely=0.3,anchor='center')       
    Button(top2,text='Click me!',command=lambda:[play(),prog()], font=('Times',25)).place(relx=0.5,rely=0.5,anchor='center')
    ch='5'
def open_nw_7():
    global ch
    top2=Toplevel(root)
    top2.geometry('750x500')
    top2.configure(bg='lightblue')
    Label(top2,text="Are You Ready?",font=('Times',25),bg='lightblue').place(relx=0.5,rely=0.3,anchor='center')       
    Button(top2,text='Click me!',command=lambda:[play(),prog()], font=('Times',25)).place(relx=0.5,rely=0.5,anchor='center')
    ch = '6'
def open_nw_1():
    top1=Toplevel(root)
    top1.geometry('750x500')
    top1.configure(bg='lightblue')
    Label(top1,text="Here are some of the themes available",font=('Times',25),bg='lightblue').place(relx=0.5,rely=0.1,anchor='center')
    b1=Button(top1,text=s2,command=lambda:[open_nw_2(),play()],font=('Times',25))
    b1.place(relx=0.2,rely=0.3,anchor='center')
    b2=Button(top1, text=s3, command=lambda:[open_nw_3(),play()],font=('Times',25))
    b2.place(relx=0.2, rely=0.8, anchor='center')
    b3=Button(top1, text=s4, command=lambda:[open_nw_4(),play()],font=('Times',25))
    b3.place(relx=0.5, rely=0.3, anchor='center')
    b4=Button(top1, text=s5, command=lambda:[open_nw_5(),play()],font=('Times',25))
    b4.place(relx=0.5, rely=0.8, anchor='center')
    b5=Button(top1, text=s6, command=lambda:[open_nw_6(),play()],font=('Times',25))
    b5.place(relx=0.8, rely=0.3, anchor='center')
    b5 = Button(top1, text=s7, command=lambda:[open_nw_7(),play()],font=('Times',25))
    b5.place(relx=0.8, rely=0.8, anchor='center')
button1=Button(root,text='Start',command=lambda:[open_nw_1(),play()],font=('Times',30))
button1.place(relx=0.5,rely=0.6,anchor='center')
#exit_button = Button(root, text="Exit", command=root.destroy).place(relx=0.5,rely=0.979,anchor='center')
root.mainloop()