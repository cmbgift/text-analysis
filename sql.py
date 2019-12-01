"""
一般 Python 用于连接 MySQL 的工具：pymysql
"""
import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='123456',
                             db='jd_skus')
import pandas as pd

cur = connection.cursor()

# 保存skus
def insert_skus(SKU_ID, SKU_INTRODUCE, SKU_SIZE, SKU_PRICE,SKU_LABEL,SKU_TITLE,SKU_COMMENT_NUMS,SKU_GOOD_RATE):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `skus1` (`SKU_ID`, `SKU_INTRODUCE`, `SKU_SIZE`,`SKU_PRICE`, `SKU_LABEL`, `SKU_TITLE`, `SKU_COMMENT_NUMS`, `SKU_GOOD_RATE`) VALUES (%s, %s, %s,%s, %s, %s,%s, %s)"
        cursor.execute(sql, (SKU_ID, SKU_INTRODUCE, SKU_SIZE, SKU_PRICE,SKU_LABEL,SKU_TITLE,SKU_COMMENT_NUMS,SKU_GOOD_RATE))
    connection.commit()
# 保存skus labels
def insert_skus_label(SKU_ID,SHOP_SCORE, SKU_LABEL1, SKU_LABEL3, SKU_LABEL5,SKU_LABEL7):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `skus_label` (`SKU_ID`, `SHOP_SCORE`,`SKU_LABEL1`, `SKU_LABEL3`,`SKU_LABEL5`, `SKU_LABEL7`) VALUES (%s, %s, %s, %s,%s, %s)"
        cursor.execute(sql, (SKU_ID, SHOP_SCORE,SKU_LABEL1, SKU_LABEL3, SKU_LABEL5,SKU_LABEL7))
    connection.commit()


# 保存音乐
def insert_music(music_id, music_name, album_id,record_company,music_intro):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `musics` (`MUSIC_ID`, `MUSIC_NAME`, `ALBUM_ID`,`ALBUM_PUB_COMPANY`, `MUSIC_INTRO`) VALUES (%s, %s, %s,%s,%s)"
        cursor.execute(sql, (music_id, music_name, album_id,record_company,music_intro))
    connection.commit()


# 保存专辑
def insert_album(album_id, artist_id,album_name,album_pub_date):#albume_id, artist_id,albums_name,albums_time
    with connection.cursor() as cursor:
        sql = "INSERT INTO `albums` (`ALBUM_ID`, `ARTIST_ID`,`ALBUM_NAME`, `ALBUM_PUB_DATE`) VALUES (%s, %s,%s, %s)"
        cursor.execute(sql, (album_id, artist_id,album_name,album_pub_date))
    connection.commit()


# 保存歌手
def insert_artist(artist_id, artist_name,v):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `artists` (`ARTIST_ID`, `ARTIST_NAME`,`ARTIST_CATE`) VALUES (%s, %s,%s)"
        cursor.execute(sql, (artist_id, artist_name,v))
    connection.commit()


# 获取所有歌手的 ID
def get_all_artist():
    with connection.cursor() as cursor:
        sql = "SELECT `ARTIST_ID` FROM `artists` ORDER BY ARTIST_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()


# 获取所有专辑的 ID
def get_all_album():
    with connection.cursor() as cursor:
        sql = "SELECT `ALBUM_ID` FROM `albums` ORDER BY ALBUM_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()


# 获取所有音乐的 ID
def get_all_music():
    with connection.cursor() as cursor:
        sql = "SELECT `MUSIC_ID` FROM `musics` ORDER BY MUSIC_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()

# 获取所有音乐的 ID
def get_all_music_csv():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `musics_info` ORDER BY MUSIC_ID"
        cursor.execute(sql, ())
        result=cursor.fetchall()
    musics=[]
    print(len(result))
    for music in result:
        tmp={"MUSIC_ID":music[0],
             "WRITE_MUSIC":music[1],
             "WRITE_WORDS":music[2],
             "MUSIC_NAME":music[3],
             "ALBUM_PUB_COMPANY":music[5],
             "MUSIC_INTRO":music[6],
             "song_url":"http://music.163.com/song?id="+str(music[0]),
             "ALBUM_url":"http://music.163.com/artist/album?id="+str(music[4]),
             "ALBUM_ID":music[4]}
        musics.append(tmp)
    import pandas as pd
    pd.DataFrame(musics)[:1000].to_csv("musics_min.csv",index=None,encoding='utf-8')
    # pd.DataFrame(musics).to_csv("musics.csv",index=None)
# 获取前一半音乐的 ID
def get_before_music():
    with connection.cursor() as cursor:
        sql = "SELECT `MUSIC_ID` FROM `musics` ORDER BY MUSIC_ID LIMIT 0, 800000"
        cursor.execute(sql, ())
        return cursor.fetchall()



# 获取后一半音乐的 ID
def get_after_music():
    with connection.cursor() as cursor:
        sql = "SELECT `MUSIC_ID` FROM `musics` ORDER BY MUSIC_ID LIMIT 800000, 1197429"
        cursor.execute(sql, ())
        return cursor.fetchall()


def dis_connect():
    connection.close()
if __name__ == '__main__':

    arr_skus=[]


    with connection.cursor() as cursor:
        sql = "select * from skus"
        cursor.execute(sql, ())
        result=cursor.fetchall()#查看歌手总个数

        for item in result:
             sku={}
             sku["SKU_ID"]=item[0]
             sku["SKU_INTRODUCE"]=item[1]
             sku["SKU_SIZE"]=item[2]
             sku["SKU_PRICE"]=item[3]
             sku["SKU_LABEL" ]=item[4]
             sku["SKU_TITLE" ]=item[5]
             sku["SKU_COMMENT_NUMS"]=item[6]
             sku["SKU_GOOD_RATE"]=item[7]
             arr_skus.append(sku)

    with connection.cursor() as cursor:
        sql = "select * from skus1 "
        cursor.execute(sql, ())
        result=cursor.fetchall()#查看歌手总个数

        for item in result:
             sku={}
             sku["SKU_ID"]=item[0]
             sku["SKU_INTRODUCE"]=item[1]
             sku["SKU_SIZE"]=item[2]
             sku["SKU_PRICE"]=item[3]
             sku["SKU_LABEL" ]=item[4]
             sku["SKU_TITLE" ]=item[5]
             sku["SKU_COMMENT_NUMS"]=item[6]
             sku["SKU_GOOD_RATE"]=item[7]
             arr_skus.append(sku)
    pd.DataFrame(arr_skus).to_excel("Gift2.xlsx")