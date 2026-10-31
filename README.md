# Nome do projeto: 
Yuri Suplementos

#  Tema escolhido: 
Sistema de produtos

# Integrantes do grupo:
### Pedro Henrique Medeiros dos Santos
### Jeizon Gomes da Silva Filho
### João Victor Noberto Tomaz Santana

# Responsabilidade principal de cada integrante;

### Pedro Henrique Medeiros dos Santos:
- Criou estrutura base do projeto + repositório no github e estruturação dos documentos do README e DIÁRIO na wiki.
- Responsável pela camada Models com a criação e alteração das entidades e seus relacionamentos, bem como suas colunas.
- Responsável pelo seed.py e criação dos objetos que compõem o banco.
- Responsável pela estrutura MVC e Blueprint da Entidade Produto.
- Criador dos serviços das imagens dos produtos e comentários.
- Revisor de commits e tratamento na limpeza dos comentários e código.
- Criador parcial das imagens utilizadas no projeto.

### Jeizon Gomes da Silva Filho:
- Responsável pelas views e blueprints de: compras e carrinho.
- Responsável principal por encontrar falhas e testar a aplicação.
- Responsável por adicionar quantidade em toda a aplicação.

### João Victor Noberto Tomaz Santana
- Responsável pela liderança da equipe e distribuição das tarefas.
- Responsável pelas views e blueprints de: user e auth. 
- Responsável pela criação da camada dos services para separação da lógica de negócio das rotas que recebem as requisições.
- Criador parcial das imagens utilizadas no projeto.

# Descrição do sistema;
O sistema Yuri Suplementos tem o objetivo de permitir que usuários possam comprar produtos relacionados a academia, com separação dos itens, compras e carrinhos de cada cliente através do seu id. As compras incluem nomes dos itens, preços, data da compra realizada e comentários opcionais dos clientes. O usuário também pode alterar os dados da compra, como incluir um produto a mais ou a menos, mudar o nome da compra e as descrições daquela compra. Como o projeto tem um foco maior em produtos para academia, o sistema conterá diversos tipos de suplementos e pré-treinos.

# Entidades do sistema:
## (OBS) PK se refere a PrimaryKey, FK se refere a ForeignKey para fins de abreviação e a setinha se refere à coluna de origem da ForeignKey.

### Usuarios
- `id` (Integer, PK)
- `nome` (String)
- `email` (String, Unique)
- `senha_hash` (String)

### Carrinho
- `id` (Integer, PK)
- `usuario_id` (Integer, FK -> usuario.id)

### Compra
- `id` (Integer, PK)
- `descricao` (String)
- `data_criacao` (String)
- `usuario_id` (Integer, FK -> usuario.id)

### Produto
- `id` (Integer, PK)
- `nome` (String)
- `preco` (Float)
- `informacao` (String)

### Comentários
- `id` (Integer, PK)
- `texto` (String)
- `autor` (String)
- `nota` (int)

### carrinho_produto (Tabela Intermediária N:N)
- `carrinho_id` (Integer, FK -> carrinho.id, PK)
- `produto_id` (Integer, FK -> produto.id, PK)

### compra_produto (Tabela Intermediária N:N)
- `compra_id` (Integer, FK -> compra.id, PK)
- `produto_id` (Integer, FK -> produto.id, PK)


# Explicação do relacionamento 1:N ;
- 1 usuário pode ter 1 ou mais (N) compras ao longo do tempo enquanto cada compra é única para cada usuario.
- 1 usuário pode ter 1 ou mais (N) carrinhos ao longo do tempo enquanto está utilizando o site.
- 1 usuário pode ter 1 ou mais (N) comentários sobre 1 ou mais (N) produtos.
- 1 produto pode ter 1 ou mais (N) comentários enquanto 1 comentário pertence a 1 produto, já que um mesmo comentário não pode (ou não deveria, aparecer em produtos diferentes).

# Explicação do relacionamento N:N ;
- 1 Carrinho pode ter 1 ou mais (N) produtos presentes ao mesmo tempo que 1 produto pode constar em 1 ou mais (N) carrinhos. 
- 1 compra pode ter um ou mais produtos nela, da mesma forma que um produto pode aparecer em 1 ou mais (N) compras.

# Instruções para instalar dependências;
- 1: Criar o ambiente vitual. `py -m venv env`

- 2: Ativar o ambiente. `.\env\scripts\activate`

- 3: Instalar a biblioteca Flask. `pip install Flask`

- 4: Instalar a biblioteca do sqlalchemy. `pip install sqlalchemy`

- 5: Instalar as dependências do sqlalchemy.orm. `pip install sqlalchemy.orm`

# Instruções para criar ou popular o banco;
- Para criar e popular o banco basta utilizar o comando `python seed.py` após ter realizado a instalação das dependências anteriores.

# Instruções para executar o sistema;
- Para executar o sistema basta utilizar o comando `flask run --debug` e copiar o endereço do servidor que aparece no prompt de comando.

# Instruções para criar ou popular o banco;
- Para criar e popular o banco basta utilizar o comando `python seed.py` após ter realizado a instalação das dependências anteriores.

# Declaração de autoria:
Declaro que desenvolvemos este projeto e compreendendos o código entregue e que
sou capaz de explicar e modificar suas partes principais.

# Uso de IA:
## [ ] Não utilizmos IA generativa.
## [X] Utilizamos IA generativa e descrevo abaixo como foi utilizada.

# Descrição do uso, se houver:
- utilizamos recursos generativos para produzir e modificar as imagens dos produtos do nosso sistema.
- utilizamos recursos generativos para indicar, revisar e corrigir APENAS elementos de estilização e de definição do layout da página, bem como construções repetitivas de html bruto.
- utilizamos recursos generativos para realizar a construção das imagens dos produtos.

# Justificativa e menções sobre o uso da IA generativa
- Não foi utilizada IA generativa para criar, modificar ou introduzir códigos novos na produção das Camadas dos Controllers e dos Modelos, a construção das entidades, criação dos métodos das entidades, definição dos relacionamentos, população e idealização dos produtos, integração entre as diferentes camadas, correções de bugs nas lógicas de código dos controllers, estruturação das pastas e arquivos, lógica geral de funcionamento do site como adicionar, criar, editar ou remover elementos. Acreditamos que o foco principal desse projeto é testar as habilidades introduzidas e ministradas pelo docente Romerito Campos ao decorrer das disciplinas, perder tempo que poderia ser usado para aperfeiçoar o foco da disciplina em complicações com CSS e HTML foi considerado algo ineficiente de forma unânime entre o grupo.
