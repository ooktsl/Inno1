import streamlit as st
import joblib
import database
import models
import psycopg2
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


#engine = create_engine(database.SQLALCHEMY_DATABASE_URL)
#models.Base.metadata.create_all(bind=engine)
#Session = sessionmaker(bind=engine)
#s = Session()

#def init_connection():
#    return psycopg2.connect(**st.secrets["postgres"])

#conn = init_connection()


# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
#@st.experimental_memo(ttl=600)
#def run_query(query):
#    with conn.cursor() as cur:
#        cur.execute(query)
#        return cur.fetchall()



def main():
    st.title("I-WUNDER Entwicklung & Innovation")
    estimator_loaded = joblib.load("./randomforest_with_advertising.pkl")

    TV = st.number_input('Geben Sie einen TV-Werbepreis ein', max_value=500, min_value=0)
    Radio = st.number_input('Geben Sie einen Preis für Radiowerbung ein', max_value=500, min_value=0)
    Newspaper = st.number_input('Geben Sie einen Zeitungsanzeigenpreis ein', max_value=500, min_value=0)
    X = [[TV, Radio, Newspaper]]

    estimator_loaded = joblib.load("./randomforest_with_advertising.pkl")
    prediction = round(estimator_loaded.predict(X)[0], 3)

    #alcohol = st.slider("Alcohol", 8, 15)
    if st.button('Einschätzung'):
        st.title(prediction)
        st.balloons()
        #entry = models.Customer(TV=TV, Radio=Radio, Newspaper=Newspaper, Sales=prediction)
        #s.add(entry)
        #s.commit()
        #st.success("Einschätzung wurde eingefügt")


if __name__ == '__main__':
    main()
