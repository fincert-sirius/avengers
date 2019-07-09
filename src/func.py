def from_txt_to_db(path):
    with open(path,'r') as f:
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

#def from_list_to_db(path):
