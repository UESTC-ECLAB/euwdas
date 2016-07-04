# -*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()
from rounte import BeijingRounte

if __name__ == '__main__':
    travelList = [u"鸟巢",u"奥林匹克公园",u"北海公园",u"长安街",u"王府井大街",
                    u"颐和园",u"清华大学",u"南锣鼓巷",u"国子监",u"八达岭"]
    b = BeijingRounte()
    print b.route(travelList)
    print b