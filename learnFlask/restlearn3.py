from flask import Flask, jsonify, redirect, url_for, request, render_template
import os
import requests
from werkzeug.utils import secure_filename
import uuid
import threading
import sys
import helper #file class
from workerThread import workerThread # different file class


app = Flask(__name__)

@app.route('/upload')
def upload():
    return render_template('page3.html')

@app.route('/uploader',methods = ['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f= request.files['file']
        f.save(secure_filename(f.filename))
    requestID = uuid.uuid1()
    helper.map1 = {requestID:(os.getcwd()+"/"+f.filename)}
    helper.map2 = {requestID:0}
    t1 = workerThread(requestID)
    t1.run()
    return requestID

@app.route('/process',methods=['GET'])
def process():
    act = request.args.get('action')
    #check this valid or not
    import helper as h
    requestId = request.args.get('requestId')
    if act == 'stop':
        h.helper().stop_request(requestId)
        return 'request has stop'
    elif act == 'resume':
        h.helper().resume_request(requestId)
        return 'is resumed'
    elif act == 'terminate':
        h.helper().remove_request(requestId)
        return 'is terminated'
    else:
        return 'invalid actions'

if __name__ == '__main__':
    app.run(debug = True)







# @app.route('/process', methods=['GET','POST'])
# def processFile():
#     if request.method == 'GET':
#         action = request.args.get('action')
#         if action == 'stop':
#             return "stop"   
#         elif action == 'resume':
#             return "resume"
#         elif action == 'terminate':
#             return "terminate"   
           
                     

# thread1 = myThread(1, "Thread-1" , 1)

# thread1.start()

print("exiting main thread") 





# class myThread(threading.Thread):

#     def __init__(self):
#         ...
#         self.can_run = threading.Event()
#         self.thing_done = threading.Event()
#         self.thing_done.set()
#         self.can_run.set()    

#     def run(self):
#         while True:
#             self.can_run.wait()
#             try:
#                 self.thing_done.clear()
#                 uploadFile(myThread())
#             finally:
#                 self.thing_done.set()

#     def pause(self):
#         self.can_run.clear()
#         self.thing_done.wait()

#     def resume(self):
#         self.can_run.set()
    
#     def terminate(self):
#         sys.exit()

# class workerThread(threading.Thread):
#     def __init__(self, requestId):
#     threading.Thread.__init__(self)
#         self.requestId = requestId
        

#     def run(self):
#         while True:
#             self.can_run.wait()
#             try:
#                 self.thing_done.clear()
#                 uploadFile(myThread())
#             finally:
#                 self.thing_done.set()

#     def pause(self):
#         self.can_run.clear()
#         self.thing_done.wait()

#     def resume(self):
#         self.can_run.set()
    
#     def terminate(self):
#         sys.exit()




# def uploadFile(t1):
#         with open(f.filename) as d:    
#             re = reader(d)
#             for row in re:
#                 print(row)
#                 t1.pause()
#                 time.sleep(1)
#                 t1.resume()
#                 time.sleep(1)
                
#     return "done"













# requestId = uuid.uuid1()
# counter = 0

# map1 = {requestId:filePath}
# map2 = {requestId:counter}
# set = ()

# class FileLoader(threading.Thread):
#     def __init__(self, requestId, counter, name):
#         threading.Thread.__init__(self)
#         self.requestId = requestId
#         self.counter = counter
#         self.name = name
#         # threading.Thread().name = "abc"
        
#     def run(self):
#         try:
#             while True:
#                 if self.requestId in map1.keys():
#                     filePath = map1[requestId]
#                     if requestId in map2.keys():
#                         self.counter = map2[requestId]
#                     cnt = 0
#                     with open(filePath) as newFile:
#                         readIt = reader(newFile)
#                         for row in readIt:
#                             cnt = cnt+1
#                             print(row)
#                     if(isRequestIdStopped(requestId)):
#                         self.raise_exception()
#         finally:
#             pass          

#     def get_id(self):
#         if hasattr(self, '_thread_id'):
#             return self._thread_id
#         for id, thread in threading._active.items():
#             if thread is self:
#                 return id
    
#     def raise_exception(self):
#         thread_id = self.get_id()
#         res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,ctypes.py_object(SystemExit))
#         if res > 1:
#             ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
#             print('Exception raise failure')

        
# @app.route('/data')
# def upload_file():
#     return render_template('page3.html')





# if __name__ == "__main__":
#     main()






# # def send_data_to_server(image_path):
# #     image_filename = os.path.basename(image_path)

# #     multipart_from_data = {
# #         'file':(image_filename, open(image_filename,'r'))
# #     }
# #     response = request.post('/upload/',file = multipart_from_data['file'])
# #     return response.status_code
# url = 'http:127'
# def file_upload(fil):
#     files = {'file':open(fil,'rb')}
#     response = request.post(files = files)
#     return response.status_code
