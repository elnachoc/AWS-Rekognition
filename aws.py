#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import datetime

def verificar(prueba,control):
    resultado = True
    for pp in control:
        if pp not in prueba:
            resultado = False
    return(resultado)

def detect_text(imagen, bucket):

    client=boto3.client('rekognition')
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':imagen}})
    TDetectControl=response['TextDetections']
    arreglo = []
    print ('Imagen Control\n----------')
    for text in TDetectControl:
        if (text['Type'] == "WORD"):
            print ('Detected text:' + text['DetectedText'])
            print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            if ((text['Confidence']) > 96.99):
                arreglo.append(text['DetectedText'])
    return arreglo
    
def main():
    # Variables AWS Rekognice
    bucket='bucketignacio'
    imagenControl ='control.png'
    imagenes = ["test-1.png","test-2.png","test-3.png","test-4.png","test-5.png","test-6.png","test-7.png","test-8.png","test-9.png","test-10.png","test-11.png","test-12.png","test-13.png","test-14.png","test-15.png"]
    for imagen in imagenes:
        #log
        log = open("log.txt","a")
        ahora = datetime.datetime.now()
        writeTime = ahora.strftime("[%d/%m/%Y %H:%M:%S]")
        log.write(writeTime)
        log.write("*Imagen control: " + imagenControl + "    *Imagen Prueba: " + imagen + "\n")
        log.write("palabras en control --> ")
        
        DetectControl = detect_text(imagenControl, bucket)
        DetectPrueba = detect_text(imagen, bucket)
        estControl = []
        estPrueba = []

        log.write("palabras en Control --> ")
    
        for palabra in DetectControl:   
            p = str.lower(palabra).strip()
            estControl.append(p)
            log.write(" / " + palabra) 
        log.write("\n")

        log.write("palabras en Prueba --> ")
        for palabra in DetectPrueba: 
            p = str.lower(palabra).strip()
            estPrueba.append(p)          
            log.write(" / " + palabra) 
        log.write("\n")
        
        # Resultado final   
        print("----------------------------------------------------------------------")
        if(verificar(estPrueba,estControl)):
            print(" --- > Encontro texto")
            log.write("--- >    Verificacion: Encontro texto\n-----------------------------\n")

        else:
            print(" --- > No encontro texto")
            log.write("--- >    Verificacion: No encontro texto\n-----------------------------\n")
        print("----------------------------------------------------------------------")
        log.close()

if __name__ == "__main__":
    main()