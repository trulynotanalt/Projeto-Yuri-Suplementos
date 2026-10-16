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

### carrinho_produto (Tabela Intermediária N:N)
- `carrinho_id` (Integer, FK -> carrinho.id, PK)
- `produto_id` (Integer, FK -> produto.id, PK)

### compra_produto (Tabela Intermediária N:N)
- `compra_id` (Integer, FK -> compra.id, PK)
- `produto_id` (Integer, FK -> produto.id, PK)

# Explicação do relacionamento 1:N ;
Um usuário pode ter 1 ou mais (N) compras ao longo do tempo enquanto cada compra é única para cada usuario, Um usuário pode ter 1 ou mais (N) carrinhos ao longo do tempo enquanto cada carrinho é único para cada usuario

# Explicação do relacionamento N:N ;
1 Carrinho pode ter 1 ou mais (N) compras presentes ao mesmo tempo que 1 compra pode constar em 1 ou mais (N) carrinhos. Uma compra pode ter um ou mais produtos nela, da mesma forma que um produto pode aparecer em uma ou mais compras.

# Instruções para instalar dependências;

# Instruções para criar ou popular o banco;

# Instruções para executar o sistema;
