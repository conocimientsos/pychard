from flask import Flask, render_template

app = Flask(__name__)


@app.route('home')
def home ():
    return render_template('home.html',name='Flask',template_name='jinja2')

@app.route('/expressions/')
def JinJa2_Expressions():
    #Interpolation
    color='brown'
    animal_one='fox'
    animal_two='dog'
    #Addition and Subtraction
    orange_amount='10'
    apple_amount='50'
    donate_amount='60'
    #String Concatenation
    first_name='ironman'
    last_name ='hulk'

    #create dictionary

    dictionary={

                'color':color,
                'animal_one': animal_one,
                ' animal_two': animal_two,
                'orange_amount':orange_amount,
                'apple_amount':apple_amount,
                'donate_amount':donate_amount,
                'first_name':first_name,
                'last_name':last_name

    }

    return render_template('expressions.html',**dictionary)

 if __name__ == '__main__':
                app.run()
