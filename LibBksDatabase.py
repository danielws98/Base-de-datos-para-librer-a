import sqlite3

def ConnectData():
    con=sqlite3.connect("libbooks.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS libbooks (id INTEGER PRIMARY KEY, MTY text, Ref text, Tit text,fna text, \
        sna text, Adr1 text,Adr2 text,pcd text,MNo text,BkID text,BKt text,Atr text,Dbo text,Ddu text, sPr text, \
        Lrf text,Dod text,DonL text)")
    con.commit()
    con.close()

def AddDataRec(MTy,Ref,Tit,fna,sna,Adr1,Adr2,pcd,MNo,BkID,BKt,Atr,Dbo,Ddu, sPr,Lrf,Dod,DonL):
    con=sqlite3.connect("libbooks.db")
    cur=con.cursor()
    cur.execute("INSERT INTO libbooks VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",\
        (MTy,Ref,Tit,fna,sna,Adr1,Adr2,pcd,MNo,BkID,BKt,Atr,Dbo,Ddu, sPr,Lrf,Dod,DonL))
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("libbooks.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM libbooks")
    rows=cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con=sqlite3.connect("libbooks.db")
    cur=con.cursor()
    cur.execute("DELETE  FROM libbooks  WHERE id=?",(id,))
    con.commit()
    con.close()

def searchData(MTy="",Ref="",Tit="",fna="",sna="",Adr1="",Adr2="",pcd="",\
    MNo="",BkID="",BKt="",Atr="",Dbo="",Ddu="", sPr="",Lrf="",Dod="",DonL=""):
    con=sqlite3.connect("libbooks.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM  libbooks WHERE MTy=? OR Ref=? OR Tit=? OR fna=? OR sna=? OR Adr1=? OR \
        Adr2=? OR pcd=? OR MNo=? OR BkID=? OR BKt=? OR Atr=? OR Dbo=? OR Ddu=? OR  sPr=? OR Lrf=? OR Dod=? OR DonL=?",\
         (MTy,Ref,Tit,fna,sna,Adr1,Adr2,pcd,MNo,BkID,BKt,Atr,Dbo,Ddu, sPr,Lrf,Dod,DonL))
    rows=cur.fetchall()
    con.close()
    return rows

def DataUpdate(id,MTy="",Ref="",Tit="",fna="",sna="",Adr1="",Adr2="",pcd="",\
    MNo="",BkID="",BKt="",Atr="",Dbo="",Ddu="", sPr="",Lrf="",Dod="",DonL=""):
    con=sqlite3.connect("libbooks.db")
    cur=con.cursor()
    cur.execute("UPDATE libbooks SET MTy=?,Ref=?,Tit=?,fna=?,sna=?,Adr1=?, \
        Adr2=? OR pcd=?,MNo=?,BkID=?,BKt=?,Atr=?,Dbo=?,Ddu=?,sPr=?,Lrf=?,Dod=?,DonL=? ",
        (id,MTy,Ref,Tit,fna,sna,Adr1,Adr2,pcd,MNo,BkID,BKt,Atr,Dbo,Ddu, sPr,Lrf,Dod,DonL))
    con.commit()
    con.close()
    
ConnectData()