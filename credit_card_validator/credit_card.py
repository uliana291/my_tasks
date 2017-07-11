

def luhn_check(card_number):
    try:
        num = int(card_number)
    except:
        return False
    sum = 0
    curr = 1
    for i in range(len(card_number)-1, -1, -1):
        if curr == 1:
            sum += int(card_number[i])
            curr = 2
        else:
            double_num = int(card_number[i])*2
            sum += double_num % 10 + double_num // 10
            curr = 1
    if sum % 10 == 0:
        return True
    else:
        return False


def visa_check(card_number):
    identifier = card_number[0:6]
    if identifier[0] == '4' and len(card_number) in {13, 16, 19}:
        return True
    return False


def mastercard_check(card_number):
    identifier = card_number[0:6]
    if identifier[0:2] in list(map(str, range(51, 56))) or identifier[0:4] in list(map(str, range(2221, 2721))):
        if len(card_number) == 16:
            return True
    return False


def maestro_check(card_number):
    identifier = card_number[0:6]
    if identifier[0] == '6' or identifier[0:2] == '50' or identifier[0:2] in list(map(str, range(56, 59))):
        if len(card_number) in range(12, 20):
            return True
    return False


def american_express(card_number):
    identifier = card_number[0:6]
    if identifier[0:2] in {'34', '37'} and len(card_number) == 15:
        return True
    return False


def validation_check(card_number, issuer_check):
    if len(card_number) < 11 or len(card_number) > 19:
        return False
    if not luhn_check(card_number):
        return False
    if '1' in issuer_check:
        if not visa_check(card_number):
            return False
    if '2' in issuer_check:
        if not mastercard_check(card_number):
            return False
    if '3' in issuer_check:
        if not maestro_check(card_number):
            return False
    if '4' in issuer_check:
        if not american_express(card_number):
            return False
    return True


def main():
    print('Welcome to application of card number checker. The only aim of' +
          ' it is checking the number of entered card number')
    card_number = input('Enter the card number:')
    print('Visa - 1, MasterCard - 2, Maestro - 3, AmericanExpress - 4')
    issuer_check = input('Choose issuing network that you want to make a validation of (1-4, comma separated):')
    if validation_check(card_number, issuer_check):
        print('This number is valid')
    else:
        print('This number is not valid')

if __name__ == "__main__":
    main()