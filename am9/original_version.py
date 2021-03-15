import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as mpath
from math import sqrt

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

zondreport = open('zondreport.txt') #Читаем файл зондового контроля
stepperreport = open('stepper.txt') #Читаем файл степпера

# Объявляем переменные
data = []
data_stepper = []
i = 0
j = 0
k = []
l = []

# Назначаем переменные
sl = 'm9-21-G1'  # Номер сопроводительного листа
wafer_di_inch = 4  # Диаметр подложки в дюймах
# Определяем размер базового среза на пластине
if wafer_di_inch == 4:
        wafer_di = 100000  # Диаметр пластины в мкм
        wafer_cut = 32500  # Размер базового среза пластины в мкм
elif wafer_di_inch == 3:
        wafer_di = 76200  # Диаметр пластины в мкм
        wafer_cut = 22000  # Размер базового среза пластины в мкм


scale = 1.5  # Задаем размер метки в мкм
metka_size_x = 970  # Ширина метки
metka_size_y = 6420  # Высота метки
metka_size_x = metka_size_x/scale
metka_size_y = metka_size_y/scale

# Объявляем класс Metka с атрибутами в последовательности столбцов читаемого файла
class Metka: 
    def __init__(self, number, tau1, tau2, tau3, a1, a2, a3, ta1, ta2, ta3, ta4, ta5, ta6, ta7, ta8,\
                 ta9, ta10, ta11, ta12, aa1, aa2, aa3, aa4, aa5, aa6, aa7, aa8, aa9, aa10, aa11, aa12,\
                 f1, f2, f3, a1centr, a2centr, a3centr, bw1, bw2, bw3, id_detected, delta_a, phase21, phase31,\
                 phase3121, tau21, tau31, tau3121, number_st, number_st2, x, y, z1, z2, z3, temp0, p0, temp1, temp2, temp3):
        self.number=number
        self.tau1=tau1
        self.tau2=tau2
        self.tau3=tau3
        self.a1=a1
        self.a2=a2
        self.a3=a3
        self.ta1=ta1
        self.ta1=ta2
        self.ta1=ta3
        self.ta1=ta4
        self.ta1=ta5
        self.ta1=ta6
        self.ta1=ta7
        self.ta1=ta8
        self.ta1=ta9
        self.ta1=ta10
        self.ta1=ta11
        self.ta1=ta12
        self.aa1=aa1
        self.aa2=aa2
        self.aa3=aa3
        self.aa4=aa4
        self.aa5=aa5
        self.aa6=aa6
        self.aa7=aa7
        self.aa8=aa8
        self.aa9=aa9
        self.aa10=aa10
        self.aa11=aa11
        self.aa12=aa12
        self.f1=f1
        self.f2=f2
        self.f3=f3
        self.bw1=bw1
        self.bw2=bw2
        self.bw3=bw3
        self.a1centr=a1centr
        self.a2centr=a2centr
        self.a3centr=a3centr
        self.id_detected=id_detected
        self.delta_a=delta_a
        self.phase21=phase21
        self.phase31=phase31
        self.phase3121=phase3121
        self.tau21=tau21
        self.tau31=tau31
        self.tau3121=tau3121
        self.number_st=number_st
        self.number_st2=number_st2
        self.x=x
        self.y=y
        self.z1=z1
        self.z2=z2
        self.z3=z3
        self.temp0=temp0
        self.p0=p0
        self.temp1=temp1
        self.temp2=temp2
        self.temp3=temp3

