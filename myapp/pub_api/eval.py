from evsim.system_simulator import SystemSimulator
from evsim.behavior_model_executor import BehaviorModelExecutor
from evsim.system_message import SysMessage
from evsim.definition import *

import os
import subprocess as sp
import datetime
from pathlib import Path 
from subprocess import STDOUT, check_output, TimeoutExpired

#mail
import e_mail

class Eval(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)
        self.init_state("IDLE")
        self.insert_state("IDLE", Infinite)
        self.insert_input_port("alert")
        self.values=[]
    def ext_trans(self,port, msg):
        if port == "alert":
           self._cur_state = "PROCESS"
           self.values = msg.retrieve()[0]

    def output(self):
        if self._cur_state == "PROCESS":
            e_mail.send_async_email.delay("peterscience@naver.com", "Current Air Stat", "email/inform", list=self.values)
        else:
            print("Error Code:" + rescode)
        return None
    def int_trans(self):
        if self._cur_state == "PROCESS":
            self._cur_state = "IDLE"