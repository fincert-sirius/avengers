# -*- coding: utf8 -*-
import requests, smtplib, configparser

ALLOWED_EXTENSIONS = ('json', 'xml', 'txt', 'csv')

subjects = {'fakebank_ru': 'Запрос на разделегирование ресурса.',
            'fakebank_en': '',
            'fakesurvey': 'Запрос на разделегирование ресурса.',
            'fakectc': 'Запрос на разделегирование ресурса.',
            'fakesocial': 'Запрос на разделегирование ресурса.',
            'faketick': 'Запрос на разделегирование ресурса.',
            'fakesmth_en': '',
            'fakemfo_en': '',
            'fakelombard': 'Запрос на разделегирование ресурса.',
            'fakesmth':'Запрос на разделегирование ресурса.'
            }
texts = {
    'fakebank_ru': u'''Уважаемые коллеги!

Наши специалисты обнаружили фишинговый сайт: {}
На данном сайте организация {названиеорг} предлагает услуги по выдаче кредитов. 
Банк России не располагает сведениями об организации {} и интернет-сайте {} –
http://cbr.ru/credit/main.asp


Организация {} использует в своем наименовании слово «банк», что является нарушением Федерального закона от 02.12.1990 № 395-1 «О банках и банковской деятельности», в ст. 7 которого указано, что ни одно юридическое лицо в Российской Федерации, за исключением юридического лица, получившего от Банка России лицензию на осуществление банковских операций, не может использовать в своем фирменном наименовании слова «банк», «кредитная организация» или иным образом указывать на то, что данное юридическое лицо имеет право на осуществление банковских операций.
{}, предлагая на своём сайте услугу по выдаче кредитов, нарушает требования Гражданского кодекса Российской Федерации. Согласно ч. 1 ст. 819 ГК РФ, кредиторами по кредитным договорам могут быть только банки или иные кредитные организации, а в соответствии с ч. 1 ст. 835 ГК РФ правом на привлечение денежных средств во вклады имеют банки, имеющие лицензию Банка России.
Таким образом, сайт {} используется с целью создания у пользователей ошибочного мнения о принадлежности к кредитной организации за счет введения этих лиц в заблуждение относительно ее принадлежности (подлинности) вследствие сходства доменных имен, оформления или содержания информации (фишинг).
Банк России, как компетентная организация, просит Вас в соответствии с п. 5.7 Правил регистрации доменных имен в доменах .RU и .РФ снять сайт с делегирования.


Банк России
Департамент информационной безопасности
Центр мониторинга и реагирования на компьютерные атаки (ФинЦЕРТ) 

T: +7 495 772-70-90
E: FinCERT@cbr.ru
''',
    'fakebank_en': u'''
Dear colleagues!

Our specialists have found phishing website, which misleads users.
{}

This organization refers to itself as a "bank". But she does not have a license from the Bank of Russia. This organization violates the laws of the Russian Federation.
The Bank of Russia asks you to consider the possibility of taking appropriate measures aimed at removing this domain from delegation. 

Best regards,

The Central Bank of the Russian Federation
The Financial Sector Computer Emergency Response Team (FinCERT) 
www.cbr.ru/eng/
T: +7 495 772-70-90
E: FinCERT@cbr.ru
''',
    'fakesurvey': u'''Коллеги, добрый день!

Наши специалисты обнаружили фишинговый сайт: {}

Данный ресурс представляет собой опрос. После ответа на несколько предложенных вопросов пользователю предлагается к выплате денежная сумма, основным условием получения которой является, так называемый, «закрепительный платёж». Ресурс предлагает пользователю ввести личные сведения для оплаты, не имея полномочий на работу с персональными данными и не являясь оператором по переводу электронных денежных средств.

Таким образом, адресуемая с использованием домена информационная система применяется для получения от третьих лиц (пользователей системы) конфиденциальных сведений за счет введения этих лиц в заблуждение.
Банк России, как компетентная организация, просит Вас в соответствии с пунктом 5.7 Правил регистрации доменных имен в доменах .RU и .РФ снять домен с делегирования.


Банк России
Департамент информационной безопасности
Центр мониторинга и реагирования на компьютерные атаки (ФинЦЕРТ) 

T: +7 495 772-70-90
E: FinCERT@cbr.ru

''',
    'fakectc': u'''Коллеги, добрый день!

Наши специалисты обнаружили фишинговый сайт: {}

Данный ресурс имитирует сервис по переводу денежных средств с карты на карту. На сайте пользователю предлагается ввести личные сведения для денежного перевода, не имея полномочий на работу с персональными данными и не являясь оператором по переводу электронных денежных средств.

Таким образом, адресуемая с использованием домена информационная система применяется для получения от третьих лиц (пользователей системы) конфиденциальных сведений за счет введения этих лиц в заблуждение.
Банк России, как компетентная организация, просит Вас в соответствии с пунктом 5.7 Правил регистрации доменных имен в доменах .RU и .РФ снять домен с делегирования.


Банк России
Департамент информационной безопасности
Центр мониторинга и реагирования на компьютерные атаки (ФинЦЕРТ) 

T: +7 495 772-70-90
E: FinCERT@cbr.ru

''',
    'fakesocial': u'''Коллеги, добрый день!

Наши специалисты обнаружили фишинговый сайт: {}

Данный ресурс представляет собой сервис по поиску выплат, якобы причитающихся пользователю. В результате работы с сайтом пользователю предлагается к выплате денежная сумма, основным условием получения которой является, так называемый, «закрепительный платёж». Ресурс предлагает пользователю ввести личные сведения для оплаты, не имея полномочий на работу с персональными данными и не являясь оператором по переводу электронных денежных средств.

Таким образом, адресуемая с использованием домена информационная система применяется для получения от третьих лиц (пользователей системы) конфиденциальных сведений за счет введения этих лиц в заблуждение.
Банк России, как компетентная организация, просит Вас в соответствии с пунктом 5.7 Правил регистрации доменных имен в доменах .RU и .РФ снять домен с делегирования.


Банк России
Департамент информационной безопасности
Центр мониторинга и реагирования на компьютерные атаки (ФинЦЕРТ) 

T: +7 495 772-70-90
E: FinCERT@cbr.ru

''',
    'faketick': u'''Коллеги, добрый день!

Наши специалисты обнаружили фишинговый сайт: {url}

Данный ресурс представляет собой сервис по продаже билетов. После выбора билетов ресурс предлагает пользователю ввести личные сведения для оплаты, не имея полномочий на работу с персональными данными и не являясь оператором по переводу электронных денежных средств.

Таким образом, адресуемая с использованием домена информационная система применяется для получения от третьих лиц (пользователей системы) конфиденциальных сведений за счет введения этих лиц в заблуждение.
Банк России, как компетентная организация, просит Вас в соответствии с пунктом 5.7 Правил регистрации доменных имен в доменах .RU и .РФ снять домен с делегирования.


Банк России
Департамент информационной безопасности
Центр мониторинга и реагирования на компьютерные атаки (ФинЦЕРТ) 

T: +7 495 772-70-90
E: FinCERT@cbr.ru

''',
    'fakesmth_en': u'''Dear colleagues!

Our specialists have found phishing website, which misleads users.
{}

The domain is phishing website, which mislead users. They collect information about user's personal.
The Bank of Russia asks you to consider the possibility of taking appropriate measures aimed at removing this domain from delegation. 

Best regards,

The Central Bank of the Russian Federation
The Financial Sector Computer Emergency Response Team (FinCERT) 
www.cbr.ru/eng/
T: +7 495 772-70-90
E: FinCERT@cbr.ru
''',
    'fakemfo_en': u'''Dear colleagues!

Our specialists have found phishing website, which misleads users.
{}

This organization does not have a license from the Bank of Russia to issue loans.
The Bank of Russia asks you to consider the possibility of taking appropriate measures aimed at removing this domain from delegation. 

Best regards,

The Central Bank of the Russian Federation
The Financial Sector Computer Emergency Response Team (FinCERT) 
www.cbr.ru/eng/
T: +7 495 772-70-90
E: FinCERT@cbr.ru
''',
    'fakelombard': u'''Уважаемые коллеги!

Наши специалисты обнаружили фишинговый сайт: {}
На данном сайте организация предлагает услуги по выдаче займов (кредитования) гражданам под залог принадлежащих им вещей и использует термин «ломбард».
Организация нарушает требования Федерального закона от 19.07.2004 № 196-ФЗ «О ломбардах», в соответствии с ч. 1, ст. 2 которого ломбардом является юридическое лицо – специализированная коммерческая организация, основными видами деятельности которой являются предоставление краткосрочных займов гражданам и хранение вещей. Согласно п. 2, ч. 3, ст. 2.3 указанного Федерального закона, ведение государственного реестра ломбардов осуществляется Банком России – 
http://www.cbr.ru/finmarket/supervision/sv_micro
в котором содержится актуальный перечень данных организаций. В данном реестре организация, предлагающая услуги на сайте {} по выдаче займов (кредитования) гражданам под залог вещей, не значится.

Таким образом, сайт {} используется с целью создания у пользователей ошибочного мнения о принадлежности к ломбарду за счет введения этих лиц в заблуждение относительно ее принадлежности (подлинности) вследствие сходства доменных имен, оформления или содержания информации (фишинг).
Банк России, как компетентная организация, просит Вас в соответствии с п. 5.7 Правил регистрации доменных имен в доменах .RU и .РФ инициировать проверку документов.


Банк России
Департамент информационной безопасности
Центр мониторинга и реагирования на компьютерные атаки (ФинЦЕРТ) 

T: +7 495 772-70-90
E: FinCERT@cbr.ru
''',
    'fakesmth': u'''Коллеги, добрый день!

Наши специалисты обнаружили фишинговый сайт: {}

Таким образом, адресуемая с использованием домена информационная система применяется для получения от третьих лиц (пользователей системы) конфиденциальных сведений за счет введения этих лиц в заблуждение.
Банк России, как компетентная организация, просит Вас в соответствии с пунктом 5.7 Правил регистрации доменных имен в доменах .RU и .РФ снять домен с делегирования.


Банк России
Департамент информационной безопасности
Центр мониторинга и реагирования на компьютерные атаки (ФинЦЕРТ) 

T: +7 495 772-70-90
E: FinCERT@cbr.ru

'''
}

