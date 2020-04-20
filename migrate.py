#!/usr/bin/env python
from app.settings import engine, Base
from app.auth.orm_models import *
from app.courses.orm_models import *

Base.metadata.create_all(engine)