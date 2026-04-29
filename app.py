import streamlit as st
import random

# ------------------------
# AVALIAÇÃO DOS TIMES
# ------------------------
teams = {
    "76ers": {"attack": 91, "defense": 88},
    "Bucks": {"attack": 88, "defense": 82},
    "Bulls": {"attack": 85, "defense": 83},
    "Cavaliers": {"attack": 93, "defense": 95},
    "Celtics": {"attack": 97, "defense": 92},
    "Clippers": {"attack": 86, "defense": 86},
    "Grizzlies": {"attack": 81, "defense": 76},
    "Hawks": {"attack": 87, "defense": 89},
    "Heat": {"attack": 83, "defense": 92},
    "Hornets": {"attack": 91, "defense": 81},
    "Grizzlies": {"attack": 81, "defense": 76},
    "Jazz": {"attack": 80, "defense": 81},
    "Kings": {"attack": 76, "defense": 73},
    "Knicks": {"attack": 94, "defense": 88},
    "Lakers": {"attack": 98, "defense": 90},
    "Magic": {"attack": 90, "defense": 97},
    "Mavericks": {"attack": 85, "defense": 79},
    "Nets": {"attack": 74, "defense": 73},
    "Nuggets": {"attack": 94, "defense": 83},
    "Pacers": {"attack": 92, "defense": 88},
    "Pelicans": {"attack": 83, "defense": 84},
    "Pistons": {"attack": 94, "defense": 94},
    "Raptors": {"attack": 87, "defense": 93},
    "Rockets": {"attack": 89, "defense": 96},
    "Spurs": {"attack": 93, "defense": 92},
    "Suns": {"attack": 88, "defense": 91},
    "Thunder": {"attack": 97, "defense": 92},
    "Timberwolves": {"attack": 94, "defense": 95},
    "Trail Blazers": {"attack": 89, "defense": 88},
    "Warriors": {"attack": 96, "defense": 87},
    "Wizards": {"attack": 81, "defense": 86},
}

# ------------------------
# SIMULAÇÃO DE UM QUARTO
# ------------------------
def simulate_quarter(team1, team2):
    score1 = 0
    score2 = 0

    for _ in range(25): # 25 seria o número médio de posses de bola que cada time tem em um quarto de jogo

        # TIME 1
        prob1 = team1["attack"] / (team1["attack"] + team2["defense"])

        if random.random() < prob1:
            play = random.choices(
                ["2PT", "3PT", "FT"],
                weights=[0.6, 0.3, 0.1]
            )[0]

            if play == "2PT":
                score1 += 2 # arremessos que valem dois pontos seriam bandejas, enterradas ou arremessos de curta/média distância
            elif play == "3PT":
                score1 += 3 # arremessos que valem três pontos seriam arremessos de longa distância
            else:
                score1 += random.choice([1, 2]) # arremessos diferentes de 3PT e 2PT são lances livres, os quais, dependendo dos acontecimentos em quadra, podem ser apenas um ou dois seguidos

        # TIME 2
        prob2 = team2["attack"] / (team2["attack"] + team1["defense"])

        if random.random() < prob2:
            play = random.choices(
                ["2PT", "3PT", "FT"],
                weights=[0.6, 0.3, 0.1]
            )[0]

            if play == "2PT":
                score2 += 2
            elif play == "3PT":
                score2 += 3
            else:
                score2 += random.choice([1, 2])

    return score1, score2

# ------------------------
# SIMULAÇÃO DO JOGO
# ------------------------
def simulate_game(team1, team2):
    quarters = []
    total1 = 0
    total2 = 0

    for _ in range(4):
        q1, q2 = simulate_quarter(team1, team2)

        quarters.append((q1, q2))
        total1 += q1
        total2 += q2

    return total1, total2, quarters

# ------------------------
# INTERFACE NO STREAMLIT
# ------------------------
st.title("SIMULADOR DE JOGOS DA NBA 2025/26")

team1_name = st.selectbox("Escolha o Time 1", list(teams.keys()))
team2_name = st.selectbox("Escolha o Time 2", list(teams.keys()))

if st.button("Simular Jogo"):
    team1 = teams[team1_name]
    team2 = teams[team2_name]

    score1, score2, quarters = simulate_game(team1, team2)

    st.subheader("Resultado Final")
    st.write(f"{team1_name} {score1} x {score2} {team2_name}")

    st.subheader("Pontuação por Quarto de Jogo")

    for i, (q1, q2) in enumerate(quarters):
        st.write(f"Q{i+1}: {team1_name} {q1} x {q2} {team2_name}")

    if score1 > score2:
        st.success(f"{team1_name} venceu!")
    elif score2 > score1:
        st.success(f" {team2_name} venceu!")
    else:
        st.warning("Empate! Esse jogo iria para a prorrogação para decidir um vencedor final.")
