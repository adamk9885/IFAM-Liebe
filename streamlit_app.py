import streamlit as st
from datetime import datetime, timedelta, time

st.set_page_config(layout="wide")

st.title("IFAM LIEBE")

col1, col2 = st.columns(2)

with col1:
    ankunftszeit = st.time_input(label="Ankunftszeit", step=60)
with col2:
    sonstige_pause = st.number_input(label="Längere Mittagspause? (min)", min_value=30, value=30, step=1)

if sonstige_pause > 60:
    st.toast("Wow, du liebst das IFAM nicht")

if st.button(label="Rechnen"):
    ankunftszeit_timedelta = timedelta(hours=ankunftszeit.hour, minutes=ankunftszeit.minute)
    sonstige_pause_timedelta = timedelta(minutes=sonstige_pause)
    
    normalzeit_delta = timedelta(hours=8, minutes=18)
    neunstd_delta = timedelta(hours=9, minutes=30)
    maxzeit_delta = timedelta(hours=10, minutes=45)

    if sonstige_pause > 30:
        abweichung = sonstige_pause_timedelta - timedelta(minutes=30)
    else:
        abweichung = timedelta(minutes=0)
    
    normalzeit = ankunftszeit_timedelta + normalzeit_delta + abweichung
    neunstd = ankunftszeit_timedelta + neunstd_delta + abweichung
    maxzeit = ankunftszeit_timedelta + maxzeit_delta + abweichung

    normalzeit_time = (datetime.min + normalzeit).time()
    neunstd_time = (datetime.min + neunstd).time()
    maxzeit_time = (datetime.min + maxzeit).time()

    st.subheader(f"Um :red[{normalzeit_time.strftime("%H:%M")}] Uhr hast du einen ganzen Tag (7,8std) gearbeitet")
    st.subheader(f"Um :red[{neunstd_time.strftime("%H:%M")}] Uhr hast du 9Std gearbeitet, pass auf, wenn du jetzt gehen kannst, geh. Ansonsten zählen die nächsten 15 Min nicht.")
    st.subheader(f":red[{maxzeit_time.strftime("%H:%M")}] Uhr ist max-Leistung")

    aktuelle_zeit = datetime.now().time()

    ankunftszeit_minutes = ankunftszeit.hour * 60 + ankunftszeit.minute
    aktuelle_zeit_minutes = aktuelle_zeit.hour * 60 + aktuelle_zeit.minute

    zeit_geleistet_minuten = aktuelle_zeit_minutes - ankunftszeit_minutes

    hours = zeit_geleistet_minuten // 60
    minutes = zeit_geleistet_minuten % 60

    # st.subheader(f"Bisher hast du :red[{hours} Stunden] und :red[{minutes} Minuten] gearbeitet")
