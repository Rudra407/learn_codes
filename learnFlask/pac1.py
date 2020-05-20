from flask import Flask, request

app = Flask(__name__)




@app.route('/upload/<int:i>')
def upload(i):
    while(i<10000000000000):
        print(i)
        i=i+1
    return "done"



@app.route('/process/')
def process():
    print(request.args.get('requestId'))
    act = request.args.get('action')
    if act == 'stop':
        print(act)
        return 'stop'
    elif act == 'resume':
        return 'resume'
    elif act == 'terminate':
        return 'terminate'
            
if __name__ == "__main__":
    app.run(debug=True)


