from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from pdf_build import pdf_report

# если нужна будет нелинейная интерполяция, а, например, кубическая
# from scipy.interpolate import interp1d


# from scipy.signal import chirp


# указываем имена обрабатываемых S2P-файлов
UP_filename = 'sample5(UP)_after_welding.s2p' # для ДАЛЗ110В
DN_filename = 'sample6(DN)_after_welding.s2p' # для ДАЛЗ110У

# читаем данные из файла для ВОСХОДЯЩИХ/ФОРМИРУЮЩИХ линий задержек
freq = []
UP_S21 = []
UP_S21_ABS = []
UP_S21_dB = []
with open(UP_filename) as data:
    for line in range(5): # пропускаем первые пять строк файла
        next(data)
    for line in data:
        freq.append(float(line.split()[0]))  # берем значения частот из 0-го столбца
        UP_S21.append(complex(float(line.split()[3]), float(line.split()[4]))) # берем значения S21 из 3 и 4-го столбца
        UP_S21_ABS.append(abs(complex(float(line.split()[3]), float(line.split()[4])))) # складываем как комплексное число по модулю
        UP_S21_dB.append(round((20 * math.log10(abs(complex(float(line.split()[3]), float(line.split()[4]))))), 2))
print("ДАЛЗ UP в дБ:", UP_S21_dB[0:10], 'и так далее...')

# читаем данные из s2p-файла для УБЫВАЮЩИХ/СЖИМАЮЩИХ линий задержек
DN_S21 = []
DN_S21_ABS = []
DN_S21_dB = []
with open(DN_filename) as data:
    for line in range(5):
        next(data)
    for line in data:
        DN_S21.append(complex(float(line.split()[3]), float(line.split()[4])))
        DN_S21_ABS.append(abs(complex(float(line.split()[3]), float(line.split()[4]))))
        DN_S21_dB.append(round((20 * math.log10(abs(complex(float(line.split()[3]), float(line.split()[4]))))), 2))
print("ДАЛЗ DN в дБ:", DN_S21_dB[0:10], 'и так далее...')

# определяем частотный диапазон (span) из s2p-файла
span = freq[-1] - freq[0]
print('Частотный диапазон (span) =', span * 1E-6, 'МГц')

# делаем свертку формирующего и сжимающего сигналов в частотной области как произведение комплексных чисел
result = np.array(UP_S21) * np.array(DN_S21)

# делаем обратное Фурье-преобразование из частотной во временную область, чтобы определить длительность сжатого импульса
result_ifft = np.fft.ifft(result)
# можно брать меньшее количество элементов массива
# http://old.pynsk.ru/posts/2015/Nov/09/matematika-v-python-preobrazovanie-fure/#.XFfnh2lwm7T

# переводим спектр из значений по модули в дБ
result_ifft_dB = []
for i in range(len(result_ifft)):
    result_ifft_dB.append(round((20 * math.log10(abs(result_ifft[i]))), 2))

# считаем временной шаг для данного частотного диапазона и создаем шкалу времени в наносекундах (коэф. 1E9)
time_step = round(1/span, 11) # чем больше span на R&S берем, тем мельче временной шаг, умножая его на количество точек получаем
# временной интервал, который можем измерить во времени, т.е. чем больше span, тем хуже для timedomain области
time_list = []
for i in range(len(freq)):
    time_list.append(round((time_step * i * 1E9), 2))
print("Временной шаг (1/span): ", time_step * 1E9, "нс")
print("Общее время: ", round(time_step * 1E6 * (len(freq) - 1)), "мкс") # умножаем на 1Е6, чтобы результат был в микросекундах
print("Временной лист для оси X: ", time_list[:10], "и так далее, общее количество точек:", len(time_list), "шт.")
print("Значения в dB для оси Y: ", result_ifft_dB[:10],
      "и так далее, общее количество точек:", len(result_ifft_dB), "шт.")

# находим максимум и сохраняем в памяти
maximum_dB_value = max(result_ifft_dB)
print("Максимум характеристики: ", max(result_ifft_dB), "дБ")

# находим индекс максимума характеристики
for i in range(len(result_ifft_dB)):
    if result_ifft_dB[i] == maximum_dB_value:
        maximum_dB_index = i

# делаем линейную интерполяцию на вершине пика АЧХ для точного определения длительности по заданному уровню
time_list_interp = np.linspace(time_list[maximum_dB_index - 5], time_list[maximum_dB_index + 5], num=10001)
result_ifft_dB_interp = np.interp(time_list_interp, time_list[:2000], result_ifft_dB[:2000])

# находим индекс максимуму характеристики в интерполированном ряде
maximum_dB_value_interp = max(result_ifft_dB_interp)
for i in range(len(result_ifft_dB_interp)):
    if result_ifft_dB_interp[i] == maximum_dB_value_interp:
        maximum_dB_index = i

# считаем длительность по измеренным значениям ряду по уровню -6дБ (грубая оценка)
i = 0
time_list_level_6dB = []
for item in result_ifft_dB:
    if item > maximum_dB_value - 6:
        time_list_level_6dB.append(time_list[i])
    i += 1
print("Длительность сжатого сигнала (грубо): ",
      round((time_list_level_6dB[-1] - time_list_level_6dB[0]), 2), "нс")

# считаем длительность по интерполированному ряду по уровню -6дБ (точное значение)
i = 0
time_list_level_6dB_interp = []
for item in result_ifft_dB_interp:
    if item > maximum_dB_value - 6:
        time_list_level_6dB_interp.append(time_list_interp[i])
    i += 1
print("Длительность сжатого сигнала (точно): ",
      round((time_list_level_6dB_interp[-1] - time_list_level_6dB_interp[0]), 2), "нс")

# строим результат свертки в дБ формате
# figure() # TODO зачем эта функция? =)
plt.plot(time_list[:2000], result_ifft_dB[:2000], 'o', markersize=2)
plt.plot(time_list_interp, result_ifft_dB_interp, '-')
plt.xlabel('Время, нc')
plt.ylabel('Затухание, дБ')
plt.title('Сжатый сигнал')
plt.grid(True)
plt.text(36900, maximum_dB_value + 1, maximum_dB_value)
plt.savefig('convolution.png')
plt.show()

# для использования pdf_build.py
# picture = ['test.png']
# f = pdf_report(picture, 'report', 'test_picture.pdf')