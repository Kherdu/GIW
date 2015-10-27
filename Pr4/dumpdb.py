def showformat(recs, sept=('-' * 40), sept2=('*'*40)):
    print len(recs), 'registros'
    print sept
    for rec in recs:
        maxkey = max(len(key) for key in rec)
        for key in rec: # or: \t align
            print '%-*s => %s' % (maxkey, key, rec[key])
            print sept
        print sept2

def dumpdb(cursor, table, format=True):
    if not format:
        cursor.execute('select * from ' + table)
        while True:
            rec = cursor.fetchone()
            if not rec: break
            print rec
    else:
        from makedicts import makedicts
        recs = makedicts(cursor, 'select * from ' + table)
        showformat(recs)

if __name__ == '__main__':
    import sys
    cmdargs = sys.argv[1:]
    if '-' in cmdargs:
        format = True
        cmdargs.remove('-')
    dbname = cmdargs.pop(0)
    table = cmdargs[0]
    from loaddb import login
    conn, curs = login(dbname)
    dumpdb(curs, table, format)
