import db_connect as db


def search_postkey(postkey):
    query = "SELECT COUNT(*) as count FROM Band WHERE post_id='" + postkey + "';"
    # print("query = " + query)
    db.cursor.execute(query)
    result = db.cursor.fetchall()
    # print(result[0]['count'])
    # for row in result:
    #     print("count : " + str(row["count"]))
    return result[0]['count']


def insertPost(postkey, createdate):
    query = "INSERT INTO Band (date, post_id) VALUES ('%s', '%s');" % (createdate, postkey)
    print(query)
    db.cursor.execute(query)

    db.conn.commit()

def afterSend():
    query = "UPDATE BAND SET isAlert = 1;"
    print(query)
    db.cursor.execute(query)

    db.conn.commit()