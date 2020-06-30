from math import ceil, log
from sys import argv

args = {}
options = ('--type', '--payment', '--principal', '--periods', '--interest')


def print_diff(interest, principal, periods):
    all_payments = 0
    for m in range(1, int(periods + 1)):
        current_payment = ceil(principal / periods + interest * (principal - principal * (m - 1) /periods))
        print(f'Month {m}: paid out {current_payment}')
        all_payments += current_payment
    print()
    print(f'Overpayment = {all_payments - principal}')


def print_principal(interest, periods, payment):
    principal = int(payment / (interest * (interest + 1) ** periods / ((interest + 1) ** periods - 1)))
    print(f'Your credit principal = {principal}!')
    print(f'Overpayment = {periods * payment - principal}')


def print_payment(interest, periods, principal):
    payment = ceil(principal * interest * (interest + 1) ** periods / ((interest + 1) ** periods- 1))
    print(f'Your annuity payment = {payment}!')
    print(f'Overpayment = {payment * periods - principal}')


def print_periods(interest, principal, payment):
    periods = ceil(log(payment / (payment - interest * principal), interest + 1))
    years = periods // 12
    months = periods % 12
    if not years:
        full_time = f"{months} month"
        if months > 1:
            full_time += 's'
    else:
        full_time = f"{years} year"
        if years > 1:
            full_time += 's'
        if months:
            full_time += f' and {months} month'
        if months > 1:
            full_time += 's'
    print(f'You need {full_time} to repay this credit!')
    print(f'Overpayment = {payment * periods - principal}')


def is_right_arg(arg):
    opt_val = arg.split('=')
    if len(opt_val) != 2 or opt_val[0] not in options or opt_val[0] in args:
        return False
    if opt_val[0] == '--type':
        args[opt_val[0]] = opt_val[1]
        return True
    else:
        try:
            opt_val[1] = float(opt_val[1])
            if opt_val[1] < 0:
                return False
            args[opt_val[0]] = opt_val[1]
            return True
        except ValueError:
            return False


def main():
    for arg in argv[1:]:
        # for arg in input().split():
        if not is_right_arg(arg):
            print('Incorrect parameters')
            return

    if not ('--type' in args and '--interest' in args) or len(args) != 4:
        print('Incorrect parameters')
        return

    if args['--type'] == 'diff':
        if '--payment' not in args:
            print_diff(args['--interest'] / 1200, int(args['--principal']), int(args['--periods']))
        else:
            print('Incorrect parameters')

    elif args['--type'] == 'annuity':
        missing_el, = (set(options) - set(args.keys()))
        if missing_el == '--principal':
            print_principal(args['--interest'] / 1200, int(args['--periods']),int(args['--payment']))
        elif missing_el == '--payment':
            print_payment(args['--interest'] / 1200, int(args['--periods']),int(args['--principal']))
        else:  # elif missing_el == '--periods':
            print_periods(args['--interest'] / 1200, int(args['--principal']),int(args['--payment']))
    else:
        print('Incorrect parameters')


main()
