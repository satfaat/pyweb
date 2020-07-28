
from flask import Flask, render_template, request, escape #redirect
from vsearch import search4letters
from decodurl import encodurl, decodurl
from datetime import datetime
#import urllib.parse

app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        #print(str(dir(req)), res, file=log)
        #print(req.form, file=log, end='|')
        #print(req.remote_addr, file=log, end='|')
        #print(req.user_agent, file=log, end='|')
        #print(res, file=log)
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

@app.route('/search4', methods=['POST']) # methods=['GET', 'POST']
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)

@app.route('/encod', methods=['POST'])
def encod() -> 'html':
    decod=''
    encod=''
    txt = request.form['txt']
    #encod = request.form['encod']
    if txt != '':
        results = decodurl(txt)
    #elif encod != '':
    #    results = encodurl(encod)
    else: 
        results = 'No input'
    return render_template('results.html', deencod_result=results)
    #return render_template('results1.html', the_decod=txt,
    #                                        the_encod=txt)

@app.route('/')
#def hello() -> '302':
#    return redirect('/entry')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')

# viewlog 

@app.route('/user/<name>') #/user/<int:id>
def user(name):
    user_agent = request.headers.get('User-Agent')
    txt1 = '<h1>Hello, %s!</h1>' % name
    txt2 = '<p>Your browser is %s</p>' % user_agent
    txt = txt1 + txt2
    return  txt

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.jade',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

print('We start off in:', __name__)
if __name__ == '__main__': # = app or __main__
    app.run(debug=True)
    print('We end up in:', __name__)
