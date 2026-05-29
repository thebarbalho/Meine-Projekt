import streamlit as st
import random
import pandas as pd

df = pd.read_csv("nba_teams_full.csv")

teams = {}

for _, row in df.iterrows():
    team_name = row["team"]
    if team_name not in teams:
        teams[team_name] = {"players": [], "attack": 0, "defense": 0}

    player = {
        "name": row["name"],
        "attack": row["attack"],
        "defense": row["defense"],
        "PTS": 0, "REB": 0, "AST": 0, "STL": 0, "BLK": 0
    }
    teams[team_name]["players"].append(player)

for team_name, team_data in teams.items():
    team_data["attack"] = sum(p["attack"] for p in team_data["players"]) / len(team_data["players"])
    team_data["defense"] = sum(p["defense"] for p in team_data["players"]) / len(team_data["players"])


def reset_stats(team_data):
    for player in team_data["players"]:
        player["PTS"] = 0
        player["REB"] = 0
        player["AST"] = 0
        player["STL"] = 0
        player["BLK"] = 0


def simulate_quarter(team1_data, team2_data):
    score1 = 0
    score2 = 0

    for _ in range(25):
        shooter1 = random.choice(team1_data["players"])
        defender2 = random.choice(team2_data["players"])

        prob1 = team1_data["attack"] / (team1_data["attack"] + team2_data["defense"])

        if random.random() < prob1:
            play = random.choices(["2PT", "3PT", "FT"], weights=[0.6, 0.3, 0.1])[0]
            points = {"2PT": 2, "3PT": 3}.get(play, random.choice([1, 2]))
            score1 += points
            shooter1["PTS"] += points

            if random.random() < 0.7:
                assister = random.choice(team1_data["players"])
                if assister != shooter1:
                    assister["AST"] += 1
        else:
            rebounder = random.choice(team1_data["players"] + team2_data["players"])
            rebounder["REB"] += 1

            if random.random() < 0.2:
                defender2["STL"] += 1
            elif random.random() < 0.2:
                defender2["BLK"] += 1

        shooter2 = random.choice(team2_data["players"])
        defender1 = random.choice(team1_data["players"])

        prob2 = team2_data["attack"] / (team2_data["attack"] + team1_data["defense"])

        if random.random() < prob2:
            play = random.choices(["2PT", "3PT", "FT"], weights=[0.6, 0.3, 0.1])[0]
            points = {"2PT": 2, "3PT": 3}.get(play, random.choice([1, 2]))
            score2 += points
            shooter2["PTS"] += points

            if random.random() < 0.7:
                assister = random.choice(team2_data["players"])
                if assister != shooter2:
                    assister["AST"] += 1
        else:
            rebounder = random.choice(team1_data["players"] + team2_data["players"])
            rebounder["REB"] += 1

            if random.random() < 0.2:
                defender1["STL"] += 1
            elif random.random() < 0.2:
                defender1["BLK"] += 1

    return score1, score2


def simulate_game(team1_data, team2_data):
    quarters = []
    total1 = 0
    total2 = 0

    for _ in range(4):
        q1, q2 = simulate_quarter(team1_data, team2_data)
        quarters.append((q1, q2))
        total1 += q1
        total2 += q2

    return total1, total2, quarters


st.title("Simulador de Jogos da NBA 2025/26")

team1_name = st.selectbox("Time 1", list(teams.keys()))
team2_name = st.selectbox("Time 2", list(teams.keys()))

if st.button("Simular Jogo"):
    if team1_name == team2_name:
        st.warning("Escolha times diferentes!")
    else:
        team1_data = teams[team1_name]
        team2_data = teams[team2_name]

        reset_stats(team1_data)
        reset_stats(team2_data)

        score1, score2, quarters = simulate_game(team1_data, team2_data)

        st.subheader("Resultado Final")
        st.write(f"**{team1_name}** {score1} x {score2} **{team2_name}**")

        st.subheader("Por Quarto")
        for i, (q1, q2) in enumerate(quarters):
            st.write(f"Q{i+1}: **{team1_name}** {q1} x {q2} **{team2_name}**")

        st.subheader("Box Score")
        st.write(f"### {team1_name}")
        for p in team1_data["players"]:
            st.write(f"{p['name']} - {p['PTS']} PTS | {p['REB']} REB | {p['AST']} AST | {p['STL']} STL | {p['BLK']} BLK")

        st.write(f"### {team2_name}")
        for p in team2_data["players"]:
            st.write(f"{p['name']} - {p['PTS']} PTS | {p['REB']} REB | {p['AST']} AST | {p['STL']} STL | {p['BLK']} BLK")

        all_players = team1_data["players"] + team2_data["players"]
        mvp = max(all_players, key=lambda p: p["PTS"])

        st.subheader("MVP da Partida")
        st.success(f"{mvp['name']} com {mvp['PTS']} pontos!")
