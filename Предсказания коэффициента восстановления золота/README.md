# Разработка прототипа модели, предсказывающей коэффициент восстановления золота из золотосодержащей руды

**Цель** - разработать прототип модели для оптимизации производства, чтобы не запускать предприятие с убыточными характеристиками.

**Задачи**:

  - Модель должна предсказать коэффициент восстановления золота из золотосодержащей руды. В  распоряжении данные с параметрами добычи и очистки.
  - Для прогноза коэффициента нужно найти долю золота в концентратах и хвостах. Причём важен не только финальный продукт, но и черновой концентрат.
  - Прогнозируются сразу две величины:
    - эффективность обогащения чернового концентрата rougher.output.recovery;
    - эффективность обогащения финального концентрата final.output.recovery

В работе применены кастомная метрика sMAPE, простая линейная регрессия, регрессии с Lasso и Ridge регуляризацией, модель на основе алгоритма случайного леса.  
Наилучший результат продемонстрировала модель с простой линейной регуляризацией, при её проверке на тестовой выборке sMAPE=10.39%.

