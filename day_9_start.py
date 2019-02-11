import datetime

class MessageUser():
    user_details= []
    messages = []
    base_message = """Hi i am amike bpllajs
    kdhaskdjaslkhdsjfklsadhfkjsdakfjalsk
    jdfsadhflkajsdlkfjalsdjfklsdajflads
    DasdASDDDDDDDDDDDDDDDDDDD
    dASDASasASDDSDASASDASDF
    ASDasDASADASASDASDASDAFASD
    ASDDAASDDASDASDASDASSADFASR
    DASASSDDASASDSDFDRTAEFD
    ASASDASDASSDRWEREWTASDF

    MIKEPLUSPLUS
"""
    def add_user(self,name,amount):
        name = name[0].upper() + name[1:].lower()

        detail = {
            'name': name,
            'amount': amount,
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        self.user_details.append(detail)



default_names = {"Justin",'John','emilie','jim', 'ron', 'sandra', 'veronica','whitney'}
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]
unf_message ="""Hi i am amike bpllajskdhaskdjaslkhdsjfklsadhfkjsdakfjalskjdfsadhflkajsdlkfjalsdjfklsdajflads
DasdASDDDDDDDDDDDDDDDDDDD
dASDASasASDDSDASASDASDF
ASDasDASADASASDASDASDAFASD
ASDDAASDDASDASDASDASSADFASR
DASASSDDASASDSDFDRTAEFD
ASASDASDASSDRWEREWTASDF

MIKEPLUSPLUS
"""
def make_messages(names, amounts):
    messages = []
    if len(names) == len(amounts):
        i = 0
        today = datatime.date.today()
