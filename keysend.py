import serial
import keyboard

com_port = 'COM5'
baud_rate = 9600

ser = serial.Serial(com_port, baud_rate)


# Функция для отправки данных в COM-порт
def send_data(data):
    ser.write(data.encode())


# Функция, вызываемая при нажатии клавиш
def on_key_press(key):
    if key.name == 'b':
        send_data('B')
    elif key.name == 'R':
        send_data('R')
    elif key.name == 'L':
        send_data('L')
    elif key.name == 'F':
        send_data('F')
    elif key.name == 'G':
        send_data('G')
    elif key.name == 'I':
        send_data('I')
    elif key.name == 'H':
        send_data('H')
    elif key.name == 'J':
        send_data('J')


# Добавляем обработчик нажатий клавиш
keyboard.on_press(on_key_press)

# Запускаем бесконечный цикл для ожидания нажатий клавиш
keyboard.wait()
