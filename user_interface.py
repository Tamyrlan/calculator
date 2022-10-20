import complex as cx
import excep as ex
import model_div as div
import model_mult as mult
import model_pow as pow
import model_sqrt as sqr
import model_sub as sub
import model_sum as sum
import log
print('Callculator app :)')


def menu():
    while True:
        print('\n Main menu')
        print('1.If you want to work with rational numbers enter "1":')
        print('2.If you want to work with complex numbers enter "2":')
        print('Enter 0 to return:')
        try:
            choice_1 = int(input("Choose model:"))
        except ValueError:
            print('There is no such model, try again :(')
            log.pop_error_log()
            return menu()

        if choice_1 == 1:
            print('\n Rational numbers')
            print('1.Addition of numbers')
            print('2.Substration of numbers')
            print('3.Devision of numbers')
            print('4.Multiplication of numbers')
            print('5.Power of number')
            print('6.sqrt')
            print('0.Return to main menu')
            try:
                choice_2 = int(input('Choose the operation thay you want:'))
            except ValueError:
                print('There is no such operation, please try again :(')
                log.pop_error_log()
                return menu()
            if choice_2 == 1:
                number_1 = ex.get_value()
                number_2 = ex.get_value()
                sum.init(number_1, number_2)
                result = sum.do_it()
                log.sum_log(number_1, number_2, result)
                print(result)
                return result

            elif choice_2 == 2:
                number_1 = ex.get_value()
                number_2 = ex.get_value()
                sub.init(number_1, number_2)
                result = sub.do_it()
                log.sub_log(number_1, number_2, result)
                print(result)
                return result
            elif choice_2==3:
                print('\n Devision of numbers')
                print('1. Standart devision " / "')
                print('2. integer devision " // "')
                print('3. The remainder of the devision " % "')
                print('0. Return to main menu')
                try:
                    choice_3 = int(input('Choose the operation:'))
                except ValueError:
                    print('There is no such operation, please try again :(')
                    log.pop_error_log()
                    return menu()
                if choice_3 ==1:
                    number_1 = ex.get_value()
                    number_2 = ex.get_value()
                    div.init(number_1, number_2)
                    try:
                        result = div.do_it()
                        log.div_log(number_1, number_2, result)
                        print(result)
                        return result
                    except ZeroDivisionError:
                        print('You can not devide to "0"')
                        log.pop_error_log
                        return menu()
                
                elif choice_3 ==2:
                    number_1 = ex.get_value()
                    number_2 = ex.get_value()
                    div.init(number_1, number_2)
                    try:
                        result = div.do_it_1()
                        log.div_1_log(number_1, number_2, result)
                        print(result)
                        return result
                    except ZeroDivisionError:
                        print('You can not devide to "0"')
                        log.pop_error_log
                        return menu()    
                
                elif choice_3 ==3:
                    number_1 = ex.get_value()
                    number_2 = ex.get_value()
                    div.init(number_1, number_2)
                    try:
                        result = div.do_it_2()
                        log.div_2_log(number_1, number_2, result)
                        print(result)
                        return result
                    except ZeroDivisionError:
                        print('You can not devide to "0"')
                        log.pop_error_log
                        return menu() 
                elif choice_3==0:
                    return menu()
                
            elif choice_2 ==4:
                number_1 = ex.get_value()
                number_2 = ex.get_value()
                mult.init(number_1, number_2)
                result = mult.do_it()
                log.mult_log(number_1, number_2, result)
                print(result)
                return result
                
            elif choice_2 ==5:
                number_1 = ex.get_value()
                number_2 = ex.get_value()
                pow.init(number_1, number_2)
                result = pow.do_it()
                log.pow_log(number_1, number_2, result)
                print(result)
                return result

            elif choice_2 ==6:
                number_1=ex.get_value()
                result = sqr.do_it(number_1)
                log.sqt_log(number_1,result)
                print(result)
                return result
                
            elif choice_2==0:
                return menu()
            else:
                print('Something went wrong, please try again :(')
                log.pop_error_log()
                menu()

        if choice_1==2:
            print("\nComplex numbers")
            print('1.Addition of numbers')
            print('2.Substration of numbers')
            print('3.Devision of numbers')
            print('4.Multiplication of numbers')
            print('5.Power of number')
            print('6.sqrt')
            print('0.Return to main menu')
            try:
                choice_2 = int(input("Выберете операцию: "))
            except ValueError:
                print('That is not integer, please try again :(')
                log.pop_error_log
                return menu()
                    
            if choice_2 ==1:
                complex_number_1 = cx.create_complex()
                complex_number_2 = cx.create_complex()
                sum.init(complex_number_1,complex_number_2)
                result = sum.do_it()
                log.sum_log(complex_number_1,complex_number_2,result)
                print(result)
                return result

            elif choice_2==2:
                complex_number_1 = cx.create_complex()
                complex_number_2 = cx.create_complex()
                sub.init(complex_number_1,complex_number_2)
                result = sub.do_it()
                log.sub_log(complex_number_1,complex_number_2,result)
                print(result)
                return result