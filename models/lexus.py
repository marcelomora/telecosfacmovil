# -*- encoding: utf-8 -*-
import ConfigParser
import pyodbc

class MSSQLModel():
    def __init__(self):
        self.readConfig()
        self.conn_string = \
            'DSN={dsn};UID={uid};PWD={pwd};DATABASE={database};'.format(
                    dsn=self.dsn, uid=self.user, pwd=self.password,
                    database=self.database)
        self.cnxn = pyodbc.connect(self.conn_string)


    def readConfig(self):
        config = ConfigParser.ConfigParser()
        config.read("/home/marcelo/lexusfacmovil.conf")
        self.dsn = config.get("SqlServer", "dsn")
        self.user = config.get("SqlServer", "user")
        self.password = config.get("SqlServer", "password")
        self.database = config.get("SqlServer", "database")

    def read_sql(self, sql, params=()):
        """
        @params list: List of params for sql query
        """
        """Execute command in database"""
        cr = self.cnxn.cursor()
        return cr.execute(sql, params)

class LexusModel(MSSQLModel):
    def read_by_fin(self, fin):
        sql = """
        select CLIE_CIAS, CLIE_NRORUC, CLIE_DESCRI1, CLIE_DESCRI2, CLIE_DESCRI3,
        CLIE_DIREC1, CLIE_DIREC2, CLIE_DIREC3, CLIE_TELF1, CLIE_TELF2, CLIE_TELF3,
        CLIE_MAIL, CLIE_CIUDAD, CLIE_VEND
        from sco$tclientes
        where CLIE_NRORUC = ?
        """

        customer_row = self.read_sql(sql, (fin,))
        row = customer_row.fetchall()[0]
        return {'cias' : row[0],
                'nroruc' : row[1],
                'descri1' : row[2],
                'descri2' : row[3],
                'descri3' : row[4],
                'direc1' : row[5],
                'direc2' : row[6],
                'direc3' : row[7],
                'telf1' : row[8],
                'telf2' : row[9],
                'telf3' : row[10],
                'mail' : row[11],
                'ciudad' : row[12],
                'vend' : row[13],
                }

    def read_all(self):
        sql = """
        select CLIE_CIAS, CLIE_NRORUC, CLIE_DESCRI1, CLIE_DESCRI2, CLIE_DESCRI3,
        CLIE_DIREC1, CLIE_DIREC2, CLIE_DIREC3, CLIE_TELF1, CLIE_TELF2, CLIE_TELF3,
        CLIE_MAIL, CLIE_CIUDAD, CLIE_VEND
        from sco$tclientes
        where CLIE_CIAS = 1000
        """

        customer_row = self.read_sql(sql)
        result = []
        for row in customer_row.fetchall():
            result.append(
                 {'cias' : row[0],
                'nroruc' : row[1],
                'descri1' : row[2].decode('cp1252'),
                'descri2' : row[3].decode('cp1252'),
                'descri3' : row[4].decode('cp1252'),
                'direc1' : row[5].decode('cp1252'),
                'direc2' : row[6].decode('cp1252'),
                'direc3' : row[7].decode('cp1252'),
                'telf1' : row[8],
                'telf2' : row[9],
                'telf3' : row[10],
                'mail' : row[11],
                'ciudad' : row[12],
                'vend' : row[13],
                }
            )
        return result



if __name__ == "__main__":
    model = LexusModel()
    print model.read_by_fin('0100080373')

