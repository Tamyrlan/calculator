from datetime import datetime as dt
from time import time

def pop_error_log():
    time = dt.now().strftime('%H:%M')
    with open('log.csv','a') as my_file:
        my_file.write('{} Time {}\n'
        .format('Error occured',time))

def sum_log(number_1,number_2,result):
    time = dt.now().strftime('%H:%M')
    with open('log.csv','a') as my_file:
        my_file.write('{}+{}={} Time \n'
        .format(number_1,number_2,result,time))

def sub_log(number_1,number_2,result):
    time = dt.now().strftime('%H:%M')
    with open('log.csv','a') as my_file:
        my_file.write('{}-{}={} Time \n'
        .format(number_1,number_2,result,time))

def mult_log(number_1,number_2,result):
    time = dt.now().strftime('%H:%M')
    with open('log.csv','a') as my_file:
        my_file.write('{}*{}={} Time \n'
        .format(number_1,number_2,result,time))

def pow_log(number_1,number_2,result):
    time = dt.now().strftime('%H:%M')
    with open('log.csv','a') as my_file:
        my_file.write('{}**{}={} Time \n'
        .format(number_1,number_2,result,time))

def div_log(number_1,number_2,result):
    time = dt.now().strftime('%H:%M')
    with open('log.csv','a') as my_file:
        my_file.write('{}/{}={} Time \n'
        .format(number_1,number_2,result,time))

def div_1_log(number_1,number_2,result):
    time = dt.now().strftime('%H:%M')
    with open('log.csv','a') as my_file:
        my_file.write('{}%{}={} Time \n'
        .format(number_1,number_2,result,time))

def div_2_log(number_1,number_2,result):
    time = dt.now().strftime('%H:%M')
    with open('log.csv','a') as my_file:
        my_file.write('{}//{}={} Time \n'
        .format(number_1,number_2,result,time))

def sqt_log(number,result):
    time = dt.now().strftime('%H:%M')
    with open('log.csv','a') as my_file:
        my_file.write('sqt{}={} Time \n'
        .format(number,result,time))