# Создаем массив из данных степпера
def read_stepper_report(k):
        i=0
        data_stepper=[]
        for line in stepperreport:
                i=i+1        
                if i==k:
                        pureline=line.rstrip(' | \n').lstrip('| ')  # Очищаем конец и начало строки от лишних символов
                        var = list(pureline.split('|'))  # Создаем список из данных разделенных 'Tab'
                        var[-1] = var[-1].split('°')[0]  # Убираем значок градуса в последнем элементе списка
                        # (делим его на две части по символу ° и забираем только левую часть получившегося списка)
                        var[-2] = var[-2].split('°')[0]  # Аналогично для предпоследнего столбца
                        var[-3] = var[-3].split('°')[0]  # Аналогично для третьего с конца столбца
                        var[-5] = var[-5].split('°')[0]  # Аналогично для пятой с конца столбца
                        var2 = list(map(float, var))  # Меняем тип данных на данные с плавающей точкой
                        i = 0
                        data_stepper = data_stepper + [var2]  # Включаем metka(i) в базу данных всех меток
        return data_stepper
data_stepper = read_stepper_report(4)

print("ДАННЫЕ СО СТЕППЕРА:", data_stepper)


# Создаем массив из данных зондовой станции
for line in zondreport:
    pureline = line.rstrip('\n')  # Читаем строку и удаляем возврат каретки в ее конце
    var = list(map(float, pureline.split('\t')))  # Создаем список из данных разделенных 'Tab'
    var2 = Metka(number=var[0], tau1=var[1], tau2=var[2], tau3=var[3], a1=var[4], a2=var[5], a3=var[6], ta1=var[7],
               ta2=var[8], ta3=var[9], ta4=var[10], ta5=var[11], ta6=var[12], ta7=var[13], ta8=var[14],
               ta9=var[15], ta10=var[16], ta11=var[17], ta12=var[18], aa1=var[19], aa2=var[20], aa3=var[21],
               aa4=var[22], aa5=var[23], aa6=var[24], aa7=var[25], aa8=var[26], aa9=var[27], aa10=var[28],
               aa11=var[29], aa12=var[30], f1=var[31], f2=var[32], f3=var[33], a1centr=var[34], a2centr=var[35],
               a3centr=var[36], bw1=var[37], bw2=var[38], bw3=var[39], id_detected=var[40], delta_a=var[41],
               phase21=var[42], phase31=var[43], phase3121=var[44], tau21=var[45], tau31=var[46], tau3121=var[47],
               number_st=data_stepper[int(var[0]-1)][0],
               number_st2=data_stepper[int(var[0]-1)][1], x=data_stepper[int(var[0]-1)][2], y=data_stepper[int(var[0]-1)][3],
               z1=data_stepper[int(var[0]-1)][4], z2=data_stepper[int(var[0]-1)][5], z3=data_stepper[int(var[0]-1)][6],
               temp0=data_stepper[int(var[0]-1)][7], p0=data_stepper[int(var[0]-1)][8], temp1=data_stepper[int(var[0]-1)][9],
               temp2=data_stepper[int(var[0]-1)][10], temp3=data_stepper[int(var[0]-1)][11])
    data = data + [var2]  # Включаем metka(i) в базу данных всех меток

# Считаем годные метки
# pdf = [('Номер','ID','A1','A2','A3',)]
selected_data = [('#',' ID', 'τ1, ns', 'τ2, ns', 'τ3, ns', 'A1, dB', 'A2, dB', 'A3, dB', 'ΔA, dB', '$α_{sr}$, dB')]

