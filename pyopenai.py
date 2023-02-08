#---------------------------------------------------------------------------------
#------------------------------- pyopenai ----------------------------------------
#---------------------------------------------------------------------------------

# ======= A biblioteca termcolor não está funcionando em sistemas Windows ========

from termcolor import colored
import sys
import os
import openai

openai.api_key = str(input('Digite aqui a sua chave api: '))


def start():

	if os.name == 'nt':
		os.popen('cls')
		str_user = os.popen('whoami').read()
		user = str_user.split("\\")[-1]

	elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
		os.system('clear')
		user = os.popen('whoami').read().strip()

	else:
		os.popen('clear')
		user = os.popen('whoami').read().strip()
	return user

def welcome():
	print('Olá %s!\n\nIsso é um programa que se comunica com a inteligência artificial do Elon Musk, isso mesmo, o chatGPT!' %user)
	print('\nÉ um programa simples, é mais fácil acessar o site oficial, mas se quiser acessá-la através de um terminal Linux ou pelo cmd do Windows esse script pode ajudar :)\n')
	print('Para encerrar o programa basta pressionar ctrl + c\n')

def gerador_de_texto(prompt):

        model_engine = "text-davinci-003"
        completions = openai.Completion.create(
                engine = model_engine,
                prompt = prompt,
                max_tokens = 500,
                n=1,
                temperature=0.5,
        )

        mensagem = completions.choices[0].text
        return mensagem

user = start()

welcome()

while True:
	try:
		message = str(input(colored('%s~$ ' %user, 'yellow')))

	except KeyboardInterrupt:
		print('\n\nAté mais! ;)\n')
		break
	resposta = gerador_de_texto(message)

	print(colored('\nchatGPT:', 'cyan') + resposta +'\n')
