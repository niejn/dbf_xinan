'''
def copy_range(source, destination, field_name, start, end):
    src = dbf.Table(source).open()
    dst = src.new(destination).open(dbf.READ_WRITE)  # copy structure
    for record in src:
        if start <= record[field_name] <= end:
            dst.append(record)
    src.close()
    dst.close()
def writeDbf(self, path):
    temphead = {}
    temphead['结算会员号'] = str(self.__account)
    table = dbf.Table(path)
    table.open()
    copyTable = table.new('./output/' + self.__account + '_' + self.__mydate + '_settlementdetail.dbf')
    copyTable.open()

    rowVals = self.__genTable

    for oneRow in rowVals:
        tempRecord = []
        for data in oneRow:
            tempRecord.append(str(data))
        if Gdebug:
            print(tuple(tempRecord))
        # table.append(tuple(tempRecord))
        copyTable.append(tuple(tempRecord))
        # tempRecord.clear()

    copyTable.close()
    table.close()

    return

    for datum in (
  61                  ('John Doe', 31, dbf.Date(1979, 9,13)),
  62                  ('Ethan Furman', 102, dbf.Date(1909, 4, 1)),
  63                  ('Jane Smith', 57, dbf.Date(1954, 7, 2)),
  64                  ('John Adams', 44, dbf.Date(1967, 1, 9)),
  65                  ):
  66              table.append(datum)
'''
import dbf
def copy_dbf(src, dst):
    # src = dbf.Table(source).open()
    # dst = src.new(destination).open(dbf.READ_WRITE)  # copy structure
    dst = dst.open(mode=dbf.READ_WRITE)
    for record in src:
        dst.append(record)
    src.close()
    dst.close()

def main(path='./data/2641_SG01_20180424_1_Trade.dbf'):

    table = dbf.Table(path,codepage='cp936')
    print(table.codepage)
    table.open()
    copyTable = table.new( './testing_Trade.dbf')
    # copyTable.open(mode=dbf.READ_WRITE)
    copy_dbf(table, copyTable)
    copyTable.open(mode=dbf.READ_WRITE)
    # record.name, record.birth, record.age
    # ['partid', 'clientid', 'instrid', 'tradeid', 'tvolume', 'tprice', 'tamt', 'ttime', 'direction', 'offsetflag', 'orderid', 'userid']

    datum = ('0', '1', 'test', '2', '3', '4', '5','15:22:12', 'buy', 'open', '0', '0' )
    copyTable.append(datum)
    copyTable.close()

    # headers = ['partid', 'clientid', 'instrid', 'tradeid', 'tvolume', 'tprice', 'tamt', 'ttime', 'direction',
    #            'offsetflag', 'orderid', 'userid']
    # for record in table:
    #     for header in headers:
    #         try:
    #             print(record[header])
    #         except Exception as e:
    #             print(e)
    return

if __name__ == '__main__':
    main()