def goodmetka(metka_a123):
        kgd=[]
        kbd=[]
        common_data=[]
        temp0=[]
        temp1=[]
        temp2=[]
        temp3=[]
        phase3121=[]
        number=[]
        x=[]
        y=[]
        z=[]
        x1=[]
        y1=[]
        z1=[]
        z3=[]
        phase_group = 0
        phase_group_color = 0
        phase_group_palette = ['red', 'orange', 'gold', 'lawngreen', 'lightblue', 'blue', 'violet', 'sandybrown',
                               'wheat', 'sienna', 'khaki', 'hotpink']
        # phase_group_palette = ['red','red' ,'red','red','red','blue','violet','red','red','red','red','red']
        for metka in data:  # Формируем массивы из data требуемых параметров для ВСЕХ меток
            temp0 = temp0 + [metka.temp0]
            temp1 = temp1 + [metka.temp1]
            temp2 = temp2 + [metka.temp2]
            temp3 = temp3 + [metka.temp3]
            z3 = z3 + [metka.z3]
            number = number + [metka.number]
            common_data.append([number, temp0, temp1, temp2, temp3, z3])
            if metka.id_detected != 0:  # Формируем массивы из data для "ЗВУЧАЩИХ" меток
                    phase3121 = phase3121 + [metka.phase3121]
            # Формируем массивы из data для ГОДНЫХ меток (критерии годности)
            if (max(metka.a1, metka.a2, metka.a3) <= metka_a123)\
               & (max(metka.bw1, metka.bw2, metka.bw3) >= 95000000)\
               & ((max(metka.a1, metka.a2, metka.a3)-min(metka.a1, metka.a2, metka.a3)) <= 5) \
               & ((metka.f1 >= 2455000000) & (metka.f1 <= 2462000000))\
               & ((metka.f2 >= 2453000000) & (metka.f2 <= 2460000000))\
               & ((metka.f3 >= 2451000000) & (metka.f3 <= 2461000000))\
               & (min(metka.aa1, metka.aa2, metka.aa3, metka.aa4, metka.aa5, metka.aa6, metka.aa7, metka.aa8,
                      metka.aa9, metka.aa10, metka.aa11, metka.aa12)*(-1)-max(metka.a1, metka.a2, metka.a3) > 10):
               x = x + [metka.x*(-1)]
               y = y + [metka.y*(-1)]
               phase_group = round((metka.phase3121/30), 0)
               phase_group_color = phase_group_palette[int(phase_group)]
               z = z + [phase_group_color]
               metka_delta_a = (max(metka.a1, metka.a2, metka.a3)-min(metka.a1, metka.a2, metka.a3))
               metka_alfa_sr = (min(metka.aa1, metka.aa2, metka.aa3, metka.aa4, metka.aa5, metka.aa6, metka.aa7,
                                metka.aa8, metka.aa9, metka.aa10, metka.aa11, metka.aa12)*(-1)-max(metka.a1, metka.a2, metka.a3))
               selected_metka = [int(metka.number), int(metka.id_detected), round(metka.tau1*1000000000, 2),
                                 round(metka.tau2*1000000000, 2), round(metka.tau3*1000000000, 2), round(metka.a1,2),
                                 round(metka.a2,2), round(metka.a3,2), round (metka_delta_a,2), round(metka_alfa_sr,2)]
               selected_data.append(selected_metka)
               kgd.append([x,y,z])
            else:  # Формируем массивы из data для БРАКОВАННЫХ меток
                x1 = x1 + [metka.x * (-1)]
                y1 = y1 + [metka.y * (-1)]
                z1 = z1 + ['white']
                kbd.append([x1,y1,z1])
        
        if len(common_data)-len(kgd)-len(kbd) != 0:
                print ('ERROR DATA')
        else:
                print ('CHIP DATA IS OK')
        return kgd, kbd, common_data, phase3121

amax = 35
metka_info = goodmetka(amax)


known_good_die = metka_info[0]
print('Годные: ', known_good_die[0:2])
known_bad_die = metka_info[1]
print('Бракованные: ', known_bad_die[0:2])
common_data = metka_info[2]

j = (len(known_good_die))
x = known_good_die[0]
y = known_good_die[1]
z = known_good_die[2]
x1 = known_bad_die[0]
y1 = known_bad_die[1]
z1 = known_bad_die[2]
phase3121 = metka_info[3]
print('Фаза:', phase3121[0:5])
z3 = common_data[5]
number = common_data[0]
temp0 = common_data[1]
temp1 = common_data[2]
temp2 = common_data[3]
temp3 = common_data[4]
print(x)
print(y, len(y))

##################### Рисуем график #################################################
    
