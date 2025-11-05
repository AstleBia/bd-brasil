from ftplib import FTP
import os

ftp = FTP('ftp.mtps.gov.br')
ftp.login()
ftp.cwd('/pdet/microdados/')

print("Diretórios/arquivos:  ")
ftp.dir()
ftp.cwd('/pdet/microdados/RAIS/2010')
print("\n RAIS:")
ftp.dir()

arquivos = []
ftp.retrlines('NLST', arquivos.append)

print(f"encontrados {len(arquivos)} arquivos")

for arquivo in arquivos:
    pasta_rais = os.path.join('./RAIS', arquivo)
    print(f"Downloading {arquivo}...")
    try:
        with open(pasta_rais, 'wb') as f:
            ftp.retrbinary(f'RETR {arquivo}', f.write)
        print(f"✓ Downloaded {arquivo}")
    except Exception as e:
        print(f"✗ Error downloading {arquivo}: {e}")

print(f"\nAll files downloaded!")
ftp.quit()