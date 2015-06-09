#!/bin/python

class welcomeMessage(object):

    def __init__(self, user):
        self.user = user

    @property
    def valuecheck(self):
        return 'user is %s' % self.user

a = welcomeMessage('John')
a.valuecheck()
