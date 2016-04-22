from flask import Flask
from flask import render_template
import os
app = Flask(__name__)

def get_choice():
    # import the magic random picker
    import random, urllib2
    
    # list of things to pick from
    url_for_list = "https://raw.githubusercontent.com/bellcodo/laughing-meme/master/typing_options.lst"
    raw_typing_options = urllib2.urlopen(url_for_list)
    list_of_options = raw_typing_options.read()
    #print "DEBUG - raw typing options is %s, %s" % (raw_typing_options, list_of_options)
    typing_options = list_of_options.split()
    
    # find a way to pick something
    typing_choice = random.choice(typing_options)
    
    # a way to tell the user what to do
    todays_choice = """This is the typing program picker.
    It will pick a random typing_choice from a list.
    The list is kept here %s
    Todays typing choice is...
    
    %s
    """ % (url_for_list, typing_choice)
    return typing_choice

@app.route("/")
def hello():
    return get_choice()

@app.route('/activity_picker', methods=["GET"])
def show_entries():
    typing_url = get_choice()
    return render_template('show_entries.html', typing_url=typing_url)

if __name__ == "__main__":
    # go get the PORT from the environment
    port = os.environ.get("PORT")
    # run the app with the port and bind to any ip
    app.debug = True
    app.run(
      "0.0.0.0"
    , port
    )
