from chatbot import ChatBot
myChatBot = ChatBot()
#apenas carregar um modelo pronto
myChatBot.loadModel()

#criar o modelo
#myChatBot.createModel()

print("\n \n === Bem vindo ao Chatbot === \n")

pergunta = input("[bot] Como posso te ajudar? :) \n")
tamanho=len(myChatBot.chatbot_response(pergunta))
if tamanho > 2:
    resposta, intencao, sugestao,intecao_sug = myChatBot.chatbot_response(pergunta)
    print(resposta + "   ["+intencao[0]['intent']+"] \n")
    print("[bot] Deixe-me sugerir um tópico \n")
    print(sugestao + "   ["+intecao_sug[0]['intent']+"] \n")
else:
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta + "   ["+intencao[0]['intent']+"]")


while (intencao[0]['intent']!="despedida"):
    pergunta = input("[bot] Posso lhe ajudar com algo mais?")
    tamanho=len(myChatBot.chatbot_response(pergunta))
    if tamanho > 2:
        resposta, intencao, sugestao,intecao_sug = myChatBot.chatbot_response(pergunta)
        print(resposta + "   ["+intencao[0]['intent']+"] \n")
        print("[bot] Deixe-me sugerir um tópico \n")
        print(sugestao + "   ["+intecao_sug[0]['intent']+"] \n")
    else:
        resposta, intencao = myChatBot.chatbot_response(pergunta)
        print(resposta + "   ["+intencao[0]['intent']+"]")



print("[bot] Foi um prazer atendê-lo!")
