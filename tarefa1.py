from bottle import route, run, template, request

mensagens = [];

formEnvio = '''
		<style type='text/css'> .mt10 { margin-top: 10px } .div50 { display: table-cell; width: 50% } </style> 
		<div class='div50'>
			<form action="/chat" method="POST">
				<div class='mt10'>Seu nome:<br/><input type="text" name="nome" />
				</div>
				<div class='mt10'>Mensagem:<br/><input type="text" name="texto" />
				</div>
				<div class='mt10'><input type="submit" value="Enviar" /></div>
			</form>
		</div>
		'''

@route('/chat', method="GET")
def acesso():
	return formEnvio

@route('/chat', method="POST")
def write():

	try:
		
		nome = request.forms.get('nome')
		texto = request.forms.get('texto')
		msgs = ""
			
		if (nome == ""):
			nome = "anônimo"
		if (texto == ""):
			texto = "Nenhuma mensagem"

		mensagens.append("<b>" + nome + "</b> diz: <i>" +  texto + "</i>")
		
		
	except Exception as e:
		try:
			return str(e)
		except:
			return "Exceção não identificada"
	
	return formEnvio + "<div class='div50'><fieldset><legend>Histórico de mensagens</legend>" + "<br/>".join(mensagens) + "</fieldset></div>"
    
run(host='localhost', port=8080)