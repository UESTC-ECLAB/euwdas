# -*- coding: utf-8 -*-
import os
import sys
import networkx as nx
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()

from dataset import beijing_data
import tsp

class Rounte(object):
    def __init__(self):
        self.attractions = None
        self.attractions_class = None
        self.section_scores = None
        self.every_section_socres = None
        self.every_section_socres_range = None

    def route(self, travelList):
        class_travel_set = self.class_travel_list(travelList)

        print class_travel_set
        travel_section = [k for k,v in class_travel_set.items()]
        # print travel_section
        travel_section_rank = self.tsp_path(travel_section, self.section_scores)
        print travel_section_rank
        class_travel_rank = {}
        for k,v in class_travel_set.items():
            every_section_socres = self.every_section_socres[self.every_section_socres_range[k]]
            class_travel_rank[k] = self.tsp_path(v, every_section_socres)
        print class_travel_rank


    def tsp_path(self, travel_list, travel_list_scores):
        DG = nx.DiGraph()
        weighted_edges_from = []
        for i in range(len(travel_list)):
            for j in range(len(travel_list)):
                if travel_list[i] != travel_list[j]:
                    if travel_list_scores.has_key(travel_list[i]+"_"+travel_list[j]):
                        scores = travel_list_scores[travel_list[i]+"_"+travel_list[j]]
                        temp_tuple = (travel_list[i],travel_list[j],-scores)
                        weighted_edges_from.append(temp_tuple)
                    else:
                        weighted_edges_from.append((travel_list[i],travel_list[j],100))
        DG.add_weighted_edges_from(weighted_edges_from)

        sol = 0.0
        rounte = []
        for i in range(len(travel_list)):
            temp_sol = tsp.greedy_tsp(DG, travel_list[i])
            if abs(temp_sol[1]) > sol:
                sol = abs(temp_sol[1])
                rounte = temp_sol[0]

        def fix(rounte):
            fix_rounte = []
            for i in range(len(rounte)):
                if i == 0:
                    fix_rounte.extend([rounte[i][0],rounte[i][1]])
                else:
                    fix_rounte.append(rounte[i][1])
            return fix_rounte
        # print fix(rounte)
        return fix(rounte)



    def class_travel_list(self, travelList):
        '''
        mean to classify the given travelList
        '''
        class_travel_set = {}
        attractions_class = self.attractions_class
        for i in range(len(travelList)):
            section_name = attractions_class[travelList[i]]
            if section_name in class_travel_set:
                temp_list = class_travel_set[section_name]
                temp_list.append(travelList[i])
                class_travel_set[section_name] = temp_list
            else:
                class_travel_set[section_name] = [travelList[i]]
        return class_travel_set


class BeijingRounte(Rounte):
    def __init__(self):
        self.attractions = beijing_data["attractions"]
        self.attractions_class = beijing_data["attractions_class"]
        self.section_scores = beijing_data["scores"]["section_scores"]
        self.every_section_socres = beijing_data["scores"]["every_section_socres"]
        self.every_section_socres_range = beijing_data["scores"]["every_section_socres_range"]


if __name__ == '__main__':
    travelList = [u"鸟巢",u"奥林匹克公园",u"北海公园",u"长安街",u"王府井大街",
                    u"颐和园",u"清华大学",u"南锣鼓巷",u"国子监",u"八达岭"]
    b = BeijingRounte()
    b.route(travelList)
    print b