################### Создаем маркер #############
shape_description = [
(-1*metka_size_x*0.5, -1*metka_size_y*0.5, mpath.Path.MOVETO),
(-1*metka_size_x*0.5, metka_size_y*0.5, mpath.Path.LINETO),
(metka_size_x*0.5, metka_size_y*0.5, mpath.Path.LINETO),
(metka_size_x*0.5, -1*metka_size_y*0.5, mpath.Path.LINETO),
(0., 0., mpath.Path.CLOSEPOLY),
]
u, v, codes = zip(*shape_description)
my_marker = mpath.Path(np.asarray((u, v)).T, codes)
#################################################
fig = plt.figure()   # Создание объекта Figure
#ax1 = fig.add_subplot(131)
#ax2 = fig.add_subplot(132)
#ax3 = fig.add_subplot(133)
cut_x = (-1*(wafer_cut/2))
cut_y = (-1*(sqrt(pow(wafer_di/2,2)+ pow(wafer_cut/2,2))))
shadow_width=250
plt.gca().add_patch(plt.Circle((0, 0), radius = (wafer_di/2+shadow_width), color = 'gray', alpha=0.15)) #Рисуем каемку пластины     
plt.gca().add_patch(plt.Circle((0, 0), radius = (wafer_di/2), color = '.75', alpha=0.1)) #Рисуем пластину
shape1 = patches.Rectangle(((cut_x), (cut_y)), wafer_cut, 5000,  color = '.75', alpha=0.15) 
shape = patches.Rectangle(((cut_x), (cut_y)), wafer_cut, 5000, color = 'white')
plt.gca().add_patch(shape1) 
plt.gca().add_patch(shape)
plt.scatter(x, y, c=z, marker=my_marker, s=(metka_size_x/2), linewidth=0)   #Рисуем годные метки
plt.scatter(x1, y1, c='white', marker=my_marker, s=(metka_size_x/2), linewidth=0) #Рисуем бракованные метки
plt.axis('scaled', color='white')
#plt.axes()
#plt.title('Wafer #'+str(sl)+'\n'+'Dies-'+str(j)+'pcs.\n'+'Yield-'+str(round((j/len(common_data)*100),2))+'%')
plt.savefig('fig1.png', dpi=300)
fig = plt.figure() 
plt.hist(phase3121, bins = 36)
plt.savefig('fig2.png')
fig = plt.figure() 
plt.plot(number, temp0, c='red')
plt.plot(number, temp1, c='blue')
plt.plot(number, temp2, c='green')
plt.plot(number, temp3, c='orange')
plt.savefig('fig3.png')
#plt.plot_surface(x, y, j, cmap=cm.gray)
#plt.show()
#fig.show()
#im = plt.imshow(z3, cmap='hot')
#plt.colorbar(im, orientation='horizontal')
#plt.show()
####################################################################################

############################# PDF ##################################################

doc = SimpleDocTemplate("test_report_lab.pdf", pagesize=letter, rightMargin=20,leftMargin=30, topMargin=20,bottomMargin=20)
elements=[]
style = TableStyle([('ALIGN',(0,0),(-1,-1),'RIGHT'), #Выравниваем по правому краю
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black), #Рисуем внутреннюю сетку
                       ('BOX', (0,0), (-1,-1), 0.5, colors.black), #Рисуем наружную рамку
                       ('BACKGROUND', (0,0), (-1,0), colors.orange), #Делаем заливку
                       #('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                       #('VALIGN',(0,0),(0,-1),'TOP'),
                       #('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                       ('ALIGN',(0,0),(-1,0),'CENTER'),
                       #('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                       #('TEXTCOLOR',(0,-1),(-1,-1),colors.green)  
                       ])
#Configure style and word wrap
#s = getSampleStyleSheet()
#s = s["BodyText"]
#s.wordWrap = 'CJK'
#selected_data = [[Paragraph(cell, s) for cell in row] for row in selected_data]
t=Table(selected_data)
t.setStyle(style)
#t._argW[1]=150

elements.append(t)
doc.build(elements)

