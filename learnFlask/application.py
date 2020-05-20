import os
import uuid
import sys
import helper
from flask import Flask, request, render_template
from workerThread import workerThread
from werkzeug.utils import secure_filename

app = Flask(__name__)

#genreate requestID
requestId = uuid.uuid1().hex

#upload api to upload file to server
@app.route('/upload')
def upload():
    try:
        return render_template('upload.html')
    except Exception as e:
        return(str(e))
#uploader api triggered when user clicks upload button displayed in page3.html
@app.route('/uploader',methods = ['GET', 'POST'])
def uploader_file():
    try:
        if request.method == 'POST':
            fileObj = request.files['file']
            fileObj.save(secure_filename(fileObj.filename))
            helper.helper().rid_filepath_dict = {requestId:(os.getcwd()+"/"+fileObj.filename)}
            helper.helper().rid_counter_dict = {requestId:0}
            workerThreadObj = workerThread(requestId)
            workerThreadObj.start()
            return "uploaded and processId = %s" % requestId
    except Exception as e:
        return str(e)

#process api triggered when upload api hai completed its task to start, stop, terminate the process
@app.route('/process',methods=['GET'])
def process():
    action = request.args.get('action')
    requestID = request.args.get('requestId')
    if requestId != requestID:
        return "enter valid requestID"
    if action == 'stop':
        helper.helper().stop_request(requestId)
        return 'request has stop'
    elif action == 'resume':
        helper.helper().resume_request(requestId)
        workerThreadObj = workerThread(requestId)
        workerThreadObj.start()
        return 'is resumed'
    elif action == 'terminate':
        helper.helper().remove_request(requestId)
        return 'is terminated'
    else:
        return 'invalid actions'

if __name__ == '__main__':
    app.run(debug = True)
