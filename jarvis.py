import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit


audio = sr.Recognizer()  # Instância do Recognizer
maquina = pyttsx3.init()  # Inicializa o mecanismo de texto para fala

def listen_command():
    try:
        with sr.Microphone() as source:
            print('Escutando...')
            voz = audio.listen(source)  # Captura o áudio do microfone
            comando = audio.recognize_sphinx(voz, language="pt-BR")  # Converte áudio em texto
            comando = comando.lower()
            if 'jarvis' in comando:
                comando = comando.replace("jarvis", "").strip()
                return comando
    except sr.UnknownValueError:
        print("Não foi possível entender o que você disse.")
    except sr.RequestError as e:
        print(f"Erro ao acessar o serviço de reconhecimento de fala: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    return None  # Retorna None caso ocorra um erro

def execute_command():
    comando = listen_command()
    if comando:
        if 'procure por' in comando or 'pesquise por' in comando:
            procurar = comando.replace('procure por', '').replace('pesquise por', '').strip()
            wikipedia.set_lang('pt')
            try:
                resultado = wikipedia.summary(procurar, sentences=2)
                print(resultado)
                maquina.say(resultado)
                maquina.runAndWait()
            except wikipedia.exceptions.DisambiguationError as e:
                print(f"Há várias opções para sua busca: {e}")
            except wikipedia.exceptions.PageError:
                print("Nenhum resultado encontrado.")
        elif 'toque' in comando:
            musica = comando.replace('toque', '').strip()
            print(f"Tocando {musica} no YouTube...")
            pywhatkit.playonyt(musica)
        else:
            print("Comando não reconhecido.")
    else:
        print("Nenhum comando foi detectado.")

# Loop principal
while True:
    execute_command()
