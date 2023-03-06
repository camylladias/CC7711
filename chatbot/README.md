# ChatBot -> tcc
##### Disciplina Inteligência Artificial e Robótica - Ciência da Computação FEI

Atividade #1 – Chatbot 
Você foi designado para criar um chatbot que ajuda o professor de TCC I e para isso, o MVP deve auxiliar um usuário com suas dúvidas em relação aula de introdução da disciplina

## 1. Inicialização do código

Para evitar problemas de versionamento, dentro da pasta CC7711 rode:
``python -m venv venv``

Em seguida, entre na pasta  ``venv``, ``cd Scripts``, rode ``.\activate``, volte para a pasta raiz ``CC7711`` e entre na pasta ``chatbot``

Instale o Python 3 e os pacotes do arquivo *pacotes.txt*:

    pip install -r pacotes.txt
Inicie a interação com o chatbot:

    python main.py
    
Para treinar seu modelo, no arquivo main.py comente a linha myChatBot.loadModel() e descomente a linha myChatBot.createModel(), digite o comando: python main.py
e espere o treinamento finalizar.
Digite Ctrl+C para matar a execução do processo

Volte no arquivo main.py comente a linha myChatBot.createModel() e descomente a linha myChatBot.loadModel(), digite o comando: python main.py

## 2. Intenções
Arquivo *intents.json*:
``` {"intents":[
  { "tag": "saudacao",
    "patterns":["Ola","Opa","Oi", "tudo bem"],
    "responses": ["Oi","Ola", "Oie, espero que esteja bem!"]
  },
  { "tag": "despedida",
    "patterns":["valeu","tchau","Obrigado","tks"],
    "responses": ["Ate breve","Falou", "Tchauzinho!"]
  },
  { "tag": "introducao_tcc",
    "patterns":["Como eh um tcc?","Por que fazer o tcc?"],
    "responses": ["O TCC eh  uma avaliacao que acontece quando a graduacao esta chegando ao fim. Ele tem o objetivo de fazer com que o aluno coloque no papel tudo o que aprendeu até o momento, desde o inicio dos estudos. Assim, eh possivel saber se tudo foi absorvido e entendido corretamente."]
  },
  { "tag": "tema_tcc",
    "patterns":["Tema","Como escolher o tema?", "Tema ciencia da computacao"],
    "responses": ["O tema de uma monografia deve ser o mais especifico possivel, nao pode ser um assunto muito aberto. Um assunto unico e especifico possibilita um melhor aprofundamento e faz com que os leitores do TCC, principalmente a banca examinadora, criem as expectativas corretas, sabendo exatamente o que sera abordado na pesquisa."]
  },
  { "tag": "opcao_tema_tcc",
    "patterns":["Tema ciencia da computacao", "Opcoes de tema"],
    "responses": ["Criacao de ChatBot para avaliacao do estado mental dos funcionarios do Metro de SP", "Como podemos anonimizar automaticamente as imagens das pessoas em gravacoes de video", "Deteccao de fraudes em cartoes de credito com aprendizado de maquina", "Analise de sentimentos em redes sociais"]
  },
  { "tag": "integrantes_tcc",
  "patterns":["Grupo","Com quantas pessoas posso fazer tcc?", "Quantidade de integrantes", "Posso fazer grupo de um?", "Posso fazer grupo com pessoas de outro curso?", "Posso fazer sozinho?"],
  "responses": ["Eh recomendado o grupo de TCC ter 4 pessoas, mas pode-se fazer com menos pessoas, tendo em vista que ainda sera esperado um trabalho digno de quatro \n integrantes, ou mais pessoas, mas tendo mais pessoas sera esperado que o trabalho reflita essa diferenca. "]
  },
  { "tag": "banca_tcc",
  "patterns":["Quem avalia?","Quantos avaliadores?", "Como eh a banca?", "Banca"],
  "responses": ["Sao 3 avaliadores."]
  },
  { "tag": "orientador_tcc",
  "patterns":["Quem pode ser meu orientador?","Como escolho um orientador?", "Meu orientador pode ser de outro curso?"],
  "responses": ["Seu orientador pode ser qualquer professor da FEI de qualquer curso. E interessante que seja alguem com quem tenha uma boa relacao e em quem confie.\n Alem disso eh importante que a area de seu tema seja algo com que ele ou ela esteja familiarizado."]
  },
  { "tag": "funcao_orientador_tcc",
  "patterns":["Por que preciso de um orientador","Qual a funcao de um orientador?", "Para que preciso de um orientador?"],
  "responses": ["O orientador eh quem vai acompanhar o projeto de perto e guia-los durante o processo, orientado quanto a qualidade do seu trabalho, qual o proximo passo e ajudar na tomada de decisoes. "]
  },
  { "tag": "apresentacao_tcc",
  "patterns":["Quem pode ver minha apresentacao?", "minha familia pode vir", "posso trazer meu namorado","posso trazer minha namorada","pode vir gente de fora"],
  "responses": ["Qualquer pessoa pode assistir sua apresentacao", "Pode vir todo mundo!"]
  },
  { "tag": "data_tcc",
  "patterns":["Qual a data final?", "Que dia devo apresentar meu tcc?", "Qual horario de apresentacao?"],
  "responses": ["Usualmente a data de avaliacao eh no fim do semestre durante a epoca da P3."]
  },
  { "tag": "divergencia_tcc",
    "patterns":["Entre meu professor de TCC e meu orientador, quem tem a decisao final?","Se meu orientador e professor discordam quem eu sigo?"],
    "responses": ["No caso do seu professor de TCC e orientador terem opinioes distintas, siga seu orientador, \n ele tem uma visao mais aprofundada de seu projeto e pode dar instrucoes mais precisas.\n Entretanto vale a pena pedir para seu orientador conversar com seu professor!"]
  }]
}
```
## 3. Descrição das Intenções
*Descrição das Tags, Patterns e Responses*

