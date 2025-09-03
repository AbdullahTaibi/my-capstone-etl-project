import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import date, timedelta
from sqlalchemy import create_engine
from src.extract.extract import extract_global_flights

