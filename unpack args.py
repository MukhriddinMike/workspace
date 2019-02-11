def health_check(age,apple, cig):
    answer=(100-age)+(apple*2.4)-(cig*1.4)
    print(answer)
my_data=[22,4,0]

health_check(my_data[0],my_data[1],my_data[2])
health_check(*my_data)
import dict_example
print(dict_example.list_friends())