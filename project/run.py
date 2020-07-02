from flask import Flask

app = Flask (__name__)

@app.route("/<name>", methods=['GET','POST'])
def ola(name):
    return 'Hello World {} !'.format(name)

if __name__ == "__main__":
    app.run(debug=True)