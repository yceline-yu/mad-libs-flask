from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story
from stories import excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

STORIES = {
    "silly_story": silly_story,
    "excited_story": excited_story
}

@app.route("/")
def home():
    """retuns the homepage menu for story picking"""
    template_stories = ["silly_story", "excited_story"]

    return render_template("homepage.html", story_list = template_stories)

@app.route("/story/<story_temp>")
def picked_story(story_temp):
    """retuns the page with all the word inputs labeled"""
    form_prompts = STORIES[story_temp].prompts

    return render_template("questions.html", prompts = form_prompts)    

@app.route("/results")
def results():
    """returns resulting story with user inputs for placeholders"""
    user_story = silly_story.generate(request.args)
    return render_template("story.html", template_story=user_story)