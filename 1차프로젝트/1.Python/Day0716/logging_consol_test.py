import logging

def say_hello(msg):
    return 'Hello' + msg
#logging 설정
logging.basicConfig(level = logging.INFO,\
                    format='%(asctime)s -%(levelname)s -%(message)s')
logging.debug("Start of Program")
logging.debug(say_hello('디버그모드'))
logging.info(say_hello('인포모드'))
logging.debug("End of Program")
