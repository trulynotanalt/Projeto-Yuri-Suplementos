from database import nova_sessao, criar_banco, Base
from models.entidades import Produto

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
            nome="Jeizons MegaBrain",
            preco=539.90,
            categoria="Magia Muscular",
            informacao="Estimulador neural para dobramento extremo do cérebro, perfeito para quem quer ficar grande não só no braço como na mente." 
            
        ),
        Produto(
            nome="GH Anderson",
            preco=72.90,
            categoria="Bateu Morreu",
            informacao="Desidrata que nem o sol do nordeste e deixa o cara trincado que Parede rachada de casa quitada em 35 anos.  " 
                    
        ),
    ]

    with nova_sessao() as session:
        
        qtd_existente = session.query(Produto).count()
        if qtd_existente > 0:
            return None

        session.add_all(produtos)
        session.commit()
        

if __name__ == "__main__":
    criar_banco()
    popular_banco()