import streamlit as st
import joblib


def main():

    st.title("I-WUNDER Demo")
    estimator_loaded = joblib.load("./randomforest_with_advertising.pkl")

    text_TV = st.number_input('Geben Sie einen TV-Werbepreis ein')
    text_Radio = st.number_input('Geben Sie einen Preis für Radiowerbung ein')
    text_Newspaper = st.number_input('Geben Sie einen Zeitungsanzeigenpreis ein')
    X=[[text_TV, text_Radio, text_Newspaper]]

    estimator_loaded = joblib.load("./randomforest_with_advertising.pkl")
    prediction = round(estimator_loaded.predict(X)[0],3)

    #alcohol = st.slider("Alcohol", 8, 15)
    if st.button('Einschätzung'):
        st.title(prediction)


if __name__ == '__main__':
    main()
