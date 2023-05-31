# ClickerTime
Кликер, который кликает по центру экрана кадые 30 секунд + рандом на 10 секунд

Остановить программу через Ctr+C

Дополнительная информация:
создай программу на пайтон, которая каждые 30 секунд будет кликать по центру экрана

Предоставленный вами код является скриптом на языке Python, который использует библиотеку `pyautogui` для симуляции кликов мыши в центре экрана с регулярными интервалами и случайным смещением.

Вот разбор того, как работает код:

1. Импортируется библиотека `pyautogui`, которая позволяет управлять мышью и клавиатурой.

2. Импортируется модуль `time` для работы с функциями, связанными со временем.

3. Импортируется модуль `random` для генерации случайных чисел.

4. Определяется функция `click_center()`. Сначала она получает ширину и высоту экрана с помощью функции `pyautogui.size()`. Затем она вычисляет координаты центра, разделив размеры экрана на 2. В конце она использует функцию `pyautogui.click()` для симуляции клика мыши в указанных координатах центра.

5. Запускается главный цикл `while True:`, который будет повторять действие клика бесконечно.

6. Внутри цикла вызывается функция `click_center()` для выполнения клика в центре экрана.

7. Переменной `interval` присваивается значение 300 секунд (5 минут) плюс случайное целое число от -10 до 10. Это добавляет случайное смещение к интервалу между каждым кликом.

8. Вызывается функция `time.sleep(interval)`, чтобы приостановить выполнение скрипта на указанный интервал перед следующей итерацией цикла.

Этот скрипт автоматизирует процесс кликов в центре экрана с регулярными интервалами, с добавлением случайности в тайминг. Однако, пожалуйста, имейте в виду, что использование автоматизированных скриптов, подобных этому, для определенных целей может нарушать условия использования конкретных приложений или веб-сайтов. Убедитесь, что используете автоматизацию ответственно и с разрешения, когда это применимо.
