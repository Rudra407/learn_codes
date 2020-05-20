class helper(object):
    _instance = None
    rid_filepath_dict = {}
    rid_counter_dict = {}
    rid_set = set()
    def __new__(self):
        if not self._instance:
            self._instance = super(helper,self).__new__(self)
        return self._instance

    def isRequestIdStopped(self,requestID):
        
        if requestID in self.rid_set:
            return True
        else:
            return False

    def isRequestIdResumed(self, requestID):
        if requestID not in self.rid_set:
            return True
        else:
            return False
        
    def isRequestIdTerminated(self,requestID):
        if self.rid_filepath_dict.get(requestID) is None:
            return True
        else:
            return False

    def remove_request(self, requestID):
        del self.rid_filepath_dict[requestID]
        del self.rid_counter_dict[requestID]

    def stop_request(self, requestID):
        self.rid_set.add(requestID)
        
    def resume_request(self, requestID):
        self.rid_set.remove(requestID)
        