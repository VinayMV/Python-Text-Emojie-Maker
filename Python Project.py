import nltk
from nltk.corpus import wordnet
import turtle

def smiley(s,h):#To diplay smiley in turtle window
        hsm=turtle.Turtle()
        hsm.hideturtle()
        hsm.up()
        hsm.goto(0,-100)  
        hsm.down()
        hsm.begin_fill()
        hsm.fillcolor("yellow")
        hsm.circle(100)
        hsm.end_fill()
        hsm.up()
        if s==h:#to draw neutral smiley
            hsm.goto(50, -60)
            hsm.setheading(-60)
            hsm.width(5)
            hsm.down()
            hsm.goto(-45, -60)
            hsm.fillcolor("black")
        else:
            if s>h:#to draw sad smiley
                hsm.goto(50, -60)
                hsm.setheading(-60)
                hsm.width(5)
                hsm.down()
                hsm.circle(-60,-120)
                hsm.fillcolor("black")
            elif s<h:#to draw happy smiley
                hsm.goto(-60,-40)
                hsm.setheading(-60)
                hsm.width(5)
                hsm.down()
                hsm.circle(70,120)
                hsm.fillcolor("black")
        for i in range(-35, 105, 70):
                hsm.up()
                hsm.goto(i, 35)
                hsm.setheading(0)
                hsm.down()
                hsm.begin_fill()
                hsm.circle(10)   
                hsm.end_fill()
        hsm.bye()

def check(f,s3=[],h3=[],b3=[],g3=[]):#to check whether a word is in the given passage
    sb=0
    gh=0
    
    for t in f.read().split():
        for i in s3:
            if(t==i):
                sb=sb+1
        for j in h3:
            if(t==j):
                gh=gh+1
        for k in b3:
            if(t==k):
                sb=sb+1
        for l in g3:
            if(t==j):
                gh=gh+1
    smiley(sb,gh)

def dupchk(s,s2):#to check if there are any duplicates in the double found out synonyms of words
    s3=[]
    for i in s:
        if i not in s3:
            s3.append(i)
    for j in s2:
       if j not in s3:
           s3.append(j)
    return s3

def counts2(s):#to find double synonyms of words and append to a list
    s2=[]
    for i in s:
        for j in wordnet.synsets(i):
            for n in j.lemma_names():
                s2.append(n)
    return s2

def counts1(w):#to find synonyms of words and to count it
    s=[]
    for syn in wordnet.synsets(w):
        for name in syn.lemma_names():
            s.append(name)
    s2=counts2(s)
    s3=dupchk(s,s2)
    return s3

print("*********************** EMOTION CREATOR OF A TEXT FILE***********************")
ch='y'
while(ch=='y' or ch=='Y'):
    try:
                name=input("Enter the filename(only .txt files with complete extension):")
                print("Please look at the turtle shell running in the background")
                f=open(name,'r')
                sl=counts1("sad")
                hl=counts1("happy")
                bl=counts1("bad")
                gl=counts1("good")
                check(f,sl,hl,bl,gl)
                ch=input("Do yo want to continue(Y/N):")
    except LookupError:
                print("Error occurred while entering the path of the file or text document!!!")
                ch=input("Do yo want to continue(Y/N):")
    except:
            print("Error Occured")
            ch=input("Do yo want to continue(Y/N):")
print ("Thanks for using \n\t\t\EMOTION CREATOR....\n\t\t\t\tKeep using it ... :)")
