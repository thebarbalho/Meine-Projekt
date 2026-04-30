import streamlit as st
import random

# ------------------------
# AVALIAÇÃO DOS TIMES
# ------------------------
teams = {
    "76ers": {
     "players": [
            {"name": "Tyrese Maxey", "attack": 94},
            {"name": "V.J. Edgecombe", "attack": 89},
            {"name": "Paul George", "attack": 91},
            {"name": "Joel Embiid", "attack": 96},
            {"name": "Andre Drummond", "attack": 86}
        ],
        "defense": 94,
    "Bucks": {
     "players": [
            {"name": "Ryan Rollins", "attack": 84},
            {"name": "Kevin Porter Jr.", "attack": 85},
            {"name": "Giannis Antetokounmpo", "attack": 98},
            {"name": "Bobby Portis Jr.", "attack": 87},
            {"name": "Myles Turner", "attack": 88}
        ],
        "defense": 91,
    "Bulls": {
     "players": [
            {"name": "Josh Giddey", "attack": 89},
            {"name": "Anfernee Simons", "attack": 88},
            {"name": "Collin Sexton", "attack": 87},
            {"name": "Matas Buzelis", "attack": 88},
            {"name": "Jalen Smith", "attack": 82}
        ],
        "defense": 88,
    "Cavaliers": {
     "players": [
            {"name": "James Harden", "attack": 94},
            {"name": "Donovan Mitchell", "attack": 96},
            {"name": "Max Strus", "attack": 87},
            {"name": "Evan Mobley", "attack": 91},
            {"name": "Jarrett Allen", "attack": 86}
        ],
        "defense": 96,
    "Celtics": {
     "players": [
            {"name": "Payton Pritchard", "attack": 89},
            {"name": "Derrick White", "attack": 91},
            {"name": "Jaylen Brown", "attack": 97},
            {"name": "Jayson Tatum", "attack": 99},
            {"name": "Nicola Vucevic", "attack": 89}
        ],
        "defense": 94,
    "Clippers": {
     "players": [
            {"name": "Darius Garland", "attack": 92},
            {"name": "Bradley Beal", "attack": 88},
            {"name": "Kawhi Leonard", "attack": 97},
            {"name": "John Collins", "attack": 87},
            {"name": "Brook Lopez", "attack": 90}
        ],
        "defense": 93,
    "Grizzlies": {
     "players": [
            {"name": "Ja Morant", "attack": 94},
            {"name": "Ty Jerome", "attack": 85},
            {"name": "G.G. Jackson", "attack": 86},
            {"name": "Santi Aldama", "attack": 83},
            {"name": "Zach Edey", "attack": 88}
        ],
        "defense": 86,
    "Hawks": {
     "players": [
            {"name": "C.J. McCollum", "attack": 92},
            {"name": "Dyson Daniels", "attack": 90},
            {"name": "Jonathan Kuminga", "attack": 88},
            {"name": "Jalen Johnson", "attack": 93},
            {"name": "Onyeka Okognwu", "attack": 86}
        ],
        "defense": 92,
    "Heat": {
     "players": [
            {"name": "Tyler Herro", "attack": 92},
            {"name": "Norman Powell", "attack": 89},
            {"name": "Jaime Jaquez Jr.", "attack": 89},
            {"name": "Andrew Wiggins", "attack": 89},
            {"name": "Bam Adebayo", "attack": 96}
        ],
        "defense": 93,
    "Hornets": {
     "players": [
            {"name": "LaMelo Ball", "attack": 96},
            {"name": "Brandon Miller", "attack": 91},
            {"name": "Kon Knueppel", "attack": 93},
            {"name": "Miles Bridges", "attack": 88},
            {"name": "Moussa Diabate", "attack": 84}
        ],
        "defense": 88,
    "Jazz": {
     "players": [
            {"name": "Keyonte George", "attack": 85},
            {"name": "Ace Bailey", "attack": 85},
            {"name": "Kevin Love", "attack": 86},
            {"name": "Jaren Jackson Jr.", "attack": 88},
            {"name": "Walker Kessler", "attack": 87}
        ],
        "defense": 90,
    "Kings": {
     "players": [
            {"name": "Russell Westbrook", "attack": 91},
            {"name": "Zach LaVine", "attack": 92},
            {"name": "DeMar DeRozan", "attack": 91},
            {"name": "Keegan Murray", "attack": 85},
            {"name": "Domantas Sabonis", "attack": 94}
        ],
        "defense": 85,
    "Knicks": {
     "players": [
            {"name": "Jalen Brunson", "attack": 98},
            {"name": "Mikal Bridges", "attack": 92},
            {"name": "O.G. Anunoby", "attack": 90},
            {"name": "Josh Hart", "attack": 89},
            {"name": "Karl-Anthony Towns", "attack": 96}
        ],
        "defense": 92,
    "Lakers": {
     "players": [
            {"name": "Luka Doncic", "attack": 99},
            {"name": "Austin Reaves", "attack": 95},
            {"name": "Marcus Smart", "attack": 88},
            {"name": "LeBron James", "attack": 99},
            {"name": "DeAndre Ayton", "attack": 90}
        ],
        "defense": 93,
    "Magic": {
     "players": [
            {"name": "Jalen Suggs", "attack": 90},
            {"name": "Desmond Bane", "attack": 92},
            {"name": "Franz Wagner", "attack": 94},
            {"name": "Paolo Banchero", "attack": 96},
            {"name": "Wendell Carter Jr.", "attack": 88}
        ],
        "defense": 95,
    "Mavericks": {
     "players": [
            {"name": "Kyrie Irving", "attack": 97},
            {"name": "Klay Thompson", "attack": 93},
            {"name": "Khris Middleton", "attack": 92},
            {"name": "Cooper Flagg", "attack": 95},
            {"name": "Daniel Gafford", "attack": 88}
        ],
        "defense": 91,
    "Nets": {
     "players": [
            {"name": "Egor Demin", "attack": 84},
            {"name": "Michael Porter Jr.", "attack": 89},
            {"name": "Danny Wolf", "attack": 86},
            {"name": "Day'Ron Sharpe", "attack": 83},
            {"name": "Nicolas Claxton", "attack": 88}
        ],
        "defense": 87,
    "Nuggets": {
     "players": [
            {"name": "Jamal Murray", "attack": 95},
            {"name": "Christian Braun", "attack": 85},
            {"name": "Cam Johnson", "attack": 88},
            {"name": "Aaron Gordon", "attack": 91},
            {"name": "Nikola Jokic", "attack": 99}
        ],
        "defense": 90,
    "Pacers": {
     "players": [
            {"name": "Tyrese Haliburton", "attack": 97},
            {"name": "Andrew Nembhard", "attack": 91},
            {"name": "Aaron Nesmith", "attack": 87},
            {"name": "Pascal Siakam", "attack": 93},
            {"name": "Ivica Zubac", "attack": 87}
        ],
        "defense": 93,
    "Pelicans": {
     "players": [
            {"name": "Dejounte Murray", "attack": 90},
            {"name": "Jordan Poole", "attack": 91},
            {"name": "Trey Murphy III", "attack": 89},
            {"name": "Saddiq Bey", "attack": 88},
            {"name": "Zion Williamson", "attack": 94}
        ],
        "defense": 92,
    "Pistons": {
     "players": [
            {"name": "Cade Cunningham", "attack": 97},
            {"name": "Duncan Robinson", "attack": 86},
            {"name": "Ausar Thompson", "attack": 92},
            {"name": "Tobias Harris", "attack": 90},
            {"name": "Jalen Duren", "attack": 92}
        ],
        "defense": 96,
    "Raptors": {
     "players": [
            {"name": "Immanuel Quickley", "attack": 90},
            {"name": "R.J. Barrett", "attack": 91},
            {"name": "Brandon Ingram", "attack": 92},
            {"name": "Scottie Barnes", "attack": 94},
            {"name": "Jakob Poeltl", "attack": 87}
        ],
        "defense": 92,
    "Rockets": {
     "players": [
            {"name": "Amen Thompson", "attack": 93},
            {"name": "Jabari Smith Jr.", "attack": 90},
            {"name": "Tari Eason", "attack": 90},
            {"name": "Kevin Durant", "attack": 98},
            {"name": "Alperen Sengun", "attack": 95}
        ],
        "defense": 94,
    "Spurs": {
     "players": [
            {"name": "De'Aaron Fox", "attack": 93},
            {"name": "Stephon Castle", "attack": 92},
            {"name": "Dylan Harper", "attack": 88},
            {"name": "Devin Vassell", "attack": 88},
            {"name": "Victor Wembanyama", "attack": 86}
        ],
        "defense": 96,
    "Suns": {
     "players": [
            {"name": "Devin Booker", "attack": 96},
            {"name": "Jalen Green", "attack": 92},
            {"name": "Dillon Brooks", "attack": 92},
            {"name": "Collin Gillespie", "attack": 87},
            {"name": "Mark Williams", "attack": 89}
        ],
        "defense": 93,
    "Thunder": {
     "players": [
            {"name": "Shai Gilgeous-Alexander", "attack": 98},
            {"name": "Lu Dort", "attack": 86},
            {"name": "Jalen Williams", "attack": 94},
            {"name": "Chet Holmgren", "attack": 94},
            {"name": "Isaiah Hartenstein", "attack": 90}
        ],
        "defense": 95,
    "Timberwolves": {
     "players": [
            {"name": "Donte DiVincenzo", "attack": 90},
            {"name": "Anthony Edwards", "attack": 98},
            {"name": "Jaden McDaniels", "attack": 91},
            {"name": "Julius Randle", "attack": 94},
            {"name": "Rudy Gobert", "attack": 90}
        ],
        "defense": 95,
    "Trail Blazers": {
     "players": [
            {"name": "Damian Lillard", "attack": 96},
            {"name": "Scoot Henderson", "attack": 91},
            {"name": "Toumani Camara", "attack": 92},
            {"name": "Deni Avdija", "attack": 95},
            {"name": "Donovan Clingan", "attack": 89}
        ],
        "defense": 92,
    "Warriors": {
     "players": [
            {"name": "Stephen Curry", "attack": 99},
            {"name": "Gui Santos", "attack": 93},
            {"name": "Jimmy Butler", "attack": 95},
            {"name": "Draymond Green", "attack": 92},
            {"name": "Kristaps Porzingis", "attack": 93}
        ],
        "defense": 94,
    "Wizards": {
     "players": [
            {"name": "Trae Young", "attack": 96},
            {"name": "Bilal Coulibaly", "attack": 89},
            {"name": "Kyshawn George", "attack": 84},
            {"name": "Alex Sarr", "attack": 93},
            {"name": "Anthony Davis", "attack": 96}
        ],
        "defense": 90
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
