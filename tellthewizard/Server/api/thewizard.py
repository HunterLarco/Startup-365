from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel

import datetime








class QuickListItem(ndb.Model):
  
  text             = ndb.StringProperty   (indexed=True)
  creation         = ndb.DateTimeProperty (indexed=True, auto_now_add=True)
  notificationtime = ndb.DateTimeProperty(indexed=True)
  
  
  def getAge(self):
    return (datetime.datetime.now()-self.creation).total_seconds()
  
  
  def getTimeToNotification(self):
    return (self.notificationtime-datetime.datetime.now()).total_seconds()
  
  
  @classmethod
  def create(cls, text, notificationtime):
    item = cls()
    
    item.text = text
    item.notificationtime = datetime.datetime.now() + datetime.timedelta(seconds=notificationtime)
    
    item.put()
    return item








class QuickList(polymodel.PolyModel):
  
  NOTIFICATION_TIME = 60*60
  
  phone = ndb.StringProperty(indexed=True)
  items = ndb.StructuredProperty(QuickListItem, repeated=True)
  
  
  def getAllItems(self):
    return self.items
  
  
  def addItem(self, text):
    self.items.append(QuickListItem.create(text, self.NOTIFICATION_TIME))
    self.put()
  
  
  @classmethod
  def exists(cls, phone):
    return cls.get(phone) != None
  
  
  @classmethod
  def createKey(cls, phone):
    return ndb.Key('PhoneNumber', phone)
  
  
  @classmethod
  def create(cls, phone):
    if cls.exists(phone):
      return None
    
    quicklist = cls(parent=cls.createKey(phone))
    
    quicklist.phone = phone
    
    quicklist.put()
    return quicklist
  
  
  @classmethod
  def get(cls, phone):
    return cls.query(ancestor=cls.createKey(phone)).get()







