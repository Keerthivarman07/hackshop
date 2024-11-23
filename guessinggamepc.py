import streamlit as st
import random

st.title("Guess the Number Game")


if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)


st.write("I'm thinking of a number between 1 and 100.")
st.write("Can you guess it?")

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)


if st.button("Submit Guess"):
    if guess < st.session_state.number_to_guess:
        st.write("Too low! Try again.")
    elif guess > st.session_state.number_to_guess:
        st.write("Too high! Try again.")
    else:
        st.write("Congratulations! You guessed it!")
        st.session_state.number_to_guess = random.randint(1, 100)

if st.button("Reset Game"):
    st.session_state.number_to_guess = random.randint(1, 100)
    st.write("Game has been reset! Try guessing again.")
