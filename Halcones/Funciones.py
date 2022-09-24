import fitz #librería pymupdf
import rasterio #librería para leer archivos raster
import numpy as np



def leer_pdf(path):
    try:
        with fitz.open(path) as file:
            text = ''
            for page in file:
                text += page.getText()
        print(text)
    except:
        pass
    
    def leer_raster(path):
        try:
            with rasterio.open(path) as file:
                print(file.profile)
        except:
            pass
    

        
    
    
    
    
    