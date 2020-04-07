# -*- coding: utf-8 -*-
"""

@author: larrea
"""

from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch
import json
import os



class searcher(object):
    
    """
    Creates a searcher object using elsapy (https://github.com/ElsevierDev/elsapy)
    
    Attributes: 
    config_path (str): path of the json file containing authentication keys 
    
    """
    
    def __init__(self, config_path='config.json'):
        self.config_path = config_path
        
    def auth(self):
        con_file = open(self.config_path)
        config = json.load(con_file)
        con_file.close()
        
        self.client = ElsClient(config['apikey'])
        self.client.inst_token = config['insttoken']
        
        
    def get_bib(self,EID=None):
        
        EID = int(EID)
        scp_doc = AbsDoc(scp_id = EID)
        scp_doc.read(self.client)
        scp_doc.write()
        bib=[]
        for x in scp_doc.data.get('item').get('bibrecord').get('tail').get('bibliography').get('reference'):
            EID_x = x.get('ref-info').get('refd-itemidlist').get('itemid')[1].get('$')
            bib.append(EID_x)
        return bib
