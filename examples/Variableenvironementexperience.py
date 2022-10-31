from dotenv import *
from dotenv import load_dotenv
import os

load = load_dotenv(dotenv_path='/home/pi/midisynth/examples/variables.env')
TRANSPOSE = int(os.getenv('TRANSPOSE'))

print(TRANSPOSE)

TRANSPOSE = TRANSPOSE + 1
#os.environ['TRANSPOSE'] = 'BONJOUR'
os.putenv(os.environ['TRANSPOSE']) = 5
print(TRANSPOSE)


