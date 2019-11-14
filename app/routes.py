from app import app

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/football_data')
def football_data():
    x = "go seahawks"
    return x

