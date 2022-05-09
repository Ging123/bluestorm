# BLUESTORM

## indice

[Como se executar](#como-se-executar)

[Rotas e exemplos](#rotas-e-exemplos)

[Processo para criar minha solução](#processo-para-criar-minha-solução)

## Como se Executar

Para se executar a aplicação, é bem simples, a primeira coisa que você precisa fazer é criar um arquivo **.env no root** da aplicação. Você deve colocar dentro desse arquivo as váriaveis de ambientes que estão no arquivo **example.env**.
Após criar o seu .env, o próximo passo é criar e executar um **ambiente virtual**

### para windows
```
#Cria o ambiente virtual
py -3 -m venv venv
#Executa o ambiente virtual
venv\Scripts\activate
```

### para mac ou linux
```
#Cria ambiente virtual
python3 -m venv venv
#Executa o ambiente virtual
venv/bin/activate
```

### Instalando dependências
Após isso o próximo passo vai ser instalar todas dependências necessárias para rodar a aplicação executando o seguinte comando

```
#Irá instalar todas as dependências necessárias para a aplicação
pip install -r requirements.txt
```

### Rodando a aplicação
Agora que você tem todas dependências instaladas, você pode executar a aplicação e a testar usando os seguintes comandos:

```
#Irá entrar na pasta mysite cuja contém diversos comandos de terminal
cd mysite
#Irá levantar a aplicação 
python manage.py runserver
```

### Rodando testes
Para testar a aplicação basta execultar o seguinte comando

```
#examplo: python manage.py test users.tests.create_user

python manage.py test <nome do app para testar>.tests.<arquivo com os testes>
```

## Rotas e Exemplos
| método | rota          | headers                   | payload                                     |
|--------|---------------|---------------------------|---------------------------------------------|
| POST   | users/        |                           | {email:"g@gmail.com", password:"123456789"} |
| POST   | users/login/  |                           | {email:"g@gmail.com", password:"123456789"} |
| GET    | patients/     | {authorization:"token"}   |                                             |
| GET    | pharmacies/   | {authorization:"token"}   |                                             |
| GET    | transactions/ | {authorization:"token"}   |                                             |

- 1 - POST users/: Irá criar uma conta para você
- 2 - POST users/login/: Irá permitir que você logue na sua conta e consiga um token que será usado para fazer requisições em outras rotas
- 3 - GET patients/: Retorna os dados dos pacientes
- 4 - GET pharmacies/: Retorna os dados das farmácias
- 5 - GET transactions/: Retorna os dados das transações

## Processo Para Criar Minha Solução

Para desenvolver a minha solução eu primeiro separei as funcionalidades que eu queria em três ordens diferentes de prioridades:
- Essenciais: Sem essas funcionalidades a aplicação não irá funcionar.
- Importantes: É possível usar a aplicação sem essas funcionalidades porém o usuário não terá uma experiência tão agradavel.
- Extra: Funcionalidade que podem ser trabalhadas em próximas versões da aplicação
Após eu definir as funcionalidades, eu comecei a escolher as tecnológias que eu iria utilizar.
 
Como eu tava afim de aprender um framework novo eu escolhi o django pois ele parecia muito bom para trabalhar com aplicações rest e já tinha um sisteminha de migrations para facilitar meu trabalho com o sqlite.