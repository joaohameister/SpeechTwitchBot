import speech_recognition as sr
# Funcao responsavel por ouvir e reconhecer a fala

mapa = {
    "c*": 0
}

def ouvir_microfone():
    # Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        # Chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)
        # Armazena a informacao de audio na variavel
        audio = microfone.listen(source)

        frase = None
        try:
            # Passa o audio para o reconhecedor de padroes do speech_recognition
            frase = microfone.recognize_google(audio_data = audio, language='pt-BR')
            # Após alguns segundos, retorna a frase falada
            

        except:
            pass
        return frase

while True:
    frase = ouvir_microfone()
    if frase is not None:
        palavras = frase.split(" ")

        # Alterar lógica de leitura para cu
        for palavra in palavras:
            if (palavra in mapa) is False:
                mapa[palavra] = 1

            else:
                mapa[palavra] = mapa[palavra] + 1

    print(mapa)