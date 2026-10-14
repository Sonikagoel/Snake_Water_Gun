import random
import streamlit as st

st.title("🐍 Snake, Water, Gun")
st.write("Play against the computer!")

choices = {
    "Snake 🐍": "s",
    "Water 💧": "w",
    "Gun 🔫": "g"
}

you = st.selectbox("Choose your move:", list(choices.keys()))

if st.button("Play"):
    comp = random.choice(["s", "w", "g"])
    player = choices[you]

    names = {
        "s": "Snake 🐍",
        "w": "Water 💧",
        "g": "Gun 🔫"
    }

    st.write("You chose:", names[player])
    st.write("Computer chose:", names[comp])

    if player == comp:
        st.info("It's a tie!")
    elif (
        (player == "s" and comp == "w")
        or (player == "w" and comp == "g")
        or (player == "g" and comp == "s")
    ):
        st.success("You win! 🎉")
    else:
        st.error("You lose! Try again.")
