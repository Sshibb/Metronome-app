import time
import sys

def metronome(bpm):
    # Интервал между ударами в секундах
    interval = 60.0 / bpm
    print(f"Метроном запущен на {bpm} BPM. Нажмите Ctrl+C для выхода.")
    
    try:
        while True:
            # Символьный удар (можно заменить на системный звук \a)
            sys.stdout.write("• TICK \n")
            sys.stdout.flush()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nМетроном остановлен.")

# Запуск со скоростью 100 ударов в минуту
metronome(100)
