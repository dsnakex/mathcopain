import streamlit as st
import random

# ============================================
# 🎓 MATHCOPAIN - Application Streamlit
# ============================================
st.set_page_config(
    page_title="MathCopain 🎓",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

def generer_addition(niveau):
    """Génère un exercice d'addition selon le niveau"""
    if niveau == "CE1":
        a = random.randint(10, 50)
        b = random.randint(10, 50)
    else:
        a = random.randint(50, 500)
        b = random.randint(50, 500)
    return {
        'type': 'addition',
        'question': f"{a} + {b} = ?",
        'reponse': a + b,
        'operande1': a,
        'operande2': b
    }

def generer_soustraction(niveau):
    """Génère un exercice de soustraction selon le niveau"""
    if niveau == "CE1":
        b = random.randint(10, 40)
        a = random.randint(b + 10, 80)
    else:
        b = random.randint(50, 400)
        a = random.randint(b + 50, 800)
    return {
        'type': 'soustraction',
        'question': f"{a} - {b} = ?",
        'reponse': a - b,
        'operande1': a,
        'operande2': b
    }

def generer_multiplication(niveau):
    """Génère un exercice de multiplication"""
    tables = [2, 3, 4, 5] if niveau == "CE1" else [2, 3, 4, 5, 6, 7, 8, 9]
    table = random.choice(tables)
    multiplicateur = random.randint(1, 10)
    return {
        'type': 'multiplication',
        'question': f"{table} × {multiplicateur} = ?",
        'reponse': table * multiplicateur,
        'operande1': table,
        'operande2': multiplicateur
    }

def generer_probleme(niveau):
    """Génère un problème mathématique contextualisé"""
    situations = [
        {
            'contexte': "Marie a {a} billes. Son ami lui en donne {b}.",
            'question': "Combien de billes a-t-elle maintenant ?",
            'operation': 'addition'
        },
        {
            'contexte': "Théo a {a} euros. Il achète un jeu qui coûte {b} euros.",
            'question': "Combien d'argent lui reste-t-il ?",
            'operation': 'soustraction'
        },
        {
            'contexte': "Dans la classe, il y a {a} rangées de {b} élèves.",
            'question': "Combien y a-t-il d'élèves en tout ?",
            'operation': 'multiplication'
        }
    ]
    situation = random.choice(situations)
    if niveau == "CE1":
        a = random.randint(10, 30)
        b = random.randint(5, 20)
    else:
        a = random.randint(20, 50)
        b = random.randint(10, 30)
    if situation['operation'] == 'addition':
        reponse = a + b
    elif situation['operation'] == 'soustraction':
        a = a + b
        reponse = a - b
    else:
        reponse = a * b
    contexte = situation['contexte'].format(a=a, b=b)
    question = situation['question']
    return {
        'type': 'probleme',
        'question': f"{contexte} {question}",
        'reponse': reponse,
        'operation': situation['operation']
    }

def generer_exercice(niveau, type_exercice=None):
    """Génère un exercice selon le type demandé ou aléatoire"""
    types = ['addition', 'soustraction', 'multiplication', 'probleme']
    if type_exercice is None:
        type_exercice = random.choice(types)
    if type_exercice == 'addition':
        return generer_addition(niveau)
    elif type_exercice == 'soustraction':
        return generer_soustraction(niveau)
    elif type_exercice == 'multiplication':
        return generer_multiplication(niveau)
    else:
        return generer_probleme(niveau)

def verifier_reponse(exercice, reponse_utilisateur):
    """Vérifie si la réponse est correcte"""
    try:
        reponse_int = int(reponse_utilisateur)
        return reponse_int == exercice['reponse']
    except ValueError:
        return False

def attribuer_points(correct, type_exercice):
    """Attribue des points selon le type d'exercice"""
    points = {
        'addition': 10,
        'soustraction': 15,
        'multiplication': 20,
        'probleme': 30
    }
    return points.get(type_exercice, 10) if correct else 0

def verifier_badges(points_total, exercices_reussis, badges_actuels):
    """Vérifie quels nouveaux badges ont été débloqués"""
    badges_disponibles = {
        'premier_pas': {'seuil': 1, 'nom': '🌟 Premier Pas'},
        'persistant': {'seuil': 5, 'nom': '💪 Persévérant'},
        'champion': {'seuil': 10, 'nom': '🏆 Champion'},
        'expert': {'seuil': 20, 'nom': '👑 Expert'},
        'centenaire': {'seuil': 100, 'nom': '💯 Centenaire'},
        'super_star': {'seuil': 500, 'nom': '⭐ Super Star'}
    }
    nouveaux_badges = []
    for key, badge in badges_disponibles.items():
        if key in ['premier_pas', 'persistant', 'champion', 'expert']:
            if exercices_reussis >= badge['seuil'] and badge['nom'] not in badges_actuels:
                nouveaux_badges.append(badge['nom'])
        else:
            if points_total >= badge['seuil'] and badge['nom'] not in badges_actuels:
                nouveaux_badges.append(badge['nom'])
    return nouveaux_badges

def init_session_state():
    """Initialise toutes les variables de session"""
    defaults = {
        'points': 0,
        'exercices_reussis': 0,
        'exercices_totaux': 0,
        'badges': [],
        'niveau': "CE1",
        'current_exercise': None,
        'show_feedback': False,
        'feedback_correct': False,
        'nom_eleve': ""
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def local_css():
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #FF6B6B;
    }
    .success-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #D4EDDA;
        border: 2px solid #28A745;
        margin: 10px 0;
    }
    .error-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #F8D7DA;
        border: 2px solid #DC3545;
        margin: 10px 0;
    }
    .info-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #D1ECF1;
        border: 2px solid #17A2B8;
        margin: 10px 0;
    }
    .badge {
        display: inline-block;
        padding: 5px 10px;
        margin: 5px;
        border-radius: 15px;
        background-color: #FFD700;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    init_session_state()
    local_css()
    with st.sidebar:
        st.title("🎓 Mon Espace")
        nom = st.text_input("Ton prénom :", value=st.session_state.nom_eleve)
        if nom:
            st.session_state.nom_eleve = nom
        st.markdown("---")
        st.session_state.niveau = st.selectbox(
            "Niveau :",
            ["CE1", "CE2"]
        )
        st.markdown("---")
        st.subheader("📊 Mes Progrès")
        st.metric("Points totaux", st.session_state.points)
        st.metric("Exercices réussis", st.session_state.exercices_reussis)
        if st.session_state.exercices_totaux > 0:
            taux = (st.session_state.exercices_reussis / st.session_state.exercices_totaux) * 100
            st.metric("Taux de réussite", f"{taux:.0f}%")
        st.markdown("---")
        st.subheader("🏅 Mes Badges")
        if st.session_state.badges:
            for badge in st.session_state.badges:
                st.markdown(f'<div class="badge">{badge}</div>', unsafe_allow_html=True)
    st.title("🎓 MathCopain - Aide aux Devoirs")
    if st.session_state.nom_eleve:
        st.markdown(f"### Bonjour {st.session_state.nom_eleve} ! 👋")
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("➕ Addition", use_container_width=True):
            st.session_state.current_exercise = generer_exercice(st.session_state.niveau, 'addition')
            st.session_state.show_feedback = False
    with col2:
        if st.button("➖ Soustraction", use_container_width=True):
            st.session_state.current_exercise = generer_exercice(st.session_state.niveau, 'soustraction')
            st.session_state.show_feedback = False
    with col3:
        if st.button("✖️ Multiplication", use_container_width=True):
            st.session_state.current_exercise = generer_exercice(st.session_state.niveau, 'multiplication')
            st.session_state.show_feedback = False
    with col4:
        if st.button("📝 Problème", use_container_width=True):
            st.session_state.current_exercise = generer_exercice(st.session_state.niveau, 'probleme')
            st.session_state.show_feedback = False

    st.markdown("---")
    if st.session_state.current_exercise:
        ex = st.session_state.current_exercise
        st.markdown(f'<p class="big-font">{ex["question"]}</p>', unsafe_allow_html=True)
        col_ans, col_btn = st.columns([3, 1])
        with col_ans:
            user_answer = st.number_input(
                "Ta réponse :",
                min_value=0,
                max_value=10000,
                value=0,
                disabled=st.session_state.show_feedback
            )
        with col_btn:
            st.write("")
            st.write("")
            if st.button("✅ Valider", disabled=st.session_state.show_feedback):
                st.session_state.exercices_totaux += 1
                correct = verifier_reponse(ex, user_answer)
                if correct:
                    st.session_state.exercices_reussis += 1
                    pts = attribuer_points(True, ex['type'])
                    st.session_state.points += pts
                    st.session_state.feedback_correct = True
                    nouveaux = verifier_badges(st.session_state.points,
                                              st.session_state.exercices_reussis,
                                              st.session_state.badges)
                    st.session_state.badges.extend(nouveaux)
                else:
                    st.session_state.feedback_correct = False
                st.session_state.show_feedback = True
                st.rerun()
        if st.session_state.show_feedback:
            if st.session_state.feedback_correct:
                pts = attribuer_points(True, ex['type'])
                st.markdown(
                    f"<div class=\"success-box\">🎉 Bravo ! C'est parfait !<br>+ {pts} points !</div>",
                    unsafe_allow_html=True
                )
                st.balloons()
            else:
                st.markdown(
                    f'<div class="error-box">😊 Pas tout à fait ! La bonne réponse est {ex["reponse"]}.<br>'
                    f'Ne t\'inquiète pas, tu vas y arriver !</div>',
                    unsafe_allow_html=True
)
            if st.button("➡️ Exercice suivant", type="primary"):
                st.session_state.current_exercise = generer_exercice(st.session_state.niveau)
                st.session_state.show_feedback = False
                st.rerun()

if __name__ == "__main__":
    main()
