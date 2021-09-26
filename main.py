import struct
from typing import List, Any

import requests
from bs4 import BeautifulSoup
from random import choice
from array import *
import re

desktop_agents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']


class tch:  # преподаватель
    name = "-"
    dgre = "-"  # ученая степень/должность
    email = "-"


class dpt:  # департамент/кафедра
    name = "-"
    url = "-"
    teachList = [tch()]  # список преподавателей, который будет заполняться


class sch:  # школа
    name = "-"
    dptList = []  # список департаментов/кафедр


def random_headers():
    return {'User-Agent': choice(desktop_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}


schools = [sch() for i in range(8)]  # список школ, которые надо найти
schools[0].name = "Политехнический институт"
schools[0].dptList = [dpt() for i in range(11)]
schools[0].dptList[0].name = "Департамент архитектуры и дизайна"
schools[0].dptList[
    0].url = "https://www.dvfu.ru/schools/engineering/structure/departments/departament-arkhitektury-i-dizayna/prepodavateli-i-sotrudniki/"
schools[0].dptList[1].name = "Департамент геоинформационных технологий"
schools[0].dptList[
    1].url = "https://www.dvfu.ru/schools/engineering/structure/departments/departament-geoinformatsionnykh-tekhnologiy/prepodavateli-i-sotrudniki/"
schools[0].dptList[2].name = "Департамент инноваций"
schools[0].dptList[
    2].url = "https://www.dvfu.ru/schools/engineering/structure/departments/departament-innovatsiy/prepodavateli-i-sotrudniki/"
schools[0].dptList[3].name = "Департамент морской техники и транспорта"
schools[0].dptList[
    3].url = "https://www.dvfu.ru/schools/engineering/structure/departments/departament-morskoy-tekhniki-i-transporta/prepodavateli-i-sotrudniki/"
schools[0].dptList[4].name = "Департамент нефтегазовых технологий"
schools[0].dptList[
    4].url = "https://www.dvfu.ru/schools/engineering/structure/departments/departament-neftegazovykh-tekhnologiy/prepodavateli-i-sotrudniki/"
schools[0].dptList[5].name = "Департамент электроники, телекоммуникации и приборостроения"
schools[0].dptList[
    5].url = "https://www.dvfu.ru/schools/engineering/structure/departments/departament-elektroniki-telekommunikatsii-i-priborostroeniya/prepodavateli-i-sotrudniki/"
schools[0].dptList[6].name = "Департамент энергетических систем"
schools[0].dptList[
    6].url = "https://www.dvfu.ru/schools/engineering/structure/departments/departament-energeticheskikh-sistem/prepodavateli-i-sotrudniki/"
schools[0].dptList[7].name = "Инженерно-строительное отделение"
schools[0].dptList[
    7].url = "https://www.dvfu.ru/schools/engineering/structure/departments/inzhenernyy-departament/inzhenerno-stroitelnoe-otdelenie/prepodavateli-i-sotrudniki/"
schools[0].dptList[8].name = "Отделение машиностроения, морской техники и транспорта"
schools[0].dptList[
    8].url = "https://www.dvfu.ru/schools/engineering/structure/departments/inzhenernyy-departament/otdelenie-mashinostroeniya-morskoy-tekhniki-i-transporta/prepodavateli-i-sotrudniki/"
schools[0].dptList[9].name = "Отделение горного и нефтегазового дела"
schools[0].dptList[
    9].url = "https://www.dvfu.ru/schools/engineering/structure/departments/inzhenernyy-departament/otdelenie-neftegazovogo-dela-i-gornogo-dela/prepodavateli-i-sotrudniki/"
schools[0].dptList[10].name = "Отделение энергетики и ресурсосбержения"
schools[0].dptList[
    10].url = "https://www.dvfu.ru/schools/engineering/structure/departments/inzhenernyy-departament/otdelenie-energetiki-i-resursosberzheniya/prepodavateli-i-sotrudniki/"

schools[1].name = "Восточный институт — Школа региональных и международных исследований"
schools[1].dptList = [dpt() for i in range(10)]
schools[1].dptList[0].name = "Кафедра корееведения"
schools[1].dptList[
    0].url = "https://www.dvfu.ru/schools/school_of_regional_and_international_studies/structure/the-department/the-department-of-korean-studies.php"
schools[1].dptList[1].name = "Кафедра русского языка как иностранного"
schools[1].dptList[
    1].url = "https://www.dvfu.ru/schools/school_of_regional_and_international_studies/structure/the-department/department-of-russian-as-a-foreign-language.php"
schools[1].dptList[2].name = "Кафедра китаеведения"
schools[1].dptList[
    2].url = "https://www.dvfu.ru/schools/school_of_regional_and_international_studies/structure/the-department/department-of-chinese-studies/"
schools[1].dptList[3].name = "Кафедра лингвистики и межкультурной коммуникации"
schools[1].dptList[
    3].url = "https://www.dvfu.ru/schools/school_of_regional_and_international_studies/structure/the-department/department-of-linguistics-and-intercultural-communication.php"
schools[1].dptList[4].name = "Кафедра японоведения"
schools[1].dptList[
    4].url = "https://www.dvfu.ru/schools/school_of_regional_and_international_studies/structure/the-department/department-of-japanese-studies.php"
schools[1].dptList[5].name = "Кафедра Тихоокеанской Азии"
schools[1].dptList[
    5].url = "https://www.dvfu.ru/schools/school_of_regional_and_international_studies/structure/the-department/department-of-asia-pacific.php"
schools[1].dptList[6].name = "Кафедра международных отношений"
schools[1].dptList[
    6].url = "https://www.dvfu.ru/schools/school_of_regional_and_international_studies/structure/the-department/department-of-international-relations/"
schools[1].dptList[7].name = "Кафедра политологии"
schools[1].dptList[
    7].url = "https://www.dvfu.ru/schools/school_of_regional_and_international_studies/structure/the-department/the-department-of-political-science.php"
schools[1].dptList[8].name = "Кафедра романо-германской филологии"
schools[1].dptList[
    8].url = "https://www.dvfu.ru/schools/school_of_regional_and_international_studies/structure/the-department/department-of-romano-germanic-philology.php"
schools[1].dptList[9].name = "Кафедра русского языка и литературы"
schools[1].dptList[
    9].url = "https://www.dvfu.ru/schools/school_of_regional_and_international_studies/structure/the-department/the-department-of-russian-language-and-literature.php"

schools[2].name = "Школа экономики и менеджмента"
schools[2].dptList = [dpt() for i in range(10)]
schools[2].dptList[0].name = "Департамент экономических наук"
schools[2].dptList[
    0].url = "https://www.dvfu.ru/schools/school_of_economics_and_management/structure/academic-department/"
schools[2].dptList[1].name = "Кафедра бизнес-информатики и экономико-математических методов"
schools[2].dptList[
    1].url = "https://www.dvfu.ru/schools/school_of_economics_and_management/structure/departments/kafedra-biznes-informatiki-i-ekonomiko-matematicheskikh-metodov/prepodavateli/"
schools[2].dptList[2].name = "Кафедра бухгалтерского учёта, анализа и аудита"
schools[2].dptList[
    2].url = "https://www.dvfu.ru/schools/school_of_economics_and_management/structure/departments/kafedra-bukhgalterskogo-ucheta-analiza-i-audit/prepodavateli/"
schools[2].dptList[3].name = "Кафедра государственного и муниципального управления"
schools[2].dptList[
    3].url = "https://www.dvfu.ru/schools/school_of_economics_and_management/structure/departments/the-department-of-state-and-municipal-management.php"
schools[2].dptList[4].name = "Кафедра мировой экономики"
schools[2].dptList[
    4].url = "https://www.dvfu.ru/schools/school_of_economics_and_management/structure/departments/the-department-of-world-economy.php"
schools[2].dptList[5].name = "Базовая кафедра современного банковского дела"
schools[2].dptList[
    5].url = "https://www.dvfu.ru/schools/school_of_economics_and_management/structure/departments/basic-department-of-modern-banking.php"
schools[2].dptList[6].name = "Кафедра сервиса и туризма"
schools[2].dptList[
    6].url = "https://www.dvfu.ru/schools/school_of_economics_and_management/structure/departments/the-department-of-service-and-tourism.php"
schools[2].dptList[7].name = "Кафедра экономики предприятия"
schools[2].dptList[
    7].url = "https://www.dvfu.ru/schools/school_of_economics_and_management/structure/departments/the-department-of-economics-of-enterprises"
schools[2].dptList[8].name = "Кафедра менеджмента"
schools[2].dptList[
    8].url = "https://www.dvfu.ru/schools/school_of_economics_and_management/structure/departments/department-with-management-diploma.php"
schools[2].dptList[9].name = "Кафедра биоэкономики и продовольственной безопасности"
schools[2].dptList[
    9].url = "https://www.dvfu.ru/schools/school_of_economics_and_management/structure/departments/chair-of-bioeconomy-and-food-security/"

schools[3].name = "Юридическая школа"
schools[3].dptList = [dpt() for i in range(8)]
schools[3].dptList[0].name = "Кафедра гражданского права и процесса"
schools[3].dptList[
    0].url = "https://www.dvfu.ru/schools/law_school/structure/departments/the-department-of-civil-law-and-process/"
schools[3].dptList[1].name = "Кафедра конкурентного и предпринимательского права"
schools[3].dptList[
    1].url = "https://www.dvfu.ru/schools/law_school/structure/departments/department-of-competitive-and-business-law/"
schools[3].dptList[2].name = "Кафедра конституционного и административного права"
schools[3].dptList[
    2].url = "https://www.dvfu.ru/schools/law_school/structure/departments/department-of-constitutional-and-administrative-law/"
schools[3].dptList[3].name = "Кафедра международного публичного и частного права"
schools[3].dptList[
    3].url = "https://www.dvfu.ru/schools/law_school/structure/departments/department-of-international-public-and-private-law/"
schools[3].dptList[4].name = "Кафедра правосудия, прокурорского надзора и криминалистики"
schools[3].dptList[
    4].url = "https://www.dvfu.ru/schools/law_school/structure/departments/the-department-of-justice-prosecutor-s-supervision-and-criminology/"
schools[3].dptList[5].name = "Кафедра теории и истории государства и права"
schools[3].dptList[
    5].url = "https://www.dvfu.ru/schools/law_school/structure/departments/department-of-theory-and-history-of-state-and-law/"
schools[3].dptList[6].name = "Кафедра трудового и экологического права"
schools[3].dptList[
    6].url = "https://www.dvfu.ru/schools/law_school/structure/departments/the-department-of-labor-and-environmental-law/"
schools[3].dptList[7].name = "Кафедра уголовного права и криминологии"
schools[3].dptList[
    7].url = "https://www.dvfu.ru/schools/law_school/structure/departments/department-of-criminal-law-and-criminology/"

schools[4].name = "Школа искусств и гуманитарных наук"
schools[4].dptList = [dpt() for i in range(8)]
schools[4].dptList[0].name = "Департамент истории и археологии"
schools[4].dptList[
    0].url = "https://www.dvfu.ru/schools/school_of_humanities/departments/the-department-of-history-and-archaeology/structure/"
schools[4].dptList[1].name = "Департамент коммуникаций и медиа"
schools[4].dptList[
    1].url = "https://www.dvfu.ru/schools/school_of_humanities/departments/the-department-of-communication-and-media/staff/"
schools[4].dptList[2].name = "Департамент социальных наук"
schools[4].dptList[
    2].url = "https://www.dvfu.ru/schools/school_of_humanities/departments/the-department-of-social-and-psychological-sciences/staff/"
schools[4].dptList[3].name = "Департамент философии и религиоведения"
schools[4].dptList[
    3].url = "https://www.dvfu.ru/schools/school_of_humanities/departments/the-department-of-philosophy-and-religious-studies/staff/"
schools[4].dptList[4].name = "Департамент психологии и образования"
schools[4].dptList[
    4].url = "https://www.dvfu.ru/schools/school_of_humanities/departments/the-department-of-psychology-and-pedagogy/staff/"
schools[4].dptList[5].name = "Департамент искусств и дизайна"
schools[4].dptList[
    5].url = "https://www.dvfu.ru/schools/school_of_humanities/departments/the-department-of-art-and-design/workers/"
schools[4].dptList[6].name = "Департамент физической культуры и спорта"
schools[4].dptList[
    6].url = "https://www.dvfu.ru/schools/school_of_humanities/departments/the-department-of-physical-culture-and-sports/workers/"
schools[4].dptList[7].name = "Департамент физического воспитания"
schools[4].dptList[
    7].url = "https://www.dvfu.ru/schools/school_of_humanities/departments/the-department-of-physical-education/workers/"

schools[5].name = "Школа педагогики"
schools[5].dptList = [dpt() for i in range(8)]
schools[5].dptList[0].name = "Кафедра русского языка, литературы и методики преподавания"
schools[5].dptList[
    0].url = "https://www.dvfu.ru/schools/school_of_education/structure/departments/philology/employees.php"
schools[5].dptList[1].name = "Кафедра образования в области романо-германских языков"
schools[5].dptList[
    1].url = "https://www.dvfu.ru/schools/school_of_education/structure/departments/european/employees.php"
schools[5].dptList[2].name = "Кафедра образования в области восточных языков и востоковедения"
schools[5].dptList[
    2].url = "https://www.dvfu.ru/schools/school_of_education/structure/departments/oriental/employees.php"
schools[5].dptList[3].name = "Кафедра исторического образования"
schools[5].dptList[
    3].url = "https://www.dvfu.ru/schools/school_of_education/structure/departments/history/employees.php"
schools[5].dptList[4].name = "Кафедра теории, методики и практики физической культуры и спорта"
schools[5].dptList[4].url = "https://www.dvfu.ru/schools/school_of_education/structure/departments/sports/employees.php"
schools[5].dptList[5].name = "Кафедра естественнонаучного образования"
schools[5].dptList[
    5].url = "https://www.dvfu.ru/schools/school_of_education/structure/departments/natural-science/employees.php"
schools[5].dptList[6].name = "Кафедра математики, физики, информатики и методики преподавания"
schools[5].dptList[
    6].url = "https://www.dvfu.ru/schools/school_of_education/structure/departments/mathematics/employees.php"
schools[5].dptList[7].name = "Кафедра педагогики и психологии развития"
schools[5].dptList[
    7].url = "https://www.dvfu.ru/schools/school_of_education/structure/departments/pedagogy/employees.php"

schools[6].name = "Школа медицины"
schools[6].dptList = [dpt() for i in range(5)]
schools[6].dptList[0].name = "Департамент клинической медицины"
schools[6].dptList[
    0].url = "https://www.dvfu.ru/school_of_medicine/struktura/departament-klinicheskoy-meditsiny/professorsko-prepodavatelskiy-sostav/"
schools[6].dptList[1].name = "Департамент медицинской биохимии и биофизики"
schools[6].dptList[
    1].url = "https://www.dvfu.ru/school_of_medicine/struktura/departament-meditsinskoy-biokhimii-i-biofiziki/professorsko-prepodavatelskiy-sostav/"
schools[6].dptList[2].name = "Департамент фундаментальной медицины"
schools[6].dptList[
    2].url = "https://www.dvfu.ru/school_of_medicine/struktura/departament-fundamentalnoy-meditsiny/professorsko-prepodavatelskiy-sostav/"
schools[6].dptList[3].name = "Департамент общественного здоровья и профилактической медицины"
schools[6].dptList[
    3].url = "https://www.dvfu.ru/school_of_medicine/struktura/departament-obshchestvennogo-zdorovya-i-profilakticheskoy-meditsiny/professorsko-prepodavatelskiy-sostav/"
schools[6].dptList[4].name = "Департамент дополнительного постдипломного образования и ординатуры"
schools[6].dptList[
    4].url = "https://www.dvfu.ru/school_of_medicine/struktura/departament-ordinatury-i-nepreryvnogo-meditsinskogo-obrazovaniya/professorsko-prepodavatelskiy-sostav/"

schools[7].name = "Школа естественных наук"
schools[7].dptList = [dpt() for i in range(7)]


schools[7].dptList[0].name = "Кафедра алгебры, геометрии и анализа"
schools[7].dptList[
    0].url = "https://www.dvfu.ru/schools/school_of_natural_sciences/structures/department/department-of-algebra-geometry-and-analysis/teachers/"
schools[7].dptList[1].name = "Кафедра прикладной математики, механики, управления и программного обеспечения"
schools[7].dptList[
    1].url = "https://www.dvfu.ru/schools/school_of_natural_sciences/structures/department/the-department-of-applied-mathematics-mechanics-control-and-software/teachers/"
schools[7].dptList[2].name = "Кафедра математических методов в экономике"
schools[7].dptList[
    2].url = "https://www.dvfu.ru/schools/school_of_natural_sciences/structures/department/department-of-mathematical-methods-in-economics/employees/"
schools[7].dptList[3].name = "Кафедра химических и ресурсосберегающих технологий"
schools[7].dptList[
    3].url = "https://www.dvfu.ru/schools/school_of_natural_sciences/structures/department/the-chemical-cluster-of-departments/department-of-chemical-and-resource-saving-technologies/faculty.php"
schools[7].dptList[4].name = "Кафедра биоразнообразия и морских биоресурсов"
schools[7].dptList[
    4].url = "https://www.dvfu.ru/schools/school_of_natural_sciences/structures/department/the-cluster-of-biological-departments/department-of-biodiversity-and-marine-bioresources/employees/"
schools[7].dptList[5].name = "Кафедра биохимии, микробиологии и биотехнологии"
schools[7].dptList[
    5].url = "https://www.dvfu.ru/schools/school_of_natural_sciences/structures/department/the-cluster-of-biological-departments/department-of-biochemistry-microbiology-and-biotechnology/members/"
schools[7].dptList[6].name = "Кафедра экологии"
schools[7].dptList[
    6].url = "https://www.dvfu.ru/schools/school_of_natural_sciences/structures/department/the-cluster-of-biological-departments/department-of-ecology/teachers-of-the-department/"



# аргументы - адрес, индекс школы, индекс кафедры/департамента

def alg1(addr, schInd, dptInd):  # просто перечисление в столбик

    req = requests.get(addr, headers=random_headers())
    soup = BeautifulSoup(req.text, "html.parser")
    t = soup.find('div', class_="content col-md-9")  # область кода с фио
    # print(t.text)
    result = re.findall(r'\w+\s\w+\s\w+\n', t.text)
    schools[schInd].dptList[dptInd].teachList = [tch() for i in range(len(result))]
    for i in range(len(result) - 1):
        ttch = tch()
        ttch.name = result[i + 1][:-1]  # последние 2 символа это \n, их нужно обрезать
        ttch.dgre = "-"
        ttch.email = "-"
        schools[schInd].dptList[dptInd].teachList[i] = ttch


def alg2(addr, schInd, dptInd):  # таблица, фио - 2, должность - 3, почта - 5 столбец
    req = requests.get(addr, headers=random_headers())
    soup = BeautifulSoup(req.text, "html.parser")
    rows = soup.find_all('tr')
    schools[schInd].dptList[dptInd].teachList = [tch() for i in range(len(rows) - 1)]
    ni = 0
    for i in range(len(rows) - 1):  # верхняя строка - шапка таблицы
        text = ''.join(map(str, rows[i + 1].contents))
        t = BeautifulSoup(text, "html.parser")
        col = t.find_all('td')
        if len(col) == 5:  # если по другому, то это не строка о преподе
            ttch = tch()
            ttch.name = re.sub(r"[\t\n]", "", col[1].text).strip()
            ttch.dgre = re.sub(r"[\t\n]", "", col[2].text).strip()
            ttch.email = re.findall(r'([a-zA-Z0-9\._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)', col[4].text)[0]
            schools[schInd].dptList[dptInd].teachList[ni] = ttch
            ni = ni + 1


def alg3(addr, schInd, dptInd):  # таблица
    req = requests.get(addr, headers=random_headers())
    soup = BeautifulSoup(req.text, "html.parser")
    rows = soup.find_all('tr')
    schools[schInd].dptList[dptInd].teachList = [tch() for i in range(len(rows) - 1)]
    ni = 0
    for i in range(len(rows) - 1):  # верхняя строка - шапка таблицы
        text = ''.join(map(str, rows[i + 1].contents))
        t = BeautifulSoup(text, "html.parser")
        col = t.find_all('td')
        if len(col) == 6:  # если по другому, то это не строка о преподе
            ttch = tch()
            ttch.name = re.sub(r"[\t\n]", "", col[1].text).strip()
            ttch.dgre = re.sub(r"[\t\n]", "", col[4].text).strip()
            if len(re.findall(r'([a-zA-Z0-9\._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)', col[5].text)) > 0:
                ttch.email = re.findall(r'([a-zA-Z0-9\._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)', col[5].text)[0]
            schools[schInd].dptList[dptInd].teachList[ni] = ttch
            ni = ni + 1


def alg4(addr, schInd, dptInd):  # таблица
    req = requests.get(addr, headers=random_headers())
    soup = BeautifulSoup(req.text, "html.parser")
    rows = soup.find_all('tr')
    schools[schInd].dptList[dptInd].teachList = [tch() for i in range(len(rows) - 1)]
    ni = 0
    for i in range(len(rows) - 1):  # верхняя строка - шапка таблицы
        text = ''.join(map(str, rows[i + 1].contents))
        t = BeautifulSoup(text, "html.parser")
        col = t.find_all('td')
        if len(col) == 4:  # если по другому, то это не строка о преподе
            ttch = tch()
            ttch.name = re.sub(r"[\t\n]", "", col[0].text).strip()
            ttch.dgre = re.sub(r"[\t\n]", "", col[1].text).strip()
            if len(re.findall(r'([a-zA-Z0-9\._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)', col[3].text)) > 0:
                ttch.email = re.findall(r'([a-zA-Z0-9\._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)', col[3].text)[0]
            schools[schInd].dptList[dptInd].teachList[ni] = ttch
            ni = ni + 1


def alg5(addr, schInd, dptInd):  # таблица с двумя столбцами
    req = requests.get(addr, headers=random_headers())
    soup = BeautifulSoup(req.text, "html.parser")
    rows = soup.find_all('tr')
    schools[schInd].dptList[dptInd].teachList = [tch() for i in range(len(rows) - 1)]
    ni = 0
    for i in range(len(rows) - 1):  # верхняя строка - шапка таблицы
        text = ''.join(map(str, rows[i + 1].contents))
        t = BeautifulSoup(text, "html.parser")
        col = t.find_all('td')
        if len(col) == 2:  # если по другому, то это не строка о преподе
            ttch = tch()
            ttch.name = re.sub(r"[\t\n]", "", col[0].text).strip()
            ttch.dgre = re.sub(r"[\t\n]", "", col[1].text).strip()
            schools[schInd].dptList[dptInd].teachList[ni] = ttch
            ni = ni + 1


def alg6(addr, schInd, dptInd):
    req = requests.get(addr, headers=random_headers())
    soup = BeautifulSoup(req.text, "html.parser")
    rows = soup.find_all('tr')
    schools[schInd].dptList[dptInd].teachList = [tch() for i in range(len(rows) - 1)]
    ni = 0
    for i in range(len(rows) - 1):  # верхняя строка - шапка таблицы
        text = ''.join(map(str, rows[i + 1].contents))
        t = BeautifulSoup(text, "html.parser")
        col = t.find_all('td')
        if len(col) == 2:  # если по другому, то это не строка о преподе
            ttch = tch()
            text1 = ''.join(map(str, col[0].contents))
            s1 = BeautifulSoup(text1, "html.parser")
            name1 = s1.find_all('b')
            dg1 = s1.find_all('i')
            ttch.name = ''
            ttch.dgre = ''

            for i in name1:
                ttch.name = ttch.name + i.text
            ttch.name = re.sub(r"[\n]", " ", ttch.name).strip()
            ttch.name = re.sub(r"[\t]", "", ttch.name).strip()
            for i in dg1:
                ttch.dgre = ttch.dgre + i.text
            ttch.dgre = re.sub(r"[\n]", " ", ttch.dgre).strip()
            ttch.dgre = re.sub(r"[\t]", "", ttch.dgre).strip()

            if len(re.findall(r'([a-zA-Z0-9\._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)', col[1].text)) > 0:
                ttch.email = re.findall(r'([a-zA-Z0-9\._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)', col[1].text)[0]
            schools[schInd].dptList[dptInd].teachList[ni] = ttch
            ni = ni + 1


def alg7(addr, schInd, dptInd):
    req = requests.get(addr, headers=random_headers())
    soup = BeautifulSoup(req.text, "html.parser")
    rows = soup.find_all('tr')
    schools[schInd].dptList[dptInd].teachList = [tch() for i in range(len(rows))]
    ni = 0
    for i in range(len(rows)):  # верхняя строка - шапка таблицы
        text = ''.join(map(str, rows[i].contents))
        t = BeautifulSoup(text, "html.parser")
        col = t.find_all('td')
        if len(col) == 2:  # если по другому, то это не строка о преподе
            ttch = tch()
            text1 = ''.join(map(str, col[0].contents))
            s1 = BeautifulSoup(text1, "html.parser")
            names = s1.find_all('p')
            if len(names) != 2: continue

            ttch.name = re.sub(r"[\t\n]", "", names[0].text)
            ttch.dgre = re.sub(r"[\t\n]", "", names[1].text)

            if len(re.findall(r'([a-zA-Z0-9\._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)', col[1].text)) > 0:
                ttch.email = re.findall(r'([a-zA-Z0-9\._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)', col[1].text)[0]
            schools[schInd].dptList[dptInd].teachList[ni] = ttch
            ni = ni + 1


def alg8(addr, schInd, dptInd):
    req = requests.get(addr, headers=random_headers())
    soup = BeautifulSoup(req.text, "html.parser")
    rows = soup.find_all('tr')
    schools[schInd].dptList[dptInd].teachList = [tch() for i in range(len(rows))]
    ni = 0
    for i in range(len(rows)):  # верхняя строка - шапка таблицы
        text = ''.join(map(str, rows[i].contents))
        t = BeautifulSoup(text, "html.parser")
        col = t.find_all('td')
        if len(col) == 2:  # если по другому, то это не строка о преподе
            ttch = tch()
            text1 = ''.join(map(str, col[0].contents))
            s1 = BeautifulSoup(text1, "html.parser")
            name1 = s1.find_all('b')
            dg1 = s1.find_all('i')
            ttch.name = ''
            ttch.dgre = ''

            for i in name1:
                ttch.name = ttch.name + i.text
            ttch.name = re.sub(r"[\n\t]", " ", ttch.name).strip()
            ttch.name = re.sub(r'\s+', ' ', ttch.name)

            for i in dg1:
                ttch.dgre = ttch.dgre + i.text
            ttch.dgre = re.sub(r"[\n\t]", " ", ttch.dgre).strip()
            ttch.dgre = re.sub(r'\s+', ' ', ttch.dgre)

            if len(re.findall(r'([a-zA-Z0-9\._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)', col[1].text)) > 0:
                ttch.email = re.findall(r'([a-zA-Z0-9\._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)', col[1].text)[0]
            schools[schInd].dptList[dptInd].teachList[ni] = ttch
            ni = ni + 1


def alg9(addr, schInd, dptInd):  # таблица, фио - 2, должность - 3, почта - 5 столбец
    req = requests.get(addr, headers=random_headers())
    soup = BeautifulSoup(req.text, "html.parser")
    rows = soup.find_all('tr')
    schools[schInd].dptList[dptInd].teachList = [tch() for i in range(len(rows))]
    ni = 0
    for i in range(len(rows)):  # верхняя строка - шапка таблицы
        text = ''.join(map(str, rows[i].contents))
        t = BeautifulSoup(text, "html.parser")
        col = t.find_all('td')
        if len(col) == 3:  # если по другому, то это не строка о преподе
            ttch = tch()
            ttch.name = re.sub(r"[\t\n]", "", col[1].text).strip()
            ttch.dgre = re.sub(r"[\t\n]", "", col[2].text).strip()
            schools[schInd].dptList[dptInd].teachList[ni] = ttch
            ni = ni + 1


def alg10(addr, schInd, dptInd):
    req = requests.get(addr, headers=random_headers())
    soup = BeautifulSoup(req.text, "html.parser")
    rows = soup.find_all('tr')
    schools[schInd].dptList[dptInd].teachList = [tch() for i in range(len(rows))]
    ni = 0

    for i in range(len(rows)):  # верхняя строка - шапка таблицы
        text = ''.join(map(str, rows[i].contents))
        t = BeautifulSoup(text, "html.parser")
        col = t.find_all('td')
        if len(col) == 3:  # если по другому, то это не строка о преподе
            ttch = tch()
            text1 = ''.join(map(str, col[1].contents))
            text1 = re.split(r"[\t\n(<br>)]",text1)

            n = len(text1)
            k = 0
            while True:
                text1[k] = re.sub(r"[\t\n]", "", text1[k]).strip()
                text1[k] = re.sub(r"[^А-Яа-я\s]", "", text1[k]).strip()
                if text1[k] == "":
                    text1.pop(k)
                    n = n - 1
                    k = k - 1
                k = k + 1
                if k == n: break
            ttch.dgre = ""
            for j in range(len(text1)):
                if j == 0:
                    ttch.name = text1[j]
                if j > 0:
                    ttch.dgre = ttch.dgre + text1[j] + " "

            if len(re.findall(r'([a-zA-Z0-9\._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)', col[2].text)) > 0:
                ttch.email = re.findall(r'([a-zA-Z0-9\._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)', col[2].text)[0]
            schools[schInd].dptList[dptInd].teachList[ni] = ttch
            ni = ni + 1


def alg11(addr, schInd, dptInd):  # таблица, фио - 2, должность - 3, почта - 5 столбец
    req = requests.get(addr, headers=random_headers())
    soup = BeautifulSoup(req.text, "html.parser")
    rows = soup.find_all('tr')
    schools[schInd].dptList[dptInd].teachList = [tch() for i in range(len(rows))]
    ni = 0
    for i in range(len(rows)):  # верхняя строка - шапка таблицы
        text = ''.join(map(str, rows[i].contents))
        t = BeautifulSoup(text, "html.parser")
        col = t.find_all('td')
        if len(col) == 2:  # если по другому, то это не строка о преподе
            ttch = tch()
            ttch.name = re.sub(r"[\t\n]", "", col[1].text).strip()
            ttch.name = re.findall(r'\w+\s\w+\s\w+', ttch.name)[0]
            schools[schInd].dptList[dptInd].teachList[ni] = ttch
            ni = ni + 1

def alg12(addr, schInd, dptInd):
    req = requests.get(addr, headers=random_headers())
    soup = BeautifulSoup(req.text, "html.parser")
    rows = soup.find_all('tr')
    schools[schInd].dptList[dptInd].teachList = [tch() for i in range(len(rows))]
    ni = 0
    for i in range(len(rows)):  # верхняя строка - шапка таблицы
        text = ''.join(map(str, rows[i].contents))
        t = BeautifulSoup(text, "html.parser")
        col = t.find_all('td')
        if len(col) == 2:  # если по другому, то это не строка о преподе
            ttch = tch()
            text1 = ''.join(map(str, col[0].contents))
            s1 = BeautifulSoup(text1, "html.parser")
            names = s1.find_all('p')
            if len(names) == 0:
                continue
            ttch.name = re.sub(r"[\t\n]", "", names[0].text)
            if len(names) > 1:
                ttch.dgre = re.sub(r"[\t\n]", "", names[1].text)

            if len(re.findall(r'([a-zA-Z0-9\._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)', col[1].text)) > 0:
                ttch.email = re.findall(r'([a-zA-Z0-9\._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)', col[1].text)[0]
            schools[schInd].dptList[dptInd].teachList[ni] = ttch
            ni = ni + 1


alg1(schools[0].dptList[0].url,0,0)
alg2(schools[0].dptList[1].url,0,1)
alg3(schools[0].dptList[2].url,0,2)
alg4(schools[0].dptList[3].url,0,3)
alg5(schools[0].dptList[4].url,0,4)
alg1(schools[0].dptList[5].url,0,5)
alg4(schools[0].dptList[6].url,0,6)
alg1(schools[0].dptList[7].url,0,7)
alg1(schools[0].dptList[8].url,0,8)
alg1(schools[0].dptList[9].url,0,9)
alg4(schools[0].dptList[10].url,0,10)
alg6(schools[1].dptList[0].url,1,0) #6
alg6(schools[1].dptList[1].url,1,1) #6
alg6(schools[1].dptList[2].url,1,2) #6
alg6(schools[1].dptList[3].url,1,3) #6
alg6(schools[1].dptList[4].url,1,4)
alg6(schools[1].dptList[5].url,1,5)
alg6(schools[1].dptList[6].url,1,6)
alg6(schools[1].dptList[7].url,1,7)
alg6(schools[1].dptList[8].url,1,8)
alg6(schools[1].dptList[9].url,1,9)
alg7(schools[2].dptList[0].url,2,0)
alg8(schools[2].dptList[1].url,2,1)
alg8(schools[2].dptList[2].url,2,2)
alg8(schools[2].dptList[3].url,2,3)
alg8(schools[2].dptList[4].url,2,4)
alg8(schools[2].dptList[5].url,2,5)
alg8(schools[2].dptList[6].url,2,6)
alg8(schools[2].dptList[7].url,2,7)
alg8(schools[2].dptList[8].url,2,8)
alg8(schools[2].dptList[9].url,2,9)
alg8(schools[3].dptList[0].url,3,0)
alg8(schools[3].dptList[1].url,3,1)
alg8(schools[3].dptList[2].url,3,2)
alg8(schools[3].dptList[3].url,3,3)
alg8(schools[3].dptList[4].url,3,4)
alg8(schools[3].dptList[5].url,3,5)
alg8(schools[3].dptList[6].url,3,6)
alg8(schools[3].dptList[7].url,3,7)
alg9(schools[4].dptList[0].url,4,0)
alg9(schools[4].dptList[1].url,4,1)
alg9(schools[4].dptList[2].url,4,2)
alg9(schools[4].dptList[3].url,4,3)
alg9(schools[4].dptList[4].url,4,4)
alg9(schools[4].dptList[5].url,4,5)
alg9(schools[4].dptList[6].url,4,6)
alg9(schools[4].dptList[7].url,4,7)
alg10(schools[5].dptList[0].url, 5, 0)
alg10(schools[5].dptList[1].url, 5, 1)
alg10(schools[5].dptList[2].url, 5, 2)
alg10(schools[5].dptList[3].url, 5, 3)
alg10(schools[5].dptList[4].url, 5, 4)
alg10(schools[5].dptList[5].url, 5, 5)
alg10(schools[5].dptList[6].url, 5, 6)
alg10(schools[5].dptList[7].url, 5, 7)
alg11(schools[6].dptList[0].url,6,0)
alg11(schools[6].dptList[1].url,6,1)
alg11(schools[6].dptList[2].url,6,2)
alg11(schools[6].dptList[2].url,6,3)
alg11(schools[6].dptList[3].url,6,4)
alg6(schools[7].dptList[0].url,7,0)
alg4(schools[7].dptList[1].url,7,1)
alg12(schools[7].dptList[2].url,7,2)
alg12(schools[7].dptList[3].url,7,3)
alg6(schools[7].dptList[4].url,7,4)
alg12(schools[7].dptList[5].url,7,5)
alg6(schools[7].dptList[6].url,7,6)

f = open('out.html','w')
ind = 0
for setSchool in schools:
    f.write('<h1>'+setSchool.name+'</h1><table border="1">')
    for setDpt in setSchool.dptList:
        f.write('<tr> <td><h3>'+setDpt.name+'</h3></td></tr> ')
        for setTch in setDpt.teachList:
            if not (setTch.name == "" or setTch.name == "-"):
                f.write('<tr><td>'+setTch.name+'</td><td>'+setTch.dgre+'</td><td>'+ setTch.email+ '</td></tr>')
                ind = ind + 1
    f.write('</table>')
print('done', ind)
