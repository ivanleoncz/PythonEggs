#!/usr/bin/python3
""" Demonstrates class inheritance functionality. """

__author__ = "@ivanleoncz" 


class German:
    """ Italian phrases. """

    def hello(self):
        return "Hallo!"


    def how_are_you(self):
        return "Wie geht's?"


class Italian:
    """ Italian phrases. """

    def hello(self):
        return "Ciao!"


    def how_are_you(self):
        return "Come stai?"


class Languages(German, Italian):
    """ Phrases in multiple languages. """

    def greetings(self):
        german  = German.hello(self)
        italian = Italian.how_are_you(self)
        return "%s %s" % (german,italian)


if __name__ == "__main__":
    langs = Languages()
    print(langs.greetings())


