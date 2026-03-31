name: Extraer Datos BCE
on:
  schedule:
    # Se ejecuta a las 00:00 del día 1 de cada mes
    - cron: '0 0 1 * *'
  workflow_dispatch: # Permite ejecutarlo manualmente si quieres

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Instalar dependencias
        run: pip install pandas requests
      - name: Ejecutar script
        run: python tu_script.py
