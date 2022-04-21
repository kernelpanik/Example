import textwrap
from argparse import ArgumentParser, HelpFormatter
import sys

class RawFormatter(HelpFormatter):
    def _fill_text(self, text, width, indent):
        return "\n".join([textwrap.fill(line, width) for line in textwrap.indent(textwrap.dedent(text), indent).splitlines()])

program_descripton = f'''
    Convert temperature between Celsius and Fahrenheit and vice versa
    Default is to convert from Fahrenheit to Celsius

    USAGE:
    '''

parser = ArgumentParser(description=program_descripton, formatter_class=RawFormatter)
parser.add_argument('Temp', help="Temperature you want to convert", type=float)
parser.add_argument("-c", "--celsius", help="Convert to Celsius", action="store_true")
parser.add_argument("-f", "--fahrenheit", help="Convert to Fahrenheit",  action="store_true")
args = parser.parse_args()

if len(sys.argv)==1:
    parser.print_help()

args = parser.parse_args()


def conv_from_f_to_c():
    temp_f = args.Temp
    temp_c = (temp_f - 32) * 0.5556
    print(f'\nTemperature in Celsius is {temp_c}\n')


def conv_from_c_to_f():
    temp_c = args.Temp
    temp_f = (temp_c * 1.8) + 32
    print(f'\nTemperature in Fahrenheit is {temp_f}\n')


if args.celsius:
    conv_from_f_to_c() 
elif args.fahrenheit:
    conv_from_c_to_f()
else:
    conv_from_f_to_c() 
