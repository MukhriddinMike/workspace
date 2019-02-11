class Animal():
    noise = "Grunt"
    size = "Large"
    color = "Brown"
    hair = "Covers the body"
    def get_color(self,abc):
        return self.color + " " + abc
    @property
    def make_noise(self):
        return self.noise


dog = Animal()
dog.get_color('red')


dog.make_noise

dog.size = 'Small'
dog.color = 'black'
dog.hair  = "hairless bold"


class Dog():
    name = 'John'
    # color = 'brown'
    # def get_color(self):
    #     return self.color

jon = Dog(Animal)
jon.color = 'white'
jon.name ='Jon Snow'





abc = "New string"
def some_func(arg_1,arg_2,kwarg_1=None, kwarg_2=None):
    print(arg_1,arg_2)
    if kwarg_1 != None:
        print(kwarg_1)


some_func('abc','car',kwarg_1='Not a big deal')


email_address = 'miwady@mail.ru'
to_list = ['mishady@list.ru']
from_list = ['miwa0981@gmail.com', 'mukhriddinergashaliev@gmail.com']

def send_mail(email, to_list = to_list, from_list=from_list):
    pass


send_mail('mukhriddinergashaliev@gmail.com', to_list=['mishady@list.ru'], from_list=['miwa0981@gmail.com'])

