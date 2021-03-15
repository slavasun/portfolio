Данный файл содержит краткое описание, выполненных рабочих и учебных проектов. Для более детального ознакомления с проектом просто кликни на его название :point_down:.  
А если хочешь предложить сотрудничество или нужна помощь :point_right: [смело пиши мне в LinkedIn](http://www.linkedin.com/in/slavasun).

  
<table>
    <tr>
        <td width="5" align="center"> <b> № </b> </td>
        <td align="center"> <b> Название проекта и решённые задачи </b> </td>
        <td align="center"> <b> Ключевые инструменты </b> </td>
        <td align="center"> <b> Использованы библиотеки </b> </td>
    </tr>
    <tr>
        <td colspan="4"> <b> Рабочие (микроэлектроника) </b> </td>
    </tr>
    <tr>
        <td> 1 </td>
        <td> <a href="empty_now"> Обработка результатов измерений беспроводных датчиков радиоидентификации </a> 
     <br> Для снижения трудозатрат разработан пайплайн, который сначала считывает данные с измерительного оборудования, проводит разметку датчиков годные/бракованные, строит ключевые распределения и выводить сводный pdf-отчет.  </td>
        <td> "тепловая карта", статистическая обработка</td>
        <td> Pandas, Numpy, Seaborn, SciPy, LaTeX </td>
    </tr>
    <tr>
        <td> 2 </td>
        <td> <a href="empty_now"> Математическая свертка радиосигналов </a> 
      <br> В данном проекте сначала считываем данные из лог-файлов измеретельного оборудования, затем преобразуем данные из формата комплексных чисел в дБ, затем проводим свертку сигналов во частотной области и с помощью обратного Фурье-преобразования переходим во временную область. Интерполируя временную область с пиковыми значениями рассчитываем функционал изделия. </td>
        <td> предобработка данных, Фурье-преобразование, интерполяция </td>
        <td> Pandas, Numpy, Seaborn, Pylab</td>
    </tr> 
    <tr>
        <td colspan="4"> <b> Яндекс.Практикум </b> </td>
    </tr> 
    <tr>
        <td> 3 </td>
        <td> <a href="empty_now"> Отток клиентов банка </a> 
    <br> По данным о клиенте банка построил модель, позволяющую спрогнозировать вероятность, уйдет ли клиент из банка в ближайшее время. При этом применил различные методы для корректной работы с исходными данными, в которых есть существенный дисбаланс классов. </td>
        <td> DecisionTreeClassifier, RandomForestClassifier, 
          br> F1-score, ROC-AUC score, 
          <br> Upsampling, Downsampling </td>
        <td> Pandas, Numpy, Sklearn,  </td>
    </tr>
    <tr>
        <td> 4 </td>
        <td> <a href="empty_now"> Выбор региона для разработки новых нефтяных месторождений </a> 
    <br> По данным о запасах и качества нефти в трёх регионах построил модель для предсказания объёма запасов в новых скважинах. С помощью техники Bootstrap для регионов, в которых находятся скважины с самыми высокими оценками значений, проанализировал возможную прибыль и риски.</td>
        <td> LinearRegression, Bootstrap </td>
        <td> Pandas, Numpy, Matplotlib, Sklearn, SciPy </td>
    </tr>
    <tr>
        <td> 5 </td>
        <td> <a href="empty_now"> Подготовка модели для металлообрабатывающего предприятия </a> 
    <br> По данным о параметрах технологического процесса восстановления золота построил модель, предсказывающую коэффициент восстановления золота из золотосодержащей руды. Модель позволяет оптимизировать производство так, чтобы не запускать предприятие с убыточными характеристиками. </td>
        <td> RandomizedSearchCV, GridSearchCV, sMAPE-score </td>
        <td> Pandas, Seaborn, Sklearn </td>
    </tr>
    <tr>
        <td> 6 </td>
        <td> <a href="empty_now"> Предсказание цены автомобиля </a> 
    <br> По данным из объявления о продаже автомобиля с пробегом разработал модель, позволяющую быстро узнать рыночную стоимость своего автомобиля. Проанализировал такие факторы как технические характеристики, комплектации и цены автомобилей. Определил степень значимости каждого фактора, выявил те, которые наиболее существенно влияют на цену. </td>
        <td> OneHotEncoder, StandardScaler </td>
        <td> Pandas, Sklearn, RandomForestRegressor, LightGBM, CatBoost </td>
    </tr>
  <tr>
        <td> 7 </td>
        <td> <a href="empty_now"> Прогнозирование заказов такси </a> 
    <br> Проанализировал исторические данные о заказах такси  (временные ряды). Спрогнозировал количество заказов такси на следующий час, чтобы привлекать больше водителей в период пиковой нагрузки. Построил модель для такого предсказания. </td>
        <td> RMSE-score </td>
        <td> Pandas, Sklearn, LightGBM, CatBoostRegressor </td>
    </tr>
  <tr>
        <td> 8 </td>
        <td> <a href="empty_now"> Классификация комментариев </a> 
    <br> Для интернет-магазина разработал инструмент, который будет искать токсичные комментарии и отправлять их на модерацию. Обучил модель позволяющую классифицировать комментарии на позитивные и негативные. </td>
        <td> NLP, векторизация текстов word2vec, N-граммы </td>
        <td> Pandas, Sklearn, NLTK </td>
    </tr>
  <tr>
        <td> 9 </td>
        <td> <a href="empty_now"> Определение возраста по фото </a> 
    <br> Разработал модель, которая по фотографии покупателя в прикассовой зоне определит его приблизительный возраст. Супермаркету это необходимо, чтобы внедрить систему контроля кассиров при продаже алкоголя, а также для анализа покупок покупателями данной возрастной группы. Система компьютерного зрения разработана на основе best practice в архитектурах нейронных сетей. </td>
        <td> neural networks, ResNet </td>
        <td> Pandas, Numpy, Matplotlib, seaborn, Keras </td>
    </tr>
    <tr>
        <td> 10 </td>
        <td> <a href="empty_now"> Определение выгодного тарифа телеком-компании </a> 
    <br> Подготовлен сводный годовой отчет с разбивкой по месяцам, рассчитана суммарная выручка, полученная от пользователей тарифа "Смарт" и "Ультра". Проведена статистическая проверка гипотез. </td>
        <td> Проверка гипотез, когортный анализ td>
        <td> Pandas, Numpy, Scipy, Seaborn, Matplotlib </td>
    </tr>
    <tr>
        <td> 11 </td>
        <td><a href="empty_now"> Анализ параметров объектов Яндекс.Недвижимости </a> 
    <br> Определено влияние на стоимость квадратного метра таких параметров как расстояние до центра Санкт-Петербурга, количество комнат, площадь кухни, высота потолков, этажность</td>
        <td>in_progress</td>
        <td>Pandas, Scipy, Seaborn, Matplotlib</td>
    </tr>
    <tr>
        <td> 12 </td>
        <td><a href="empty_now"> Определение факторов влияющих на платежеспособность клиентов банка </a>
      Определены признаки самых рискованных и наиболее надёжных заемщиков, влияющих на уровень просрочки по платежам. <b>Проведена лемматизация</b> целей кредита с последующей категоризацией заёмщиков по цели кредита</td>
        <td>in_progress</td>
        <td>Pandas, Numpy, PyMystem3, Collections</td>
    </tr>
    <tr>
        <td> 13 </td>
        <td><a href="empty_now"> Формирование типичных портретов клиентов фитнес-центра для минимизации оттока </a>
      С помощью методов машинного обучения проведен анализ анкет пользователей фитнес-центра, составлены портреты типичных групп клиентов. Определены показатели, указывающие на то, что клиент собирается перестать пользоваться услугами центра</td>
        <td>in_progress</td>
        <td>Pandas, Numpy, Matplotlib, Seaborn, Sklearn, Scipy</td>
    </tr>
    <tr>
        <td colspan="4"><b> СберУниверситет </b><b> </b></td>
    </tr>
    <tr>
        <td>14</td>
        <td><a href="empty_now"> Изучение закономерностей, определяющих успешность игр для интернет-магазина </a> 
      Определены факторы, определяющие успешность игры на рыке, проверены гипотезы о различии пользовательского рейтинга между жанрами</td>
        <td>in_progress</td>
        <td>Pandas, Numpy, Scipy, Seaborn, Matplotlib</td>
    </tr>
    <tr>
        <td>15</td>
        <td><a href="empty_now"> Проверка гипотезы о повышении спроса на авиабилеты во время фестивалей </a>
      Данные о перелетах и фестивалях собраны <b>с помощью парсера и SQL-запросов</b>. По полученным данным проанализирован спрос пассажиров на рейсы в города, где проходят крупнейшие фестивали. Проверена гипотеза, что количество рейсов во время фестивалей увеличивается </td>
        <td>in_progress</td>
        <td>requests, bs4, SQL, Pandas, Matplotlib, Seaborn</td>
    </tr>
    <tr>
        <td colspan="4"><b> Дополнительные, но полезные)</b></td>
    </tr>
    <tr>
        <td>16</td>
        <td><a href="empty_now"> Оптимизация маркетинговых затрат в Яндекс.Афише </a>
      Рассчитаны ключевые метрики LTV, CAC, ROI по маркетинговым затратам, проведен когортный анализ, выявлены нерентабельные направления рекламы и те, которые окупились </td>
        <td>in_progress</td>
        <td>Pandas, Numpy, Matplotlib, Seaborn</td>
    </tr>
    <tr>
        <td>17</td>
        <td><a href="empty_now"> Проверка гипотез для увеличения выручки в интернет-магазине, оценка результатов A/B-теста </a> Проведен анализ A/B-теста, данные очищены от выбросов, существенно искажавших результат, проверены гипотезы о различии среднего чека заказа и конверсии между А и В группами</td>
        <td>in_progress</td>
        <td>Pandas, Numpy, Matplotlib, Scipy, ICE, RICE</td>
    </tr>
    <tr>
        <td>18</td>
        <td><a href="empty_now"> Исследование рынка общественного питания в Москве </a> Определены характерные особенности рынка общественного питания, выявлены самые насыщенные объектами улицы, а также распределение объектов по типу, имеющих сетевое распространение </td>
        <td>in_progress</td>
        <td>Pandas, Numpy, Matplotlib, Seaborn, Plotly, tqdm</td>
    </tr>
    <tr>
        <td>19</td>
        <td><a href="empty_now"> Анализ пользовательского поведения в мобильном приложении </a> Определена воронка событий в приложении, доли пользователей для каждого этапа конверсии, проведены A/A/B-эксперименты, с поправкой Бонферрони проверены гипотезы о различии долей</td>
        <td>in_progress</td>
        <td>Pandas, Numpy, Scipy, Matplotlib, Seaborn, Plotly, Math</td>
    </tr>
    <tr>
        <td>20</td>
        <td><a href="empty_now"> Создание дашборда по пользовательским событиям для агрегатора Новостей </a> Разработан пайплайн для автоматизации задач сбора и трансформации данных, разработан дашборд по заданному техническому заданию</td>
        <td>in_progress</td>
        <td>Pandas, SQLalchemy, datetime, dash, Tableau</td>
    </tr>
</table>
