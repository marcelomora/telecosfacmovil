# -*- encoding: utf-8 -*-

import lexus
import couchdb
from couchdb.mapping import Document, TextField, IntegerField, DateTimeField

class couchdb_manager():
    def get_server(self):
        "Returns a couch database instance"
        couch = couchdb.Server('http://localhost:5984/')
        try:
            db = couch['customers']
        except:
            db = couch.create('customers')
        return db

    def load_customers(self):
        lexusModel = lexus.LexusModel()
        rows = lexusModel.read_all()

        db = self.get_server()
        for row in rows:
            try:
                db.save(row)
            except Exception, e:
                print e

    def get_customer_by_fin(self, fin):
        "Load customer using fin"
        query ="""
        function(doc) {{
            if(doc.nroruc == '{}')
                emit(doc.nroruc, doc);
        }}
        """.format(fin)
        db = self.get_server()
        res = db.query(query)
        try:
            return [r for r in res][0]
        except:
            return {"id":"0", "key":"0", "value":{}}

class Customer(Document):
    cias = IntegerField()
    nroruc = TextField()
    descri1 = TextField()
    descri2 = TextField()
    descri3 = TextField()
    direc1 = TextField()
    direc2 = TextField()
    direc3 = TextField()
    telf1 = TextField()
    telf2 = TextField()
    telf3 = TextField()
    mail = TextField()
    ciudad = TextField()
    vend = IntegerField()

    """

    def __init__(self,dct):
        self.cias = dct['cias']
        self.nroruc = dct['nroruc']
        self.descri1 = dct['descri1']
        self.descri2 = dct['descri2']
        self.descri3 = dct['descri3']
        self.direc1 = dct['direc1']
        self.direc2 = dct['direc2']
        self.direc3 = dct['direc3']
        self.telf1 = dct['telf1']
        self.telf2 = dct['telf2']
        self.telf3 = dct['telf3']
        self.mail = dct['mail']
        self.ciudad = dct['ciudad']
        self.vend = dct['vend']
    """
    def to_dict(self):
        return {
            'cias' : self.cias,
            'nroruc' : self.nroruc,
            'descri1' : self.descri1,
            'descri2' : self.descri2,
            'descri3' : self.descri3,
            'direc1' : self.direc1,
            'direc2' : self.direc2,
            'direc3' : self.direc3,
            'telf1' : self.telf1,
            'telf2' : self.telf2,
            'telf3' : self.telf3,
            'mail' : self.mail,
            'ciudad' : self.ciudad,
            'vend' : self.vend,
        }


if __name__ == '__main__':
    cm = couchdb_manager()
    cm.load_customers()


