#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__      = "Germán Culqui"
__copyright__   = "Escuela Politécnica Nacional"
__credits__     = ["Germán Culqui","EPN"]
__license__     = "GPL"
__version__     = "1.5"
__description__ = " Bot para telegram, Objetivo realizar pruebas de uso de modelos CNN, para verificacion de firmas manuscritas"
__email__       = "german.culqui@epn.edu.ec"
__status__      = "En desarrollo, ultima actualizacion Agosto / 2021"

import logging
import os
from   os           import listdir
from   os.path      import isfile
from   telegram     import Update
from   telegram.ext import Updater, CommandHandler, CallbackContext,  MessageHandler, Filters
from   keras.preprocessing.image   import ImageDataGenerator
from   keras.models                import load_model
import pandas       as     pd
import numpy        as     np
from   sklearn.metrics             import confusion_matrix
from   sklearn                     import metrics
from   time import time

print(__doc__) 


BOT_TOKEN         = "1998228436:AAFFiwDruVZeDQzxCzRCWf4Z999P3XCeN5I"
institucion       = "Escuela Politecnica Nacional - Ecuador"
name              = "An Algorithm for Classifying Handwritten "+ \
                    "Signatures Using Convolutional Networks" 
student           = "German Culqui, Sandra Sanchez, Myriam Hernandez"

logging.basicConfig( format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO )

logger = logging.getLogger(__name__)

def ListarArchivos(path):    
    return [obj for obj in listdir(path) if isfile(path + '/'+obj)]

def ListarDirectorios(path):    
    return [obj for obj in listdir(path) if isfile(path + '/'+obj) == False]

def ExisteArchivo(file):    
    if os.path.isfile(file) :
        return True
    else :
        raise ValueError(' El archivo "'+file+'", no existe ')
    return False

def bienvenida(update: Update, context: CallbackContext) -> None:
    user_name = update.effective_user['first_name']
    update.message.reply_text(f'Bienvenido <b>{user_name}</b>, digita <b>/help</b> o presiona sobre el texto, para obtener ayuda sobre el uso de este Bot', parse_mode="HTML")

def abstract(update: Update, context: CallbackContext) -> None:
    documento = 'A model based on convolutional neural networks is proposed to quickly and efficiently classify and '\
                'identify the signature of a person with an accuracy greater than 90%. Two sets of signature data were used.'\
                ' The first, entitled CEDAR available for public access, and the second compiled by the researchers'\
                ' entitled GC-DB, in uncontrolled environments (different positions to sign), made up of 121 local '\
                'signers from the Republic of Ecuador, who delivered 45 signature copies each one, in this set of '\
                'signatures, the implicit noise produced by the capture device and by the paper of different thicknesses '\
                'used in its collection, made the elimination of noise a relatively complex operation. '\
                'The efficiency of the proposed algorithm was compared with two other algorithms that were implemented '\
                'and validated with the same data sets. The results show that an efficient classification of handwritten'\
                ' signatures can be executed exceeding the established objective. The built algorithm is light and easy '\
                'to implement, and can be installed on handheld devices such as cell phones or tablets.'
    update.message.reply_text(f'{documento}', parse_mode="HTML")


def description(update: Update, context: CallbackContext) -> None:
    global student
    descripcion = ' Este bot ha sido creado por los autores del paper titulado <b>An Algorithm for Classifying Handwritten ' \
                ' Signatures Using Convolutional Networks.</b>'\
                ' Este Bot esta sujeto a cambios constantes, debido a que se usa para probar los modelos de la red CNN-GCC'\
                ' descrita en el paper, asi como las aplicaciones en trabajos futuros relacionados con el mismo.'\
                ' Los autores de este paper son <b>'+student+'</b>, patrocinados por la <b>'+institucion+'</b>'
    update.message.reply_text(descripcion, parse_mode="HTML")

def salir(update: Update, context: CallbackContext) -> None:
    user_name = update.effective_user['first_name']    
    update.message.reply_text('Gracias <b>{user_name}</b>, por tu visita.', parse_mode="HTML")
    

