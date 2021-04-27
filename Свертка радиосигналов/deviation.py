from pylab import *
# from scipy.interpolate import interp1d
import numpy as np
from scipy.signal import chirp
import matplotlib.pyplot as plt


# указываем имена обрабатываемых S2P-файлов
UP_filename = 'sample5(UP)_after_welding.s2p' # для ДАЛЗ110В
DN_filename = 'sample6(DN)_after_welding.s2p' # для ДАЛЗ110У

N = 100001  # количество точек
t = 28E-6  # длительность импульса в мкс
f_min = 107E6  # начальная частота в МГц
f_max = 113E6  # конечная частота в МГц

# создаем ЛЧМ сигнал во временной области
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.chirp.html
time = np.linspace(0, t, N)
freq = np.linspace(f_min, f_max, N)

# создаем ЛЧМ сигнал с заданной выше длительностью и восходящим изменением (девиацией) частоты
chirp_signal_UP = chirp(time, f_min, t, f_max, method='linear')
# TODO записать в память или отдельный файл, чтобы каждый раз не генерировать заново

# создаем ЛЧМ сигнал с заданной выше длительностью и ниспадающим изменением (девиацией) частоты
chirp_signal_DN = chirp(time, f_max, t, f_min, method='linear')

# строим оба ЛЧМ сигнала на одном графике
plt.plot(time * 1E6, chirp_signal_UP)
plt.plot(time * 1E6, chirp_signal_DN)
plt.title('LFM signals')
plt.xlabel('Time, mks')
plt.ylabel('Intensity, units')
plt.show()

# читаем данные из файла для ВОСХОДЯЩИХ линий задержек
freq = []
UP_S21 = []
UP_S21_ABS = []
UP_S21_dB = []
with open(UP_filename) as data:
    for line in range(5):  # пропускаем первые пять строк файла
        next(data)
    for line in data:
        freq.append(float(line.split()[0]))  # берем значения частот из 0-го столбца
        UP_S21.append(complex(float(line.split()[3]), float(line.split()[4]))) # берем значения S21 из 3 и 4-го столбца
        UP_S21_ABS.append(abs(complex(float(line.split()[3]), float(line.split()[4])))) # складываем как комплексное число по модулю
        UP_S21_dB.append(round((20 * math.log10(abs(complex(float(line.split()[3]), float(line.split()[4]))))), 2))
print("ДАЛЗ UP в дБ:", UP_S21_dB[0:10], 'и так далее...')

# читаем данные из s2p-файла для У(ё)БЫВАЮЩИХ линий задержек
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
freq_step = span/(N-1)
print('Частотный диапазон (span) =', span * 1E-6, 'МГц', '\n'
      'Шаг изменения частоты (span/N) = ', freq_step, 'Гц')


chirp_signal_UP_freq = np.fft.fft(chirp_signal_UP)
plt.plot(abs(chirp_signal_UP_freq)) #TODO МОДУЛИ????
plt.title('---')
plt.xlabel('---')
plt.ylabel('Intensity, units')
plt.show()


chirp_signal_UP_freq_dB = []
for item in chirp_signal_UP_freq:
    chirp_signal_UP_freq_dB.append(20 * math.log10(abs(item)))
print(chirp_signal_UP_freq_dB)


result = np.array(chirp_signal_UP_freq) * np.array(DN_S21)
#TODO модули????
result_ifft = np.fft.ifft(result)

plt.plot(result_ifft)
plt.title('Compressed signal')
plt.xlabel('---')
plt.ylabel('Intensity, units')
plt.show()

# TODO построить трехмерную картинку с комплексными числами

# открываем файлы time, up, dn, в которые записываем значения из списка
# time_file = open('time.txt', 'w')
# for item in time:
#     time_file.write("%s\n" % item)
#
# UP_file = open('UP.txt', 'w')
# for item in chirp_signal_UP:
#     UP_file.write("%s\n" % item)
#
# DN_file = open('DN.txt', 'w')
# for item in chirp_signal_DN:
#     DN_file.write("%s\n" % item)

# plt.plot(time * 1E6, chirp_signal_UP)
# plt.plot(time * 1E6, chirp_signal_DN)



# TODO: частота дискретизация должна быть 2f от чего? (критерий ... Валера  знает)