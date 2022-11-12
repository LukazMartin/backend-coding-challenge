from fastapi import FastAPI
from src.dataset_model import Planning
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from typing import Optional
from sqlalchemy import desc, asc

app = FastAPI()

engine = create_engine('sqlite:///planning.bd')
Session = sessionmaker(engine)
session = Session()


@app.get('/filtering')
def filter_records(talentGrade: Optional[str] = None, officeCity: Optional[str] = None, clientName: Optional[str] = None,
                   isUnassigned: Optional[bool] = None, industry: Optional[str] = None):
    """
        Call this method with the filter parameters in the url.
        Example: localhost/filtering?talentGrade=Intern&isUnassigned=false
    """

    variables = locals().copy()
    result = session.query(Planning)
    for var in variables:
        if locals()[var] is not None:
            result = result.filter(getattr(Planning, var) == locals()[var])
    return {'records': [rec for rec in result]}


@app.get('/sorting')
def sort_records(clientId: Optional[str] = None, startDate: Optional[str] = None, endDate: Optional[str] = None):
    """
        Call this method with the sorting parameters in the url.
        Example: localhost/sorting?clientId=cl_1&startDate=asc
    """

    if clientId is None:
        return {"No clientId parameter found."}
    result = session.query(Planning).filter(Planning.clientId == clientId)

    if startDate == 'asc':
        result = result.order_by(asc(Planning.startDate))
    elif startDate == 'desc':
        result = result.order_by(desc(Planning.startDate))
    elif endDate == 'asc':
        result = result.order_by(asc(Planning.endDate))
    elif endDate == 'desc':
        result = result.order_by(desc(Planning.endDate))
    else:
        return {"Add sorting parameters to url. Example: /sorting?clientId=someId&startDate=asc"}
    return {'records': [rec for rec in result]}


@app.get('/pagination')
def pagination(page_num: int = 1, page_size: int = 10):
    """
        Call this method for pagination of all records.
        Example: localhost/pagination?page_num=1&page_size=10
    """
    start = (page_num - 1) * page_size
    end = start + page_size

    result = [rec for rec in session.query(Planning)[start:end]]
    total = session.query(Planning).count()

    response = {
        "data": result,
        "total": total,
        "count": page_size,
        "pagination": {}
    }

    if end >= total:
        response["pagination"]["next"] = None
    else:
        response["pagination"]["next"] = f'/pagination?page_num={page_num+1}&page_size={page_size}'

    if page_num > 1:
        response["pagination"]["previous"] = f'/pagination?page_num={page_num}&page_size={page_size}'
    else:
        response["pagination"]["previous"] = None

    return response
