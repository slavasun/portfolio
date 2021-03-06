# Свертка линейно-частотно модулированных (ЛЧМ) радиосигналов

**Целью** данного проекта является определение ключевой характеристики изделия - длительности сжатого сигнала в наносекундах (нс). В общем случае, чем меньшую длительность имеет сжатый сигнал, тем выше пространственное разрешение (точность определения координаты объекта в пространстве) радиолокационной системы.

В итоге реализовано:
  - считывание из файлов контрольно-измерительного оборудования функциональных характеристики изделий;
  - преобразование исходных данных из комплексных чисел в децибелы (дБ);
  - свертка радиосигналов и обратное Фурье-преобразование для перехода из частотной во временную область;
  - определение максимума амплитудно-частотной характеристики, линейная интерполяция соседних точек
  - расчет длительности сжатого сигнала по заданному уровню -6 дБ
