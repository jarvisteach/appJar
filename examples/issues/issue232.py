import sys
sys.path.append("../../")
from appJar import gui
from sqlalchemy import create_engine, select, Column, Integer, Text, MetaData, Table, Boolean, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

app = gui("Test SQL Alch (ORM GUI)", "600x600")
app.setBg("#FF9D40")

engine = create_engine('sqlite:///:memory:')

Base = declarative_base()
Session = sessionmaker(bind=engine)

class Money(Base):
    __tablename__ = 'money'
    md5hash = Column(String, primary_key=True)
    category = Column(String)
    verified = Column(Boolean)
    booked = Column(Date)
    valuta = Column(Date)
    issuer = Column(String)
    receiver = Column(String)
    account_nr = Column(String)
    iban = Column(String)
    blz = Column(String)
    bic = Column(String)
    reference = Column(String)
    comment = Column(String)
    currency = Column(String)
    amount = Column(String)
    type = Column(String)

    def __repr__(self):
        return "<Money(md5='%s', amount='%s', date='%s')>" % (
            self.md5hash, self.amount, self.booked)

session = Session()

Base.metadata.create_all(engine)
for n in range(25):
    session.add(Money(md5hash="test"+str(n), amount=n, comment="test", verified=False, 
        receiver="rec"+str(n), reference="ref"+str(n), booked=datetime.now(), type="S"))
session.commit()

def press(row):
    print(all_money[row])

all_money = []

def runQuery():
    data = [["booked", "receiver", "reference", "comment", "amnt", "type"]]
    query = session.query(Money).filter(Money.verified != None)
    if len(app.getEntry("receiver"))>0:
        query = query.filter(Money.receiver.like("%"+app.getEntry("receiver")+"%"))
    else:
        query = query.limit(25)
    all_money = query.all()
    for m in all_money:
        data.append([m.booked, m.receiver[:14], m.reference[:18], m.comment[:10], m.amount, m.type])
    app.addGrid("g1", data, action=press, row=1)

def submit(obj):
    app.removeGrid("g1")
    runQuery()

app.setStretch("none")
app.addLabelEntry("receiver")
app.setEntrySubmitFunction("receiver", submit)
app.setFocus("receiver")
app.setStretch("both")
runQuery()

app.go()

