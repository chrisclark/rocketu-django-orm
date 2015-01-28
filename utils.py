import sqlparse

def sqlf(sql):
    return sqlparse.format(sql, reindent=True, keyword_case='upper')

def qsf(qs):
    return sqlf(str(qs))


