import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
 
from pprint import pprint
import time
import datetime
import json

TOKEN="875253482:AAEBGBMJsWVehz1r6uA2VM38Oc6kCdyTCDE" #da sostituire
ID =  856689208 # Gabbro
ID1 = 838210367 # Fabio
ID2 = 889258127 # Pia
ID3 = 294614221 # Frank
ID4 = 629900380 # Chiara
ID5 = 1253682294 # Sergio
ID6 = 945256843 # Bruno

def conti(*args):
    return sum(args), sum(args)/len(args)

def ordina(*args):
    return sorted(args)

def quadrato(*args):
    area = sum(args) * sum(args)
    return area

def radicequadrata(*args):
    radice = sum(args) ** 0.5
    return radice

def on_chat_message(msg):
    
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat message:', content_type, chat_type, chat_id)
 
    if content_type == 'text':
        name = msg["from"]["first_name"]
        txt = msg['text']
        
        if txt.startswith('/start'):
            bot.sendMessage(chat_id, 'ciao {}, sono un bot molto stupido!'.format(name))
            bot.sendMessage(chat_id, 'Nella tastiera affianco al bottone di allega file troverai un tasto che indica uno "/" premilo per scoprire tutti i miei comandi!')
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                             [InlineKeyboardButton(text='Ciao', callback_data='ciao'),
                             InlineKeyboardButton(text='Contatti', callback_data='info')],
                             [InlineKeyboardButton(text='Time', callback_data='time')],
                         ])
            bot.sendMessage(chat_id, 'Puoi usare anche questa\n      inline keyboard', reply_markup=keyboard)

        elif txt.startswith('/hey'):
            bot.sendMessage(chat_id, 'Hey tutto bene? In che modo posso esserti di aiuto!?')
        elif txt.startswith('/help'):
            bot.sendMessage(chat_id, 'Ecco i comandi che capisco: \n - /start\n - /hey\n - /calcola\n - /riordinare\n - /areaquadrato\n - /radicequadrata')
        elif txt.startswith('/calcola'):
            params = txt.split()[1:]
            if len(params) == 0 or len(params) == 1:
                bot.sendMessage(chat_id, 'Usa il comando calcola in questo modo:\n      /calcola 1 2 3 4 5 ..\n\nUsalo per calcolare la somma e la media dei numeri che inserisci!')
            else:
                try:
                    params = [float(param) for param in params]
                    somma, media = conti(*params)
                    bot.sendMessage(chat_id, 'Somma: {}, media {}'.format(somma, media))
                except:
                    bot.sendMessage(chat_id, 'Errore nei parametri, non hai inserito i numeri correttemante! Digitanto / troverari la lista dei comandi che conosco... ')
        elif txt.startswith('/riordinare'):
            params = txt.split()[1:]
            if len(params) == 0:
                bot.sendMessage(chat_id, 'Usa il comando riordinare in questo modo:\n      /riordinare 99 50 5 10 48 ..\n\nUsalo per mettere in ordine crescente i numeri che inserisci!')
            else:
                try:
                    params = [float(param) for param in params]
                    mx = ordina(*params)
                    bot.sendMessage(chat_id, 'Numeri in ordine: {}'.format(mx))
                except:
                    bot.sendMessage(chat_id, 'Errore nei parametri, non hai inserito i numeri correttemante! Digitanto "/" troverari la lista dei comandi che conosco... ')
        elif txt.startswith('/areaquadrato'):
            params = txt.split()[1:]
            if len(params) == 0:
                bot.sendMessage(chat_id, 'Usa il comando areaQuadrato in questo modo:\n      /areaquadrato 4\n\nSe gli assegni piu numeri prima di eseguire il calcolo li somma per avere un solo numero da elevare a potenza!')
            else:
                try:
                    params = [float(param) for param in params]
                    mx = quadrato(*params)
                    bot.sendMessage(chat_id, 'Area del quadrato: {}'.format(mx))
                except:
                    bot.sendMessage(chat_id, 'Errore nei parametri, non hai inserito i numeri correttemante! Digitanto "/" troverari la lista dei comandi che conosco... ')
        elif txt.startswith('/radicequadrata'):
            params = txt.split()[1:]
            if len(params) == 0:
                bot.sendMessage(chat_id, 'Usa il comando radiceQuadrata in questo modo:\n      /radicequadrata 8\n\nSe gli assegni piu numeri prima di eseguire il calcolo li somma per avere un solo numero da elevare a potenza!')
            else:
                try:
                    params = [float(param) for param in params]
                    mx = radicequadrata(*params)
                    bot.sendMessage(chat_id, 'La radice quadrata: {}'.format(mx))
                except:
                    bot.sendMessage(chat_id, 'Errore nei parametri, non hai inserito i numeri correttemante! Digitanto "/" troverari la lista dei comandi che conosco... ')
        else:
            bot.sendMessage(chat_id, 'Mi spiace {}, non capisco...\nUsa /help per sapere cosa posso fare!'.format(name))
        
    
def on_callback_query(msg):
    
    query_id, chat_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, chat_id, query_data)
          
    if query_data == 'ciao':
        bot.sendMessage(chat_id, 'Ciao sono un bot prova!\nProva i miei comandi, se non li trovi digita "/" sulla tastiera!! ')
        time.sleep(0.5)
        bot.answerCallbackQuery(query_id, 'Mi hanno insegnato a fare piccoli calcoli!!')
    elif query_data == 'info':
        bot.sendMessage(chat_id, 'Proprietario del Bot Prova:\nPer maggiori informazioni risponde al seguente account Telegram: @Gabbro_95')
    elif query_data == 'time':
        ts = time.time()
        bot.answerCallbackQuery(query_id, text=datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')) #messaggio a comparsa

if __name__ == '__main__':
    bot = telepot.Bot(TOKEN)
    MessageLoop(bot, {'chat': on_chat_message,
                      'callback_query': on_callback_query}).run_as_thread() 
    print('Listening ...')
     
     
    while 1:
        
        time.sleep(10)