types = ['fakebank_ru', 'fakebank_en', 'fakesurvey', 'fakectc', 'fakesocial', 'faketick', 'fakesmth_en', 'fakemfo_en',
         'fakelombard', 'fakesmth']


def from_txt_to_db(path):
    with open(path, 'r') as f:
        try:
            text = f.read().split('\n')
            return text
        except Exception:
            return 'Error'


def from_lst_to_db(path):
    def load_list():
        dangerous_urls = []
        fraud_mobile_sms_urls = []
        fraud_phishing_finance_urls = []
        fraud_phishing_urls = []
        with open('dangerous_urls.lst', mode='r') as f:
            for line in f.readlines():
                dangerous_urls.append(line.split('/')[2])
        with open('fraud_mobile_sms_urls.lst', mode='r') as f:
            for line in f.readlines():
                fraud_mobile_sms_urls.append(line.split('/')[2])
        with open('fraud_phishing_finance_urls.lst', mode='r') as f:
            for line in f.readlines():
                fraud_phishing_finance_urls.append(line.split('/'[2]))
        with open('fraud_phishing_urls.lst', mode='r') as f:
            for line in f.readlines():
                fraud_phishing_urls.append(line.split('/')[2])

        result = {}
        result['dangerous_urls'] = dangerous_urls
        result['fraud_mobile_sms_urls'] = fraud_mobile_sms_urls
        result['fraud_phishing_finance_urls'] = fraud_phishing_finance_urls
        result['fraud_phishing_urls'] = fraud_phishing_urls

        return result


