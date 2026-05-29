import streamlit as st
import random
import pandas as pd


# AVALIAÇÃO DOS TIMES

def load_teams():
    df = pd.read_csv("nba_teams_full.csv")

# FUNÇÃO DE ATAQUE DE UM TIME

def calculate_team_attack(team):
    return sum(p["attack"] for p in team["players"]) / len(team["players"])

# FUNÇÃO PARA RESETAR ESTATÍSTICAS
def reset_stats(team):
    for player in team["players"]:
        player["PTS"] = 0
        player["REB"] = 0
        player["AST"] = 0
        player["STL"] = 0
        player["BLK"] = 0

# SIMULAÇÃO DE UM QUARTO

def simulate_quarter(team1, team2):
    score1 = 0
    score2 = 0

    attack1 = calculate_team_attack(team1)
    attack2 = calculate_team_attack(team2)

    for _ in range(25):

        #  ATAQUE DO TIME 1 
        shooter1 = random.choice(team1["players"])
        defender2 = random.choice(team2["players"])

        prob1 = attack1 / (attack1 + team2.get("defense", 90))

        if random.random() < prob1:
            play = random.choices(
                ["2PT", "3PT", "FT"],
                weights=[0.6, 0.3, 0.1]
            )[0]

            if play == "2PT":
                points = 2
            elif play == "3PT":
                points = 3
            else:
                points = random.choice([1, 2])

            score1 += points
            shooter1["PTS"] += points

            # assistência
            if random.random() < 0.7:
                assister = random.choice(team1["players"])
                if assister != shooter1:
                    assister["AST"] += 1

        else:
            # rebote
            rebounder = random.choice(team1["players"] + team2["players"])
            rebounder["REB"] += 1

            # defesa
            if random.random() < 0.2:
                defender2["STL"] += 1
            elif random.random() < 0.2:
                defender2["BLK"] += 1

        # ATAQUE DO TIME 2 
        shooter2 = random.choice(team2["players"])
        defender1 = random.choice(team1["players"])

        prob2 = attack2 / (attack2 + team1.get("defense", 90))

        if random.random() < prob2:
            play = random.choices(
                ["2PT", "3PT", "FT"],
                weights=[0.6, 0.3, 0.1]
            )[0]

            if play == "2PT":
                points = 2
            elif play == "3PT":
                points = 3
            else:
                points = random.choice([1, 2])

            score2 += points
            shooter2["PTS"] += points

            if random.random() < 0.7:
                assister = random.choice(team2["players"])
                if assister != shooter2:
                    assister["AST"] += 1

        else:
            rebounder = random.choice(team1["players"] + team2["players"])
            rebounder["REB"] += 1

            if random.random() < 0.2:
                defender1["STL"] += 1
            elif random.random() < 0.2:
                defender1["BLK"] += 1

    return score1, score2

# SIMULAÇÃO DO JOGO

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


# INTERFACE NO STREAMLIT
# ------------------------
st.title("SIMULADOR DE JOGOS DA NBA 2025/26")

team1_name = st.selectbox("Time 1", list(teams.keys()))
team2_name = st.selectbox("Time 2", list(teams.keys()))

if st.button("Simular Jogo"):    

    if team1_name == team2_name:        
        st.warning("Escolha times diferentes!")    
    else:        
        team1 = teams[team1_name]        
        team2 = teams[team2_name]       
       
# RESET DAS ESTATÍSTICAS     
reset_stats(team1)        
reset_stats(team2)        

score1, score2, quarters = simulate_game(team1, team2)       

# RESULTADO DO DUELO
st.subheader("Resultado Final")        
st.write(f"{team1_name} {score1} x {score2} {team2_name}")      

# DINÂMICA DURANTE OS QUARTOS DE JOGO        
st.subheader("Por Quarto")        
for i, (q1, q2) in enumerate(quarters):            
    st.write(f"Q{i+1}: {q1} x {q2}")        
    
# ESTATÍSTICAS INDIVIDUAIS      
st.subheader("Box Score")        

st.write(f"### {team1_name}")        
for p in team1["players"]:            
    st.write(f"{p['name']} - {p['PTS']} PTS | {p['REB']} REB | {p['AST']} AST | {p['STL']} STL | {p['BLK']} BLK")        
    
st.write(f"### {team2_name}")        
for p in team2["players"]:            
    st.write(f"{p['name']} - {p['PTS']} PTS | {p['REB']} REB | {p['AST']} AST | {p['STL']} STL | {p['BLK']} BLK")       
    
# MELHOR JOGADOR DA PARTIDA        
all_players = team1["players"] + team2["players"]        
mvp = max(all_players, key=lambda p: p["PTS"])        

st.subheader(" MVP DA PARTIDA")        
st.success(f"{mvp['name']} com {mvp['PTS']} pontos!")
