# -*- coding: utf-8 -*-
# Use unicode source code to make test character string writing easier
import os

from bulkinsert.management.commands.bulkinsert import CSVIMPORT_LOG
from django.conf import settings
from django.test import TestCase

class LogTest(TestCase):
    """ Run test of file parsing """
    logpath = ''

    def get_log_path(self):
        """ Get the log file that should of been written by the parse tests """
        if CSVIMPORT_LOG != 'logger':
            print '''CSVIMPORT_LOG is not set to 'logger' in settings 
                     - assume not using bulkinsert.tests.settings 
                     - so cannot test the log'''
            return False
        logging = getattr(settings, 'LOGGING', '')
        if logging:
            handlers = logging.get('handlers', {})
            if handlers:
                logfile = handlers.get('logfile',{})
                if logfile:
                    self.logpath = logfile.get('filename', '')
        if self.logpath.endswith('.log'):
           if os.path.exists(self.logpath):
               print 'Found bulkinsert_test.log'
               return True
        print '''cvsimport logging is not set up for %s from 
                 bulkinsert.tests.settings so cannot test the log''' % self.logpath
        return False

    def test_log(self):
        """ Check the log is there and then remove it """
        if self.get_log_path():
            csvlog = open(self.logpath)
            lines = csvlog.read()
            self.assertIn('Column quantity = 1e+28 more than the max integer', lines)
            os.remove(self.logpath)
            print 'Deleted bulkinsert_test.log'
        return
