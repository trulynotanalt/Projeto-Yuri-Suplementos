from pathlib import Path

PASTA = Path(__file__).resolve().parent.parent / "static" / "img" / "produtos"


IMAGEM_POR_PRODUTO = {
    "Starters train": "starter.jpeg",
    "25-25 power": "2525power.jpeg",
    "Treino dos psicóticos": "treino_dos_psicoticos.jpeg",
    "A noite treina": "anoitetreina.jpeg",
    "Treino dos moggers": "moggers.jpg",
    "Alegria do jojo": "alegria_do_jojo.jpeg",
    "Segredinho dos 40 da Caixa": "segredinho_da_caixa.png",
    "Romeritos coffee": "romeritos_coffee.png",
    "Helaidios mix": "helaidios_mix.png",
    "Hirobraço e Nagapeito": "hirobraco_nagapeito.png",
    "Po do yuri": "po_do_iuri.jpg",
    "A perna do cangaço": "aperna_do_cangaco.jpg",
    "Medeiros Growth": "medeiros_growth.png",
    "Nobertos Abs": "noberto_abs.png",
    "Cleysys MegaBrain": "cleysys_megabrain.png",
    "GH Anderson": "ghanderson.jpg",
    
}


def imagem_do_produto(produto):
    arquivo = IMAGEM_POR_PRODUTO.get(produto.nome)
    if arquivo and (PASTA / arquivo).is_file():
        return arquivo 
    else: None