def web_archive(DOMAIN, FROM=2018, TO=2019):
    # Готовим запрос.
    # Ключи web archive: [["urlkey","timestamp","original","mimetype","statuscode","digest","length"],
    web_request = "http://web.archive.org/cdx/search/cdx?url=*.{}/*&output=json&from={}&to={}&fl=timestamp,original,length&limit=100".format(
        DOMAIN, str(FROM), str(TO))
    response = None
    try:
        response = requests.get(web_request)

        if response:
            json_response = response.json()
            return json_response
        else:
            return ['',
                    "Ошибка выполнения запроса:\n" + "Http статус:" + response.status_code + "(" + response.reason + ")"]

    except:
        return ['', "Запрос не удалось выполнить. Проверьте подключение к сети Интернет."]


def send_email(subject, to_addr, body_text):
    config = configparser.ConfigParser()
    config.read(r'C:\Users\User\PycharmProjects\avengers_final\src\settings.ini')
    user = config.get('SMTP', "user")
    psw = config.get('SMTP', "psw")
    server = config.get("SMTP", 'SMTP_server')
    port = int(config.get("SMTP", "server_port"))
    BODY = "\r\n".join((
        "From: %s" % user,
        "To: %s" % to_addr,
        "Subject: %s" % subject,
        "",
        body_text
    )).encode('utf-8')

    server = smtplib.SMTP(server, port)
    server.ehlo()
    server.starttls()
    server.login(user, psw)
    server.sendmail(user, to_addr, BODY)
    server.close()


def send_to_registrator(domain, type, reg_mail, orgname=None):
    to_addr = reg_mail
    body_text = 'None'
    subject = subjects[type]
    if type == "fakebank_ru":
        body_text = texts[type].format(domain, orgname, domain, orgname, orgname, domain)

    elif type in ['fakebank_en', 'fakesurvey', 'fakectc', 'fakesocial', 'faketick', 'fakemfo_en', 'fakebank_en', 'fakesmth']:
        body_text = texts[type].format(domain)

    elif type == 'fakelombard':
        body_text = texts[type].format(domain, domain, domain)

    send_email(subject, to_addr, body_text)

    #body_text.encode('utf-8')
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# send_to_registrator('ya.ru', 'fakebank_en', 'xenon.a@ya.ru')