def ValidarModelo(update: Update, context: CallbackContext) -> None:
    
    DefCedarFileModel1   = './models/CNN-MCGC-CEDAR.h5'
    DefDBGCFileModel1    = './models/CNN-MCGC-DBGC.h5'
    IMAGE_SIZE = (340,440)

    modelo     = DefCedarFileModel1
    PATH_BASE  = '.'    
    CEDAR      = '/cedar'
    DBGC       = '/dbgc'    
    test_dir   = PATH_BASE+CEDAR
    
    start_time = time()
    
    if ExisteArchivo(modelo):    
        clasificador    = load_model(modelo)
    else :
        update.message.reply_text('El modelo '+modelo+' NO EXISTE')
        return
    elapsed_time = time()-start_time

    update.message.reply_text('Modelo CNN-GC, Base CEDAR')    
    update.message.reply_text('Tiempo de carga del modelo %0.10f segundos'%elapsed_time)    

    start_time      = time()        
    clases          = ListarDirectorios(test_dir)
    clases.sort()
    test_datagen    = ImageDataGenerator()
    test_generator  = test_datagen.flow_from_directory(test_dir, target_size=IMAGE_SIZE, batch_size = 8, class_mode='categorical', shuffle=False, color_mode='grayscale')
    elapsed_time    = time()-start_time
    update.message.reply_text('Tiempo de carga de imagenes 55*4 %0.10f segundos'%elapsed_time)    


    start_time      = time()        
    predicciones    = clasificador.predict_generator(generator = test_generator)
    y_predicciones  = np.argmax(predicciones, axis = 1)
    y_real          = test_generator.classes
    elapsed_time    = time()-start_time
    update.message.reply_text('Tiempo de prediccion 55 clases %0.10f segundos'%elapsed_time)    

    # Datos del modelo con la base DB-GC
    modelo     = DefDBGCFileModel1
    test_dir   = PATH_BASE+DBGC
    start_time      = time()            
    if ExisteArchivo(modelo):    
        clasificador    = load_model(modelo)
    else :
        update.message.reply_text('El modelo '+modelo+' NO EXISTE')
        return
    elapsed_time = time()-start_time
    update.message.reply_text('==================================')
    update.message.reply_text('Modelo CNN-GC, Base DB-GC')    
    update.message.reply_text('Tiempo de carga del modelo %0.10f segundos'%elapsed_time)    

    start_time      = time()        
    clases          = ListarDirectorios(test_dir)
    clases.sort()
    test_datagen    = ImageDataGenerator()
    test_generator  = test_datagen.flow_from_directory(test_dir, target_size=IMAGE_SIZE, batch_size = 8, class_mode='categorical', shuffle=False, color_mode='grayscale')
    elapsed_time    = time()-start_time
    update.message.reply_text('Tiempo de carga de imagenes 121*7 %0.10f segundos'%elapsed_time)    

    start_time      = time()        
    predicciones    = clasificador.predict_generator(generator = test_generator)
    y_predicciones  = np.argmax(predicciones, axis = 1)
    y_real          = test_generator.classes
    elapsed_time    = time()-start_time
    update.message.reply_text('Tiempo de prediccion 121 clases %0.10f segundos'%elapsed_time)    
    
    return      
    
def help_command(update: Update, context: CallbackContext) -> None:
    """Envía un mensaje de información a la pantalla de Telegram."""
    update.message.reply_text('<b>Comandos disponibles</b>', parse_mode="HTML")
    update.message.reply_text('/abstract  /description  /summary  /individual  /help')
    update.message.reply_text('digita un comando o presiona sobre el texto del comando')    

def main() -> None:
    global BOT_TOKEN
   
    global institucion

    """Se inicia el Bot"""
   
    updater    = Updater(token = BOT_TOKEN)
    dispatcher = updater.dispatcher   

    # Menu principal de telegram
    dispatcher.add_handler(CommandHandler("start",      bienvenida))  
    dispatcher.add_handler(CommandHandler("help",       help_command))
    dispatcher.add_handler(CommandHandler("abstract",   abstract))    
    dispatcher.add_handler(CommandHandler("description",description)) 
    dispatcher.add_handler(CommandHandler("summary",    ValidarModelo))     
    dispatcher.add_handler(CommandHandler("individual", ValidarModelo))         
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, bienvenida))       
    
    # Inicial el Bot
    updater.start_polling()

    # Se ejecuta hasta que se presione  Ctrl-C 
    updater.idle()


if __name__ == '__main__':
    main()
