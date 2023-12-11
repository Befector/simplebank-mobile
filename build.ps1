python -m venv beeware-venv
.\beeware-venv\Scripts\Activate.ps1
python -m pip install briefcase
briefcase create android
briefcase build android
briefcase run android