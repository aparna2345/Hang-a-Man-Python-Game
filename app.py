from flask import Flask, render_template, request, Response, session, redirect, url_for
import random
app = Flask(__name__)
app.secret_key = 'test'

def print_line(completed_array):
    line = ''
    for letter in completed_array:
        line = line + letter + ' '
    return line

array = ["orange","pineapple","grapes","sappota","apricot",
"avocado","bilberry","lychee","cranberry","jujube","plumcoat",
"gooseberry","squash","cat","dog","lion","goat","gray","rhinoceros","crocodile","hyena",
"crane","parrot","penguine","lovebird","bike","car","bus"]

hints = ["it is a fruit","it is a fruit","it is a fruit","it is a fruit","it is a fruit",
"it is a fruit","it is a fruit","it is a fruit","it is a fruit","it is a fruit","it is a fruit"
,"it is a fruit","it is a fruit","it is a animal","it is a animal","it is a animal","it is a animal",
"it is a animal","it is a animal","it is a animal","it is a animal","it is a bird","it is a bird","it is a bird",
 "it is a bird","it is a automobile","it is a automobile","it is a automobile"]


@app.route('/')
def root():
    session['selected'] = random.choice(array)
    life = 9
    session['life'] = life
    i = 0
    completed_array = []
    while i < len(session['selected']):
        completed_array.append('-')
        i = i + 1
    session['completed_array'] = completed_array
    hint = hints[array.index(session['selected'])]
    return render_template('game.html', completed_array = print_line(completed_array), life = life, hint = hint)


@app.route('/submit',methods = ['POST'])
def submit():
   letter = request.form['letter']
   life = session['life']
   selected = session['selected']
   selected_array = list(selected)
   completed_array = session['completed_array']
   position = array.index(selected)
   hint = hints[position]
   i = 0
   flag = 0
   for l in selected_array:
       if l == letter:
           completed_array[i] = l
           flag = 1
       i = i + 1
   if flag == 0:
       life = life - 1
   if life == 0:
       return render_template('result.html', result = selected )
   if '-' not in completed_array:
       return render_template('won.html', result = selected )

   session['life'] = life
   session['completed_array'] = completed_array
   return render_template('game.html', completed_array = print_line(completed_array), life = life, hint = hint)


if __name__ == '__main__':
    app.run(debug = True)
