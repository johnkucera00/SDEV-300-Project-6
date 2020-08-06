"""
__filename__ = "webpage.py"
__coursename__ = "SDEV 300 6380 - Building Secure Web Applications (2198)"
__author__ = "John Kucera"
__copyright__ = "None"
__credits__ = ["John Kucera"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "John Kucera"
__email__ = "johnkucera00@gmail.com"
__status__ = "Test"
"""
from datetime import datetime
from flask import Flask
from pytz import timezone

APP = Flask(__name__)

# Index
@APP.route('/webpage')
def index():
    """
    Webpage Index
    """
    content = webhead()
    content += webh1('The Best Breath Mints Of All Time')
    content += webh2('Altoids')
    content += paragraph1()
    content += unordlist()
    content += webh3('Tic Tacs')
    content += paragraph2()
    content += ordlist()
    content += currenttime()
    content += webend()
    return content

# Head
def webhead():
    """
    Webpage Head
    """
    head_data = '<!--Head and Title-->'
    head_data += '<!DOCTYPE html> '
    head_data += '<html>'
    head_data += '<head> '
    head_data += '<title>The Best Breath Mints</title>'
    head_data += '</head>'
    head_data += '<body>'
    return head_data

# Heading 1
def webh1(string):
    """
    Webpage Heading 1
    """
    heading_string = '<H1 style="font-family: Verdana, sans-serif;">' + string + '</H1>'
    return heading_string

# Heading 2
def webh2(string):
    """
    Webpage Heading 2
    """
    heading_string = '<H2 style="font-family: Lucida Console, monospace;">' + string + '</H2>'
    return heading_string

# Paragraph under Heading 2
def paragraph1():
    """
    Webpage Paragraph under Heading 2
    """
    para_data = '<!--Content for Altoids Heading-->'
    para_data += '<p>'
    para_data += 'Altoids - the Curiously Strong Mints! They were first made in '
    para_data += '1780 and have stayed in the same distinctive tin cases for '
    para_data += 'centuries. Their sharp taste of peppermint wipes bad breath out'
    para_data += ' in an instant. Places you can buy it:'
    para_data += '</p>'
    return para_data

# Unordered List under Heading 2
def unordlist():
    """
    Webpage Unordered List under Heading 2
    """
    ul_data = '<ul>'
    ul_data += '<li>Target</li>'
    ul_data += '<li>7-eleven</li>'
    ul_data += '<li>Costco</li>'
    ul_data += '<li><a href="https://productcentral.mars.com/altoids">'
    ul_data += 'Altoids Official Website</a></li>'
    ul_data += '</ul>'
    return ul_data

# Heading 3
def webh3(string):
    """
    Webpage Heading 3
    """
    heading_string = '<H3 style="font-family: Lucida Console, monospace;">' + string + '</H3>'
    return heading_string

# Paragraph under Heading 3
def paragraph2():
    """
    Webpage Paragraph under Heading 3
    """
    para_data = '<!--Contents for Tic Tac Heading-->'
    para_data += '<p>'
    para_data += 'Tic Tacs! These smaller, smoother candies come in dozens of '
    para_data += 'different flavors, including Peppermint, Orange, Spearmint, and '
    para_data += 'Wintergreen. They were first created in 1968 and have spread to '
    para_data += 'over 100 countries. They knock out bad breath in minutes. '
    para_data += 'Places you can buy it:'
    para_data += '</p>'
    return para_data

# Ordered List under Heading 3
def ordlist():
    """
    Webpage Ordered List under Heading 3
    """
    ol_data = '<ol>'
    ol_data += '<li>Walmart</li>'
    ol_data += '<li>Shoppers</li>'
    ol_data += '<li><a href="https://www.amazon.com/s?k=tic+tacs&i=grocery&ref=nb_sb_noss_2>">'
    ol_data += 'Amazon</a></li>'
    ol_data += '<li><a href="https://www.tictac.com/us/en/">'
    ol_data += 'Tic Tacs Official Website</a></li>'
    ol_data += '</ol>'
    return ol_data

# Current Time
def currenttime():
    """
    Webpage Current Time EST
    """
    eastern = timezone('US/Eastern')
    rightnow = datetime.now(eastern)
    current_time = rightnow.strftime('%H:%M:%S')
    para_data = '<!--Getting Current Time (EST)-->'
    para_data += '<p>'
    para_data += 'The current time (EST) is: ' + current_time
    para_data += '</p>'
    return para_data

# End
def webend():
    """
    Webpage End
    """
    end_data = '</body>'
    end_data += '</html>'
    return end_data

APP.run(host='0.0.0.0', port=8080)
