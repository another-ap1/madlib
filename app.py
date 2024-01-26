from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = "CourageTheCowerdlyDog"
debug = DebugToolbarExtension(app)

@app.route('/')
def show_home():
    """
    Diplaying the home page where the user will put their inputs

    """
    prompts = story.prompts
    return render_template('home.html',  prompts=prompts)

@app.route('/home2')
def show_home2():
    """
    Diplaying the home page where the user will put their inputs

    """

    return render_template('home2.html')

@app.route('/home3')
def show_home3():
    """
    Diplaying the home page where the user will put their inputs

    """

    return render_template('home3.html')

@app.route('/story')
def show_story():
    """
    get all the inputs from the user and creates the madlib
    
    """
    
    text = story.generate(request.args)
    return render_template('story.html', text=text )
