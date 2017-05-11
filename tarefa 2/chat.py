from bottle import run, get, post, view, redirect, request
from datetime import datetime
import requests, bottle, json, threading, time, sys

mensagens = []
peers = sys.argv[2:]
print(peers)

@get('/')
@view('index')
def index():
    return {'mensagens': mensagens}

@get('/escrever_mensagem')
@view('escrever_mensagem')
def new():
	return;

@post('/enviar')
def newMessage():
	usuario = request.forms.get('usuario')
	mensagem = request.forms.get('mensagem')
	now = datetime.now()
	hora = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
	mensagens.append([usuario, mensagem, hora])
	redirect('/')

@get('/peers')
def index():
	return json.dumps(peers)

@get('/mensagens')
def index():
	return json.dumps(mensagens)

def clientePeers():
	time.sleep(50)
	while True:
		time.sleep(10)
		np = []
		for p in peers:
			r = requests.get(p + '/peers')
			np = np + json.loads(r.text)
		peers[:] = list(set(np + peers))
		print(peers)
		time.sleep(20)

def clienteMensagens():
	time.sleep(50)
	while True:
		nm = []
		for p in peers:
			m = requests.get(p + '/mensagens')
			nms = json.loads(m.text)
			for msg in nms:
					if msg not in mensagens:
						mensagens.append(msg)
	
		time.sleep(20)

th1 = threading.Thread(target=clientePeers)
th1.start()

th2 = threading.Thread(target=clienteMensagens)
th2.start()

run(host='localhost', port=int(sys.argv[1]))
