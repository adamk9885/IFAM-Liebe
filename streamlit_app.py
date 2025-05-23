import streamlit as st
from datetime import datetime, timedelta
from basic_functions import page_setup

page_setup()

col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 2, 3])

with col2:
    new_hours = st.selectbox(label="Uhr", index=7,
                             options=["0" + str(t) for t in range(0, 10)] + [str(t) for t in range(10, 24)],
                             key="hours_countdown_timer_selectbox_key")
with col3:
    new_minutes = st.selectbox(label="verborgen", index=0,
                               options=["0" + str(t) for t in range(0, 10)] + [str(t) for t in range(10, 60)],
                               label_visibility="hidden", key="min_countdown_timer_selectbox_key")

ankunftszeit = f"{new_hours}:{new_minutes}"

with col4:
    sonstige_pause = st.number_input(label="Längere Mittagspause? (min)", min_value=30, value=30, step=1)

if sonstige_pause > 30:
    st.toast("Wow, du liebst das IFAM nicht")

col1, col2, col3 = st.columns([3, 4, 3])

with col2:
    if st.button(label="Rechnen", use_container_width=True):
        ankunftszeit_timedelta = timedelta(hours=int(new_hours), minutes=int(new_minutes))
        sonstige_pause_timedelta = timedelta(minutes=sonstige_pause)

        sechsstdzeit_delta = timedelta(hours=6)
        normalzeit_delta = timedelta(hours=8, minutes=18)
        neunstd_delta = timedelta(hours=9, minutes=30)
        maxzeit_delta = timedelta(hours=10, minutes=45)

        if sonstige_pause > 30:
            abweichung = sonstige_pause_timedelta - timedelta(minutes=30)
        else:
            abweichung = timedelta(minutes=0)

        sechsstdzeit = ankunftszeit_timedelta + sechsstdzeit_delta
        normalzeit = ankunftszeit_timedelta + normalzeit_delta + abweichung
        neunstd = ankunftszeit_timedelta + neunstd_delta + abweichung
        maxzeit = ankunftszeit_timedelta + maxzeit_delta + abweichung

        sechsstdzeit_time = (datetime.min + sechsstdzeit).time()
        normalzeit_time = (datetime.min + normalzeit).time()
        neunstd_time = (datetime.min + neunstd).time()
        maxzeit_time = (datetime.min + maxzeit).time()

        st.subheader(f":red[{sechsstdzeit_time.strftime("%H:%M")}] \u2192 Mindestleistung")
        st.subheader(f":red[{normalzeit_time.strftime("%H:%M")}] \u2192 genau 7,8std. Nichts mehr, nichts weniger. Du bist durchschnittlich")
        st.subheader(f":red[{neunstd_time.strftime("%H:%M")}] \u2192 9std, Zeit zu fliehen")
        st.subheader(f":red[{maxzeit_time.strftime("%H:%M")}] \u2192 Max-Leistung")


    # aktuelle_zeit = datetime.now().time()
    #
    # ankunftszeit_minutes = ankunftszeit.hour * 60 + ankunftszeit.minute
    # aktuelle_zeit_minutes = aktuelle_zeit.hour * 60 + aktuelle_zeit.minute
    #
    # zeit_geleistet_minuten = aktuelle_zeit_minutes - ankunftszeit_minutes
    #
    # hours = zeit_geleistet_minuten // 60
    # minutes = zeit_geleistet_minuten % 60
    #
    # # st.subheader(f"Bisher hast du :red[{hours} Stunden] und :red[{minutes} Minuten] gearbeitet")
