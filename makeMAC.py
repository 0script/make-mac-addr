import random
import argparse

#download module in local dir
# ==>>$wget https://raw.githubusercontent.com/0script/int-to-hexaString/main/hexify.py
import hexify


VENDORS={
    'sony':'6C:B2:27',
    'samsung':'00:07:AB',
    'apple':'00:03:93',
    'intel':'00:17:35',
    'nokia':'00:19:8F',
    'honhai':'80:2B:F9',
    'hp':'18:60:24',
    }


def makeMac(vendors_OUI):
    
    return vendors_OUI+':'+hexify.hexify(random.randint(0,255))+':'+hexify.hexify(random.randint(0,255))+':'+hexify.hexify(random.randint(0,255))

def main(number,oui):
    for i in range(number):
        print('{}'.format(makeMac(VENDORS[oui])))

########################################################

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('-n',
        '--number',
        dest='number',
        type=int,
        help='Number of mac address to generate',
        default=10)
    parser.add_argument('--oui',
        dest='OUI',
        type=str,
        help='vendor : samsung,apple,intel,hp.. edit vendor list by setting VENDORS!',
        default='intel')
    args=parser.parse_args()

    main(args.number,args.OUI)