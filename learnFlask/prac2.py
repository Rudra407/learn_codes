import threading

class workerThread(threading.Thread):
    def __init__(self, requestId):
    threading.Thread.__init__(self)
        self.requestId = requestId
        

    def uploadFile():
        with open(f.filename) as d:    
            re = reader(d)
            for row in re:
                print(row)
                t1.pause()
                time.sleep(1)
                t1.resume()
                time.sleep(1)                
    return "done"


    def run(self):
        while True:
            self.can_run.wait()
            try:
                self.thing_done.clear()
                uploadFile(myThread())
            finally:
                self.thing_done.set()

    def pause(self):
        self.can_run.clear()
        self.thing_done.wait()

    def resume(self):
        self.can_run.set()
    
    def terminate(self):
        sys.exit()

