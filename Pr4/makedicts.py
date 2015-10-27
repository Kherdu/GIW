def makedicts(cursor, query, params=()):
 cursor.execute(query, params)
 colnames = [desc[0] for desc in cursor.description]
 rowdicts = [dict(zip(colnames, row)) for row in cursor.fetchall()]
 return rowdicts
