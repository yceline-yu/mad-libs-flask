from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def home():
    """retuns the homepage with all the word inputs labeled"""
    form_prompts = silly_story.prompts

    return render_template("questions.html", prompts = form_prompts)

@app.route("/results")
def results():
    """returns resulting story with user inputs for placeholders"""
    user_story = silly_story.generate(request.args)
    return render_template("story.html", template_story=user_story)