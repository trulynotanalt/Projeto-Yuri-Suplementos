from database import nova_sessao, criar_banco, Base
from models.entidades import Produto, Comentario

def popular_banco():
    produtos = [
        
        Produto(
            nome="Starters train",
            preco=59.90,
            categoria="Pré-Treino",
            informacao="Quantidade moderada de calorias, vitaminas e proteínas. Para quem ta começando a malhar."
        ),
        Produto(
            nome="25-25 power",
            preco=145.50,
            categoria="Pré-Treino",
            informacao="Aumenta a taxa de ganho de massa geral em 25% para braço e 25% para perna. (OBS) Te deixa um pouco lesado caso use muito."
        ),
        Produto(
            nome="Treino dos psicóticos",
            preco=210.00,
            categoria="Pré-Treino",
            informacao="Potencializador de performance e resistência muscular para os ratões da academia."
        ),
        Produto(
            nome="A noite treina",
            preco=119.90,
            categoria="Pré-Treino",
            informacao="Fórmula concentrada em cafeína e proteínas para madrugar no treino."
        ),
        Produto(
            nome="O Pós-Treino",
            preco=555.00,
            categoria="Pré-Treino",
            informacao="Efeito pump prolongado por 12 horas e máxima vascularização. Substitui todos os tipos de refeições possíveis devido a sua contentração em carboidratos, vitaminas, proteinas e lipídeos."
        ),

        
        Produto(
            nome="Alegria do jojo",
            preco=159.90,
            categoria="Bomba",
            informacao="Concentrado de cuscuz líquido feito em 15 minutos no vapor do sol de 45 graus de Caicó. Dobra a potência muscular."
        ),
        Produto(
            nome="Segredinho dos 40 da Caixa",
            preco=229.00,
            categoria="Bomba",
            informacao="Fórmula de suporte para ganho de massa muscular rápido. (OBS) Deixa sua cabeça um pouco lisa."
        ),
        Produto(
            nome="Romeritos coffee",
            preco=395.00,
            categoria="Bomba",
            informacao="Combinação potente de carboidratos complexos, cortisol e adrenalina, perfeito para quem quer passar o dia treinando."
        ),
        Produto(
            nome="Helaidios mix",
            preco=175.00,
            categoria="Bomba",
            informacao="Um grande químico fez uma mistura de aminoácidos e conjuntos enzimáticos capazes de alterar a forma e desenvolvimento dos seus membros."
        ),
        Produto(
            nome="Hirobraço e Nagapeito",
            preco=249.90,
            categoria="Bomba",
            informacao="São 2 bombas em uma só, aumenta seus braços e peitos em até 5cm."
        ),

        
        Produto(
            nome="Pó do yuri",
            preco=1000.67,
            categoria="Magia Muscular",
            informacao="Pó proteico usado pelo Grande e ilustre Pedro Yuri em seus tempos aureos, iguala seu shape ao dele."
        ),
        Produto(
            nome="A perna do cangaço",
            preco=239.90,
            categoria="Magia Muscular",
            informacao="Faz suas pernas ficarem tão fortes quanto a de um maratonista ai..."
        ),
        Produto(
            nome="Medeiros Growth",
            preco=260.90,
            categoria="Magia Muscular",
            informacao="Contém 18 ovos misturados com whey de baunilha no seu maior teor de pureza, ótimo para ficar grandão sem ganhar gordura."
        ),
        Produto(
            nome="Nobertos Abs",
            preco=410.00,
            categoria="Magia Muscular",
            informacao="Contém enzimas que contraem seu abdomen involuntariamente, deixando-o trincado que nem ferro. "
        ),
        Produto(
            nome="Cleysys MegaBrain",
            preco=539.90,
            categoria="Magia Muscular",
            informacao="Estimulador neural para dobramento extremo do cérebro, para aqueles que querem tirar da gordura e dar ao saber" 
            
        ),
        Produto(
            nome="GH Anderson",
            preco=72.90,
            categoria="Bateu Morreu",
            informacao="Desidrata que nem o sol do nordeste e deixa o cara trincado que Parede rachada de casa quitada em 35 anos.  " 
                    
        ),
    ]


    
    comentarios = [
        ("Rafael M.", "Starters train", 5, "Comecei a malhar faz um mês e o Starters train foi perfeito: calorias na medida, com vitaminas e proteínas sem exagero."),
        ("Camila S.", "25-25 power", 4, "Braço e perna responderam bem. Mas o aviso é real: usei demais e fiquei um pouco lesada. Com moderação é ótimo."),
        ("Lucas P.", "A noite treina", 5, "Treino de madrugada é comigo. A cafeína com proteína me segurou até a última série."),
        ("Ana B.", "Alegria do jojo", 5, "Parece piada, mas o cuscuz líquido funciona. Fica pronto em 15 minutos e a potência nos treinos subiu muito."),
        ("Diego F.", "Segredinho dos 40 da Caixa", 4, "Ganhei massa rápido, como diz a descrição. O aviso sobre a cabeça lisa também é verdade."),
        ("Marina T.", "Hirobraço e Nagapeito", 5, "São duas bombas em uma só. Braço e peito cresceram em poucas semanas. Me senti como se estivesse em umas certas cidades japonesas."),
        ("Bruno A.", "Medeiros Growth", 5, "18 ovos com whey de baunilha: fiquei grandão sem ganhar gordura, e o sabor é ótimo."),
        ("Henrique L.", "Pó do yuri", 4, "É caro, mas é o pó proteico que o próprio Yuri das lendas usava. Meu shape está chegando perto do dele."),
    ]

    with nova_sessao() as session:

        
        if session.query(Produto).count() == 0:
            session.add_all(produtos)
            session.flush()

        if session.query(Comentario).count() == 0:
            por_nome = {p.nome: p for p in session.query(Produto).all()}
            for autor, produto_nome, nota, texto in comentarios:
                comentario_p = Comentario(autor = autor, nota = nota, texto = texto, produto = por_nome[produto_nome])
                session.add(comentario_p)

        session.commit()

if __name__ == "__main__":
    criar_banco()
    popular_banco()
