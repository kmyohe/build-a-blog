from flask import Flask, render_template, request

def title(t):
    if int(len(t)) > 0:
        return('')
    else:
        return('Please enter a Title')

def author(a):
    if int(len(a)) > 0 :
        return('')
    else:
        return('Please enter your name')

def blog(b):
    if int(len(b)) > 0:
        return('')
    else:
        return('Please type your Blog')


def login(ti, au, bl):
    b_title = title(ti)
    b_author = author(au)
    b_blog = blog(bl)
    if (b_title == '') and (b_author == '') and (b_blog == ''):
        form = render_template("blog.html")
        return(2)
    else:
        form = render_template("new_blog.html")
        return(form.format(b_title, b_author, b_blog))
           
def main():
    UN = input("What is your username?")
    PW = input("What is your password?")
    VPW = input("Verify passwrd")
    EM = input("What is your email?(this is opptional)")
    print(login(UN, PW, VPW, EM))
    
    
if __name__ == "__main__":
    main()
    