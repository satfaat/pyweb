from fapp import app

print('We start off in:', __name__)
if __name__ == '__main__': # = app or __main__
    app.run(debug=True)
    print('We end up in:', __name__)