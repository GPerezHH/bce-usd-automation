import pandas as pd
import io
import requests
import zipfile
import os

def extraer_datos():
    url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip"
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    df = pd.read_csv(z.open('eurofxref-hist.csv'))

    df['Date'] = pd.to_datetime(df['Date'])
    df = df[['Date', 'USD']].dropna()
    df['weekday'] = df['Date'].dt.weekday

    # Filtrar miércoles (2) y agrupar por mes
    miercoles = df[df['weekday'] == 2].copy()
    miercoles['year'] = miercoles['Date'].dt.year
    miercoles['month'] = miercoles['Date'].dt.month

    # Obtener el penúltimo de cada mes
    resultado = miercoles.sort_values('Date').groupby(['year', 'month']).nth(-2)

    # Guardar a un archivo CSV
    resultado[['Date', 'USD']].to_csv("historico_usd.csv", index=False)
    print("Archivo actualizado con éxito.")

if __name__ == "__main__":
    extraer_datos()
