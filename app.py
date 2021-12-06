import streamlit as st
import pandas as pd

dfHouryRates = pd.read_csv('hourly_rates.csv')
profession = dfHouryRates["Profession"].unique()

dfCountryMultipliers = pd.read_csv('country_multipliers.csv')
country = dfCountryMultipliers["Countries & Regions"].unique()

dfAgeMultipliers = pd.read_csv('age_multipliers.csv')
age = dfAgeMultipliers["Age Ranges"].unique()

dfGenderMultipliers = pd.read_csv('gender_multipliers.csv')
gender = dfGenderMultipliers["Gender"].unique()


st.title("Hourly Rate Calculator")
st.write("Based on Rimuut freelancer data and some calculations you may calculate optimal rates")
inputAgeMultiplier = 1
inputCategoryMultiplier = 1
inputCountryMultiplier = 1
inputGenderMultiplier = 1
inputCategory = st.selectbox("Profession", sorted(profession))
if inputCategory:
    inputCategoryMultiplier = dfHouryRates[dfHouryRates["Profession"] == inputCategory].values[0][1]

inputCountry = st.selectbox("Countries & Regions", sorted(country))
if inputCountry:
    inputCountryMultiplier = dfCountryMultipliers[dfCountryMultipliers["Countries & Regions"] == inputCountry].values[0][1]

inputAge = st.selectbox("Age", sorted(age))
if inputAge:
    inputAgeMultiplier = dfAgeMultipliers[dfAgeMultipliers["Age Ranges"] == inputAge].values[0][1]

inputGender = st.radio("Gender (Unfortunately, female hourly rates are generally lower)", gender)
if inputGender:
    inputGenderMultiplier = dfGenderMultipliers[dfGenderMultipliers["Gender"] == inputGender].values[0][1]

if st.button("Show my hourly rates"):
    st.header("{} € / hour".format(round(inputAgeMultiplier*inputCategoryMultiplier*inputCountryMultiplier*inputGenderMultiplier)))
