# Nome do projeto: 
Yuri Suplementos

#  Tema escolhido: 
Sistema de produtos

# Integrantes do grupo:
### Pedro Henrique Medeiros dos Santos
### Jeizon Gomes da Silva Filho
### João Victor Noberto Tomaz Santana

# Responsabilidade principal de cada integrante;

# Descrição do sistema;
O sistema Yuri Suplementos tem o objetivo de permitir que usuários possam comprar produtos a partir da criação de novas receitas (prescrições) cada usuário terá sua própria receita com seus produtos, incluindo nomes dos itens, preços e data da compra realizada. O usuário também pode alterar os dados da receita, como incluir um produto a mais ou a menos e mudar o nome da receita. Como o projeto tem um foco maior em produtos para academia, o sistema conterá diversos tipos de suplementos e pré treinos.

# Entidades do sistema:
## (OBS) PK se refere a PrimaryKey, FK se refere a ForeignKey para fins de abreviação e a setinha se refere à coluna de origem da ForeignKey. Além disso, a criação da entidade Compra pode parecer desnecessária, entretanto, ela facilita a comunicação entre os elementos do banco de dados e é formaliza de fato as compras das receitas dos produtos/suplementos.

### Usuarios
- `id` (Integer, PK)
- `nome` (String)
- `email` (String, Unique)
- `senha_hash` (String)

### Receita
- `id` (Integer, PK)
- `descricao` (String)
- `data_criacao` (String)
- `usuario_id` (Integer, FK -> usuario.id)

### Compra
- `id` (Integer, PK)
- `descricao` (String)
- `data_criacao` (String)
- `usuario_id` (Integer, FK -> usuario.id)

### Produtos
- `id` (Integer, PK)
- `nome` (String)
- `preco` (Float)
- `informacao` (String)

### receita_produto (Tabela Intermediária N:N)
- `receita_id` (Integer, FK -> receita.id, PK)
- `produto_id` (Integer, FK -> produto.id, PK)

### compra_produto (Tabela Intermediária N:N)
- `compra_id` (Integer, FK -> compra.id, PK)
- `produto_id` (Integer, FK -> produto.id, PK)

# Explicação do relacionamento 1:N ;
1 usuário pode ter 1 ou mais (N) receitas ao longo do tempo enquanto cada receita pertence apenas a 1 usuário. Da mesma forma, um usuário pode ter 1 ou mais compras ao longo do tempo enquanto cada compra é única para cada usuario

# Explicação do relacionamento N:N ;
1 Receita pode ter 1 ou mais (N) produtos prescritos ao mesmo tempo que 1 produto pode constar em 1 ou mais (N) receitas de produtos. Uma compra pode ter um ou mais produtos nela, da mesma forma que um produto pode aparecer em uma ou mais compras.

# Instruções para instalar dependências;

# Instruções para criar ou popular o banco;

# Instruções para executar o sistema;
