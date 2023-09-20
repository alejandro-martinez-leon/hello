from hello.register import Person
from hello import __version__
import datetime
import argparse

def say_hi():
    parser = argparse.ArgumentParser(description=__doc__,
                                        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        help='Your name',
        dest='name',
        type=str)
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f"hello: {__version__}")
    
    args = parser.parse_args()
    
    today = datetime.date.today()
    print(f"Hi {Person(args.name, (today.year, today.month, today.day))}")
