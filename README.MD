## README.MD
Modelo de IA para Diagnóstico Automotivo
Objetivo:

Este projeto tem como objetivo auxiliar os usuários a identificar possíveis problemas em seus veículos através de uma interface simples e intuitiva. O modelo de inteligência artificial foi desenvolvido utilizando técnicas de aprendizado de máquina para analisar descrições textuais de problemas automotivos e fornecer um diagnóstico preliminar e uma estimativa de custo para reparo.


ORDEM PARA CRIACAO DE CADA COISA

1. Comecei pelo Dataset.csv (/src/data)
Objetivo: Garantir que os dados seram usados estão prontos e bem formatados para o treino do meu Machine Learn.

2. Treinar o Modelo (/src/models)
Objetivo: Treine e ajuste o modelo de Machine Learning.

3. Implementar o Fluxo de Inferência (/src/ml)
Objetivo: Criar um fluxo onde o modelo recebe novas entradas e faz inferências.

4. Integração com o Chatbot (/src/integration)
Objetivo: Integrar o Watson Assistant com o modelo.

5. Banco de Dados (/src/database)
Objetivo: Configure o banco de dados para armazenar resultados das inferências.

6. Front-End (/src/frontend)
Objetivo: Conecte a interface do usuário para que o chatbot esteja acessível.

Ordem que estou seguindo para chegar ao final da entrega da porto
Dados → 2. Modelo → 3. Inferência → 4. Integração → 5. Banco de Dados → 6. Front-End



No Projeto utilizei o Gemini para realizar um diagnostico mais preciso

a ideia e que o usuario consiga realizar o pre diagnostico e conseguir um pre orcamento


Minhas Dificuldades durante o Projeto:

Aumentar o Acurrancy do Modelo Treinado: tive um problema inicial pois meus dados estavam nao fazendo muito sentido com o que era pra ser entregue logo realizei uma mudanca completa no modelo utilizei tambem o treino gridsearch do multinomialNB por recomendacao do professor

Conexao com a Api: A principio fiquei sem saber como faria para que meu modelo conversasse com a API do Gemini mais apos algumas buscas consegui utilizar a biblioteca Flask do Python para conseguir.

Integrassao com o Watson: de Longe a unica coisa que eu realmente nao consegui fazer foi conectar meu projeto ao Watson por nao ter muito conhecimento eu acabei ficando preso tentei utilizar o Postman para fazer testes mais sem sucesso.



Grupo AutoCall - 1TDSPW

Ruan Lima Silva - 558775

Richardy Borges - -557883

Henrique Izzi - 555413