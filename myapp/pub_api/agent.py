from . import contexts
from celery import Celery
from evsim.system_simulator import SystemSimulator
from evsim.behavior_model_executor import BehaviorModelExecutor
from evsim.system_message import SysMessage
from evsim.definition import *

from .config import *
from .instance.config import *

from .crawler import Crawler
from .eval import Eval

#mail
from celery import Celery
from flask import Flask,render_template
from flask_mail import Mail, Message
from instance.config import *

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('instance/config.py')
mail = Mail(app)
celery = Celery(app.import_name ,broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


se = SystemSimulator()

@celery.task
def agent_initiate():
	se.register_engine("sname", SIMULATION_MODE)

	a = Crawler(0, Infinite, "Peter", "sname")
	b = Eval(0, Infinite, "Simon", "sname")

	se.get_engine("sname").insert_input_port("report")
	se.get_engine("sname").register_entity(a)
	se.get_engine("sname").register_entity(b)
	se.get_engine("sname").coupling_relation(None, "report", a, "report")
	se.get_engine("sname").coupling_relation(a, "alert", b, "alert")
	se.get_engine("sname").insert_external_event("report", None)
	se.get_engine("sname").simulate()


