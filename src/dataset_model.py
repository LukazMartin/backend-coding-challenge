from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, JSON

Base = declarative_base()


class Planning(Base):

    __tablename__ = 'planning'

    id = Column(Integer(), primary_key=True)
    originalId = Column(String(255), unique=True, nullable=False)
    talentId = Column(String(255))
    talentName = Column(String(255))
    talentGrade = Column(String(255))
    bookingGrade = Column(String(255))
    operatingUnit = Column(String(255))
    officeCity = Column(String(255))
    officePostalCode = Column(String(255))
    jobManagerName = Column(String(255))
    jobManagerId = Column(String(255))
    totalHours = Column(Float(), nullable=False)
    startDate = Column(DateTime(), nullable=False)
    endDate = Column(DateTime(), nullable=False)
    clientName = Column(String(255))
    clientId = Column(String(255), nullable=False)
    industry = Column(String(255))
    isUnassigned = Column(Boolean())
    requiredSkills = Column(JSON)
    optionalSkills = Column(JSON)

    def __init__(self, record):
        self.id = record['id']
        self.originalId = record['originalId']
        self.talentId = record['talentId']
        self.talentName = record['talentName']
        self.talentGrade = record['talentGrade']
        self.bookingGrade = record['bookingGrade']
        self.operatingUnit = record['operatingUnit']
        self.officeCity = record['officeCity']
        self.officePostalCode = record['officePostalCode']
        self.jobManagerName = record['jobManagerName']
        self.jobManagerId = record['jobManagerId']
        self.totalHours = record['totalHours']
        self.startDate = datetime.strptime(record['startDate'], '%m/%d/%Y %I:%M %p')
        self.endDate = datetime.strptime(record['endDate'], '%m/%d/%Y %I:%M %p')
        self.clientName = record['clientName']
        self.clientId = record['clientId']
        self.industry = record['industry']
        self.isUnassigned = record['isUnassigned']
        self.requiredSkills = record['requiredSkills']
        self.optionalSkills = record['optionalSkills']

