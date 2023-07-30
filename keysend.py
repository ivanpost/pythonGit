import serial
import keyboard
import serial.tools.list_ports

com_port = 'COM3'
baud_rate = 9600

ser = serial.Serial(com_port, baud_rate)
# Получение списка доступных COM портов
ports = serial.tools.list_ports.comports()

# Вывод списка портов
for port in ports:
    print(port.device)


# Функция для отправки данных в COM-порт
def send_data(data):
    ser.write(data.encode())


# Функция, вызываемая при нажатии клавиш
def on_key_press(key):
    if key.name == '2':
        send_data('B')
    elif key.name == '6':
        send_data('R')
    elif key.name == '4':
        send_data('L')
    elif key.name == '8':
        send_data('F')
    elif key.name == '7':
        send_data('G')
    elif key.name == '9':
        send_data('I')
    elif key.name == '1':
        send_data('H')
    elif key.name == '3':
        send_data('J')


# Добавляем обработчик нажатий клавиш
keyboard.on_press(on_key_press)

# Запускаем бесконечный цикл для ожидания нажатий клавиш
keyboard.wait()
