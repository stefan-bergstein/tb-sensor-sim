import sys
import os
import argparse
import logging
import urllib3
import requests
import time
import random

urllib3.disable_warnings()

#
# Globals
#

# Logging
module = sys.modules['__main__'].__file__
logger = logging.getLogger(module)


# Generates new random value that is within 3% range from previous value
def gen_next_value(prev_Vvalue, min_val, max_val): 
    ran = random.random()
    value = prev_Vvalue + ((max_val - min_val) * (ran - 0.5)) * 0.03
    value = max([min_val, min(max_val, value)])
    return value


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Sensor simulator')


    parser.add_argument(
            '--server',  type=str, default='https://demo.thingsboard.io',
            help='Thingsboard HTTP Endpoint [default: https://demo.thingsboard.io]')

    parser.add_argument(
            '--token',  type=str, 
            help='ACCESS_TOKEN of the device')    

    parser.add_argument(
            '--interval',  type=int, default=1,
            help='Frequency of submitted data')

    parser.add_argument(
            '--telemetry_key',  type=str, default='temperature',
            help='telemetry key [default: temperature]' ) 

    parser.add_argument(
            '--telemetry_min',  type=int, default=20,
            help='telemetry min value [default: 20]' ) 

    parser.add_argument(
            '--telemetry_max',  type=int, default=30,
            help='telemetry max value [default: 30]' ) 


    parser.add_argument('-l', '--log-level', default='WARNING',
                                help='Set log level to ERROR, WARNING, INFO or DEBUG')

    args = parser.parse_args()


    #
    # Configure logging
    #

    try:
        logging.basicConfig(stream=sys.stderr, level=args.log_level, format='%(name)s (%(levelname)s): %(message)s')
    except ValueError:
        logger.error("Invalid log level: {}".format(args.log_level))
        sys.exit(1)

    logger.info("Log level set: {}".format(logging.getLevelName(logger.getEffectiveLevel())))

    thingsboard_server = os.getenv("SERVER", default=args.server)
    access_token = os.getenv("TOKEN", default=args.token)
    interval = int(os.getenv("INTERVAL", default=args.interval))
    telemetry_key = os.getenv("TELEMETRY_KEY", default=args.telemetry_key)
    telemetry_min = int(os.getenv("TELEMETRY_MIN", default=args.telemetry_min))
    telemetry_max = int(os.getenv("TELEMETRY_MAX", default=args.telemetry_max))

    url = thingsboard_server + '/api/v1/' + access_token + '/telemetry'


    telemetry_value = telemetry_min

    while True:
        try:
            telemetry_value =  gen_next_value(telemetry_value, telemetry_min, telemetry_max )
            r = requests.post(url, json={telemetry_key: telemetry_value},  verify=False )
            if r.status_code != 200:
                logger.error("http POST faild: {}, Code: {}".format(url, r.status_code))

        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)

        time.sleep(interval) 

