import json
import sys
import os

#script per pulire le annotation 'widgets' nei notebook di colab perchè questi quando vengono caricati su GitHub vanno in errore.
#Basta posizionare lo script nella cartella root del progetto che si vuole fixare e andrà a modificare anche i file .ipynb nelle sottocartelle
def fix_notebook(file_list):
    notebooks = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if file_list is None:
        print("Errore: nessun file specificato. Procedo con la fix di tutti i notebook nella cartella corrente.")
        for root, dirs, files in os.walk(script_dir):
            
            # Opzionale: Salta la cartella nascosta dei checkpoint di Jupyter
            if '.ipynb_checkpoints' in root:
                continue
            for file in files:
                print(file)
                if file.endswith('.ipynb'):
                    full_path = os.path.join(root, file)
                    notebooks.append(full_path)
    else:
        print(f"📂 Ricevuti {len(file_list)} file specifici da elaborare.")
        for filename in file_list:
            # Gestione intelligente del percorso:
            # Se il file esiste dove ho lanciato il comando, bene.
            if os.path.exists(filename):
                notebooks.append(filename)
            # Altrimenti provo a cercarlo nella cartella dello script
            elif os.path.exists(os.path.join(script_dir, filename)):
                notebooks.append(os.path.join(script_dir, filename))
            else:
                print(f"⚠️ Attenzione: Il file '{filename}' non è stato trovato.")

    print(f"--- Inizio pulizia su {len(notebooks)} file ---\n")

    for filename in notebooks:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Rimuove la sezione widgets dai metadati se presente
        if 'widgets' in data.get('metadata', {}):
            del data['metadata']['widgets']
            print(f"Riparato: {filename}")
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=1)
        else:
            print(f"Nessun widget trovato in: {filename}")

# Esegui passando il nome del file, es: python fix_nb.py mio_notebook.ipynb
if __name__ == "__main__":
    try:
        fix_notebook(sys.argv[1])
    except IndexError:
        fix_notebook(None)