**saudacao**: tag de cumprimento onde pode ser o início da interação com o chatbot.
Nele temos como *patterns*, por exemplo, "Olá", "Opa" e como *responses* "Oi", "Oie, espero que esteja bem!".

**despedida**: tag de despedida, na finalização da interação com o chatbot.
Temos como *patterns*, por exemplo, "tchau", "tks" e como *responses* "Até breve", "Tchauzinho".

**introducao_tcc**: Essa tag se refere a dúvida sobre o que é o tcc, onde utilizamos os *patterns* "Como é um tcc?", "Por que fazer o tcc?" e em seguida o chatbot dá a explicação através da *response* aplicada.

**tema_tcc**: Essa tag utiliza os *patterns* "Tema", "Como escolher o tema?", "Tema ciência da computação" para ajudar o usuário, através da *response*, a entender o propósito do tema de tcc.

**opcao_tema_tcc**: Essa tag utiliza os *patterns* "Tema ciência da computação",  "Opções de tema",  para sugerir ao usuário através das *responses* com temas relacionados ao curso de Ciência da Computação.

**integrantes_tcc**: Essa tag utiliza os *patterns* "Grupo", "Com quantas pessoas posso fazer tcc?", "Quantidade de integrantes", etc. Para informar o usuário, através da *response* a quantidade ideal de participantes para o grupo de tcc.

**banca_tcc**: Essa tag é utilizada para responder a quantidade de avaliadores da banca de tcc.

**orientador_tcc**: Essa tag é utilizada para dar dica de como escolher o orientador de tcc. Para isso são utilizados os *patterns* "Quem pode ser meu orientador?", "Como escolho um orientador?", "Meu orientador pode ser de outro curso?".

**funcao_orientador_tcc**: Essa tag é utilizada para explicar ao usuário a função e importância do orientador do tcc.

**apresentacao_tcc**: Essa tag é utilizada para responder ao usuário quem pode assistir a apresentação do tcc.

**data_tcc**: Essa tag é utilizada para responder ao usuário uma data *aproximada* da apresentação do tcc.

**divergencia_tcc**: Essa tag utiliza os *patterns* "Entre meu professor de TCC e meu orientador, quem tem a decisão final?", "Se meu orientador e professor discordam quem eu sigo?" para ajudar o usuário a entender como tratar de divergências entre as opiniões do professor de tcc e do orientador do tcc.

## 3. Exemplo de Interação


## 4. Vídeo
