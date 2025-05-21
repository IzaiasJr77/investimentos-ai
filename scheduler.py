import schedule
import time
from main import executar

# Agenda para 8h da manhã
schedule.every().day.at("08:00").do(executar)

while True:
    schedule.run_pending()
    time.sleep(60)
