$ErrorActionPreference = "Stop"

if (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCommand = "py -3.14"
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCommand = "python"
} else {
    throw "Python nao encontrado. Instale o Python em https://www.python.org/downloads/"
}

Invoke-Expression "$pythonCommand -m venv .venv"
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\pip.exe install -r requirements.txt
.\.venv\Scripts\python.exe scripts\create_sample_excel.py
Write-Host "Projeto configurado com sucesso. Execute: .\.venv\Scripts\python.exe -m app.main"
