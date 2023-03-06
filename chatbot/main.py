from chatbot import ChatBot
myChatBot = ChatBot()
#apenas carregar um modelo pronto
#myChatBot.loadModel()

#criar o modelo
myChatBot.createModel()

print("Bem vindo ao Chatbot")

pergunta = input("como posso te ajudar?")
tamanho=len(myChatBot.chatbot_response(pergunta))
if tamanho > 2:
    resposta, intencao, sugestao,intecao_sug = myChatBot.chatbot_response(pergunta)
    print(resposta + "   ["+intencao[0]['intent']+"] \n")
    print("Deixe-me sugerir um tópico \n")
    print(sugestao + "   ["+intecao_sug[0]['intent']+"] \n")
else:
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta + "   ["+intencao[0]['intent']+"]")


while (intencao[0]['intent']!="despedida"):
    pergunta = input("posso lhe ajudar com algo a mais?")
    tamanho=len(myChatBot.chatbot_response(pergunta))
    if tamanho > 2:
        resposta, intencao, sugestao,intecao_sug = myChatBot.chatbot_response(pergunta)
        print(resposta + "   ["+intencao[0]['intent']+"] \n")
        print("Deixe-me sugerir um tópico \n")
        print(sugestao + "   ["+intecao_sug[0]['intent']+"] \n")
    else:
        resposta, intencao = myChatBot.chatbot_response(pergunta)
        print(resposta + "   ["+intencao[0]['intent']+"]")



print("Foi um prazer atendê-lo")
