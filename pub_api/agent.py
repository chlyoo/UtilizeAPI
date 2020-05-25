from . import contexts

from evsim.system_simulator import SystemSimulator
from evsim.behavior_model_executor import BehaviorModelExecutor
from evsim.system_message import SysMessage
from evsim.definition import *

from .config import *
from .instance.config import *

from .crawler import Crawler
def agent_initiate():
    se = SystemSimulator()
    se.register_engine("sname", SIMULATION_MODE)

    a = Crawler(0, Infinite, "Peter", "sname")

    se.get_engine("sname").insert_input_port("start")
    se.get_engine("sname").insert_input_port("report")
    se.get_engine("sname").register_entity(a)

    se.get_engine("sname").coupling_relation(None, "report", a, "report")
    se.get_engine("sname").insert_external_event("report", None)
    se.get_engine("sname").simulate()


