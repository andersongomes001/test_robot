# coding: iso-8859-1 -*-
import aiml
import os

"""
pip install python-aiml
pip install --upgrade google-api-python-client
"""

os.chdir('./') # diret�rio que cont�m os arquivos da AIML standard
ai = aiml.Kernel() # inicializa��o
ai.learn('std-startup.xml') # l� o arquivo principal da AIML e faz refer�ncias aos outros
ai.respond('load aiml b') # faz com que os outros arquivos da AIML sejam carregados

while True:
    frase = input('Oi o que voce desaja me perguntar: ')

    try:
        resposta = ai.respond(frase)
    except Exception:
        resposta = "n�o sei isso ainda"

    print("{}\n".format(resposta))
