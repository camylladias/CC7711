# ChatBot -> tcc
##### Disciplina Inteligência Artificial e Robótica - Ciência da Computação FEI

Atividade #1 – Chatbot 
Você foi designado para criar um chatbot que ajuda o professor de TCC I e para isso, o MVP deve auxiliar um usuário com suas dúvidas em relação aula de introdução da disciplina

## 1. Inicialização do código

Para evitar problemas de versionamento, dentro da pasta ``CC7711`` crie o ambiente virtual:

    python -m venv venv

Em seguida, ative o ambiente virtual:

    .\venv\Scripts\activate

Instale o [Python 3](https://www.python.org/downloads/), dentro da pasta ``chatbot`` instale os pacotes do arquivo *pacotes.txt*:

    pip install -r pacotes.txt
    
Inicie a interação com o chatbot em modo *createModel* (-c) para treinar o modelo:

    python3 main2.py -c
    
Em seguida, entre com CRTL+C e inicie o chatbot em modo *loadModel* (-l) para carregar o modelo:

    python3 main2.py -l

## 2. Intenções
Arquivo *intents.json*:
``` {"intents":[

{ "tag": "saudacao",

"patterns":["Ola","Opa","Oi", "tudo bem"],

"responses": ["Oi","Olá", "Oie, espero que esteja bem!"]

},

{ "tag": "despedida",

"patterns":["valeu","tchau","Obrigado","tks"],

"responses": ["Até breve","Falou", "Tchauzinho!"]

},

{ "tag": "introducao_tcc",

"patterns":["Como é um tcc?","Por que fazer o tcc?"],

"responses": ["O TCC é uma avaliação que acontece quando a graduação está chegando ao fim. Ele tem o objetivo de fazer com que o aluno coloque no papel tudo o que aprendeu até o momento, desde o início dos estudos. Assim, é possível saber se tudo foi absorvido e entendido corretamente."]

},

{ "tag": "tema_tcc",

"patterns":["Tema","Como escolher o tema?", "Tema ciência da computação"],

"responses": ["O tema de uma monografia deve ser o mais específico possível, não pode ser um assunto muito aberto. Um assunto único e específico possibilita um melhor aprofundamento e faz com que os leitores do TCC, principalmente a banca examinadora, criem as expectativas corretas, sabendo exatamente o que será abordado na pesquisa."]

},

{ "tag": "opcao_tema_tcc",

"patterns":["Tema ciência da computação", "Opções de tema"],

"responses": ["Criação de ChatBot para avaliação do estado mental dos funcionários do Metrô de SP", "Como podemos anonimizar automaticamente as imagens das pessoas em gravações de vídeo", "Detecção de fraudes em cartões de crédito com aprendizado de máquina", "Análise de sentimentos em redes sociais"]

},

{ "tag": "integrantes_tcc",

"patterns":["Grupo","Com quantas pessoas posso fazer tcc?", "Quantidade de integrantes", "Posso fazer grupo de um?", "Posso fazer grupo com pessoas de outro curso?", "Posso fazer sozinho?"],

"responses": ["É recomendado o grupo de TCC ter 4 pessoas, mas pode-se fazer com menos pessoas, tendo em vista que ainda será esperado um trabalho digno de quatro \n integrantes, ou mais pessoas, mas tendo mais pessoas será esperado que o trabalho reflita essa diferença. "]

},

{ "tag": "banca_tcc",

"patterns":["Quem avalia?","Quantos avaliadores?", "Como é a banca?", "Banca"],

"responses": ["São 3 avaliadores."]

},

{ "tag": "orientador_tcc",

"patterns":["Quem pode ser meu orientador?","Como escolho um orientador?", "Meu orientador pode ser de outro curso?"],

"responses": ["Seu orientador pode ser qualquer professor da FEI de qualquer curso. E interessante que seja alguém com quem tenha uma boa relação e em quem confie.\n Além disso é importante que a área de seu tema seja algo com que ele ou ela esteja familiarizado."]

},

{ "tag": "funcao_orientador_tcc",

"patterns":["Por que preciso de um orientador","Qual a função de um orientador?", "Para que preciso de um orientador?"],

"responses": ["O orientador é quem vai acompanhar o projeto de perto e guia-los durante o processo, orientado quanto a qualidade do seu trabalho, qual o próximo passo e ajudar na tomada de decisões. "]

},

{ "tag": "apresentacao_tcc",

"patterns":["Quem pode ver minha apresentação?", "minha família pode vir", "posso trazer meu namorado","posso trazer minha namorada","pode vir gente de fora"],

"responses": ["Qualquer pessoa pode assistir sua apresentação", "Pode vir todo mundo, queride! Boa sorte amore s2"]

},

{ "tag": "data_tcc",

"patterns":["Qual a data final?", "Que dia devo apresentar meu tcc?", "Qual horário de apresentação?"],

"responses": ["Usualmente a data de avaliação é no fim do semestre durante a época da P3."]

},

{ "tag": "divergencia_tcc",

"patterns":["Entre meu professor de TCC e meu orientador, quem tem a decisão final?","Se meu orientador e professor discordam quem eu sigo?"],

"responses": ["No caso do seu professor de TCC e orientador terem opiniões distintas, siga seu orientador, \n ele tem uma visão mais aprofundada de seu projeto e pode dar instruções mais precisas.\n Entretanto vale a pena pedir para seu orientador conversar com seu professor!"]
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
![img1.png](https://github.com/camylladias/CC7711/blob/main/chatbot/arquivos/img1.png?raw=true)

## 4. Vídeo

https://user-images.githubusercontent.com/37374749/223206125-1f1a43a6-b837-4086-bed2-8eeeec1696b0.mp4
###### [Atividade 1 - ChatBot (CC7711 - FEI) - YouTube](https://www.youtube.com/watch?v=Eph6xjY803s)
