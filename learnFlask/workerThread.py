import threading
import helper
import sys
from csv import reader
from time import sleep

class workerThread(threading.Thread):
    def __init__(self, requestId):
        super(workerThread, self).__init__()
        self.requestId = requestId
        
    def uploadFile(self):
        if helper.helper().rid_filepath_dict.get(self.requestId) != None:
            if helper.helper().rid_counter_dict.get(self.requestId) != None:
                filename = helper.helper().rid_filepath_dict[self.requestId]
                counter = helper.helper().rid_counter_dict[self.requestId]
                count = 0
                try:
                    with open(filename) as fileContent:    
                        readItr = reader(fileContent)
                        for row in readItr:
                            count+=1
                            if count > counter:
                                print(row)
                                sleep(3)
                                if(helper.helper().isRequestIdStopped(self.requestId)):
                                    print("stopping the process")
                                    helper.helper().rid_counter_dict.update({self.requestId:count})   
                                    sys.exit()      
                                if(helper.helper().isRequestIdTerminated(self.requestId)):
                                    print("terminating the process")
                                    sys.exit()
                        return "done"
                except Exception as e:
                    return str(e)

    def run(self):
        self.uploadFile()
