import streamlit as st
from datetime import datetime, timedelta, time

st.set_page_config(layout="wide")

st.title("IFAM LIEBE")

ankunftszeit = st.time_input(label="Ankunftszeit", step=60)

if st.button(label="Rechnen"):
    ankunftszeit_timedelta = timedelta(hours=ankunftszeit.hour, minutes=ankunftszeit.minute)

    normalzeit_delta = timedelta(hours=8, minutes=18)
    neunstd_delta = timedelta(hours=9, minutes=30)
    maxzeit_delta = timedelta(hours=10, minutes=45)

    normalzeit = ankunftszeit_timedelta + normalzeit_delta
    neunstd = ankunftszeit_timedelta + neunstd_delta
    maxzeit = ankunftszeit_timedelta + maxzeit_delta

    normalzeit_time = (datetime.min + normalzeit).time()
    neunstd_time = (datetime.min + neunstd).time()
    maxzeit_time = (datetime.min + maxzeit).time()

    st.subheader(f"Um {normalzeit_time.strftime("%H:%M")} Uhr hast du einen ganzen Tag (7,8std) gearbeitet")
    st.subheader(f"Um {neunstd_time.strftime("%H:%M")} Uhr hast du 9Std gearbeitet, pass auf, wenn du jetzt gehen kannst, geh. Ansonsten zählen die nächste 15Min nicht.")
    st.subheader(f"{maxzeit_time.strftime("%H:%M")} Uhr ist max-Leistung")
