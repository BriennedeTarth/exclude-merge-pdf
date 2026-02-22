from PyPDF2 import PdfMerger 
from datetime import datetime
import glob 
import os
import time


#selecciona todos los archivos con extension.pdf 

pdfs=glob.glob('./*.pdf') 

#fecha actual en formato ddmmyyyy
current_date = datetime.now().strftime("%d%m%Y")
output_filename = f"mergedPDF-{current_date}.pdf"
#si ya existe borra primero para que no se haga append
#if os.path.exists(output_filename):
#    os.remove(output_filename)

merger = PdfMerger() 

# Ensure the output directory exists
#output_dir = os.path.dirname(output_filename)
#if output_dir and not os.path.exists(output_dir):
#os.makedirs(output_dir)
# If the output file already exists, delete it before starting the merge
#if os.path.exists(output_filename):
#    try:
#        os.remove(output_filename)
#    except PermissionError:
#        print(f"Could not delete {output_filename}. It might be open in another program.")
#if output_dir and not os.path.exists(output_dir):

#if not os.path.exists(output_filename):
#    with open(output_filename, 'w') as f:
#        pass  # Just create an empty file


for pdf in pdfs:
    #solo hacer append si no tienen la palabra clave
    filename = os.path.basename(pdf)
    if not filename.startswith('EXCLUIR-'): 
        merger.append(pdf) 



merger.write(output_filename)
#merger.write("mergedPDF.pdf") 
merger.close() 