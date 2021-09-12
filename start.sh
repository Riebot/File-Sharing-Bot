echo "[INFO] - FETCHING UPSTREAM REPO ..."
git clone https://github.com/ZauteKm/File-Sharing-Bot.git /File-Sharing-Bot
cd /File-Sharing-Bot
echo "[INFO] - INSTALLING REQUIREMENTS ..."
pip3 install -r requirements.txt
echo "[INFO] - STARTING FILE-SHARING-BOT ..."
python3 main.py
