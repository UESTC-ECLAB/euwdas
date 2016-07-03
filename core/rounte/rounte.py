# -*- coding: utf-8 -*-
import os
import sys
import networkx as nx
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()

from dataset import beijing_data

def hamilton(G):
    F = [(G,[G.nodes()[0]])]
    n = G.number_of_nodes()
    while F:
        graph,path = F.pop()
        confs = []
        for node in graph.neighbors(path[-1]):
            conf_p = path[:]
            conf_p.append(node)
            conf_g = nx.Graph(graph)
            conf_g.remove_node(path[-1])
            confs.append((conf_g,conf_p))
        for g,p in confs:
            if len(p)==n:
                return p
            else:
                F.append((g,p))
    return None

class Rounte(object):
    def __init__(self):
        self.attractions = None
        self.attractions_class = None
        self.section_scores = None

    def route(self, travelList):
        class_travel_set = self.class_travel_list(travelList)

        print class_travel_set
        travel_section = [k for k,v in class_travel_set.items()]
        print travel_section
        travel_section_rank = self.shortest_path(travel_section, self.section_scores)


    def shortest_path(self, travel_list, travel_list_scores):
        DG = nx.DiGraph()
        weighted_edges_from = []
        for i in range(len(travel_list)):
            for j in range(len(travel_list)):
                if travel_list[i] != travel_list[j]:
                    scores = travel_list_scores[travel_list[i]+"_"+travel_list[j]]
                    temp_tuple = (travel_list[i],travel_list[j],scores)
                    weighted_edges_from.append(temp_tuple)
        print weighted_edges_from
        DG.add_weighted_edges_from(weighted_edges_from)
        print DG.nodes()

        print hamilton(DG)


        # print DG





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


if __name__ == '__main__':
    travelList = [u"鸟巢",u"奥林匹克公园",u"北海公园",u"长安街",u"王府井大街",
                    u"颐和园",u"清华大学",u"南锣鼓巷",u"国子监",u"八达岭"]
    b = BeijingRounte()
    b.route(travelList)
    print b

