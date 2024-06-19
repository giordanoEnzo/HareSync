import nltk
from nltk.stem import RSLPStemmer

nltk.download('rslp')


def radicalizar(texto):
    stemmer = RSLPStemmer()
    texto_formatado = [stemmer.stem(palavra) for palavra in texto]

    return texto_formatado


def remover_stopwords(texto):
    stopwords = ("a à aí agora ainda alguém algum alguma algumas alguns ali ano "
                 "anos antes até bem cada com como contra da daquele daqueles das"
                 " de dela delas deles depois desde desta destas deste deste dia "
                 "dias disse disso disto dólar dois dos é ela elas eles em entre "
                 "então era essa essas esse esses esta está estas estava estavam "
                 "este esteve estive estivemos estiveram estiverem estivermos eu "
                 "foi for foram fosse fossem fui fôssemos geral grandes há até "
                 "depois dentro fora iam isso isto já lugar mais mas meu minha "
                 "minhas meus mês meses muito na nada não nome no nos nós nada "
                 "nem nenhum nenhuma nenhumas nenhuns nunca nuns o onde os ou "
                 "outra outras outro outros para pela pelo pelas pelos pessoa pode "
                 "podem por porém qual quando quem quero seu sua suas seus sempre ser"
                 " será serão seu seus sobre somos tal tem tempo tenho teu tua tuas teus"
                 " tudo um uma umas uns vontade vez vezes")

    texto_separado = texto.split()
    texto_formatado = []

    for palavra in texto_separado:
        if palavra not in stopwords:
            texto_formatado.append(palavra)

    return texto_formatado


def remover_pontuacao(texto):
    pontuacao = ".,;:!?()[]{}--\/*&=+-"
    texto_minusculo = texto.lower()
    texto_formatado = ''

    for char in texto_minusculo:
        if char not in pontuacao:
            texto_formatado += char

    return texto_formatado
