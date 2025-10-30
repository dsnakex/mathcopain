import streamlit as st
import random
from datetime import datetime

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
    if niveau == "CE1":
        a = random.randint(10, 50)
        b = random.randint(10, 50)
    elif niveau == "CE2":
        a = random.randint(50, 500)
        b = random.randint(50, 500)
    elif niveau == "CM1":
        # CM1 : Additions jusqu'à 100 000
        a = random.randint(1000, 50000)
        b = random.randint(1000, 50000)
    else:  # CM2
        # CM2 : Additions avec décimaux ou très grands nombres
        a = random.randint(10000, 100000)
        b = random.randint(10000, 100000)
    return {
        'type': 'addition',
        'question': f"{a} + {b} = ?",
        'reponse': a + b,
        'operande1': a,
        'operande2': b
    }

def generer_soustraction(niveau):
    if niveau == "CE1":
        b = random.randint(10, 40)
        a = random.randint(b + 10, 80)
    elif niveau == "CE2":
        b = random.randint(50, 400)
        a = random.randint(b + 50, 800)
    elif niveau == "CM1":
        # CM1 : Soustractions jusqu'à 100 000
        b = random.randint(1000, 25000)
        a = random.randint(b + 1000, 50000)
    else:  # CM2
        # CM2 : Soustractions plus complexes
        b = random.randint(10000, 50000)
        a = random.randint(b + 10000, 100000)
    return {
        'type': 'soustraction',
        'question': f"{a} - {b} = ?",
        'reponse': a - b,
        'operande1': a,
        'operande2': b
    }

def generer_multiplication(niveau):
    if niveau == "CE1":
        tables = [2, 3, 4, 5]
        multiplicateur = random.randint(1, 10)
    elif niveau == "CE2":
        tables = [2, 3, 4, 5, 6, 7, 8, 9]
        multiplicateur = random.randint(1, 10)
    elif niveau == "CM1":
        # CM1 : Multiplications posées (2-3 chiffres × 1-2 chiffres)
        a = random.randint(10, 999)
        b = random.randint(2, 99)
        return {
            'type': 'multiplication',
            'question': f"{a} × {b} = ?",
            'reponse': a * b,
            'operande1': a,
            'operande2': b
        }
    else:  # CM2
        # CM2 : Multiplications plus grandes
        a = random.randint(100, 9999)
        b = random.randint(10, 100)
        return {
            'type': 'multiplication',
            'question': f"{a} × {b} = ?",
            'reponse': a * b,
            'operande1': a,
            'operande2': b
        }
    table = random.choice(tables)
    return {
        'type': 'multiplication',
        'question': f"{table} × {multiplicateur} = ?",
        'reponse': table * multiplicateur,
        'operande1': table,
        'operande2': multiplicateur
    }
def generer_probleme(niveau):
    # Situations pour CE1/CE2
    situations_base = [
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
            'question': "Combien y a-t-il d'élèves en total ?",
            'operation': 'multiplication'
        }
    ]

    # Situations supplémentaires pour CM1/CM2
    situations_avancees = [
        {
            'contexte': "Une boulangerie vend {a} baguettes par jour. En {b} jours, combien de baguettes vend-elle ?",
            'question': "Combien de baguettes en total ?",
            'operation': 'multiplication'
        },
        {
            'contexte': "{a} bonbons sont partagés équitablement entre {b} enfants.",
            'question': "Combien de bonbons chacun recevra-t-il ?",
            'operation': 'division'
        },
        {
            'contexte': "Un livre coûte {a} euros. Une librairie en vend {b}.",
            'question': "Combien rapporte la vente ?",
            'operation': 'multiplication'
        }
    ]
    
    # Choisir les situations selon le niveau    
    if niveau in ["CE1", "CE2"]:
        situations = situations_base
    else:  # CM1/CM2        
        situations = situations_base + situations_avancees
    situation = random.choice(situations)
    # Adapter les nombres selon le niveau    
    if niveau == "CE1":
        a = random.randint(10, 30)
        b = random.randint(5, 20)
    elif niveau == "CE2":
        a = random.randint(20, 50)
        b = random.randint(10, 30)
    elif niveau == "CM1":
        a = random.randint(50, 200)
        b = random.randint(20, 100)
    else:  # CM2
        a = random.randint(100, 500)
        b = random.randint(50, 200)
    # Calculer la réponse
    if situation['operation'] == 'addition':
        reponse = a + b
    elif situation['operation'] == 'soustraction':
        if a < b: a, b = b, a # Éviter les négatifs
        reponse = a - b
    elif situation['operation'] == 'multiplication':
        reponse = a * b
    else:  # division
        if b == 0: b = 1 # Éviter la division par zéro
    # S'assurer que la division tombe juste pour les problèmes simples
        a = b * random.randint(2, 10) # Assure une division entière
        reponse = a // b # Calcul de la réponse pour la division
    contexte = situation['contexte'].format(a=a, b=b)
    question = situation['question']
    return {
        'type': 'probleme', # Correction de l'indentation
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
    """
    Vérifie si la réponse de l'utilisateur est correcte
    
    Args:
        exercice (dict): L'exercice avec 'reponse'
        reponse_utilisateur: La réponse saisie (int ou str)
    
    Returns:
        bool: True si correcte, False sinon
    """
    try:
        # Convertir la réponse en entier
        reponse_int = int(reponse_utilisateur) # Utilisation de int() et correction du nom de variable
        # Comparer avec la bonne réponse
        return reponse_int == exercice['reponse'] # Comparaison avec la variable correcte
    except (ValueError, TypeError):
        # Si conversion impossible, réponse incorrecte
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

def verifier_badges(points_total, exercices_reussis, badges_actuels, niveau):
    """Vérifie quels nouveaux badges ont été débloqués"""
    badges_disponibles = {
        'premier_pas': {'seuil': 1, 'nom': '🌟 Premier Pas'},
        'persistant': {'seuil': 5, 'nom': '💪 Persévérant'},
        'champion': {'seuil': 10, 'nom': '🏆 Champion'},
        'expert': {'seuil': 20, 'nom': '👑 Expert'},
        'centenaire': {'seuil': 100, 'nom': '💯 Centenaire'},
        'super_star': {'seuil': 500, 'nom': '⭐ Super Star'}
    }
    # Badges bonus pour CM1/CM2
    if niveau in ["CM1", "CM2"]:
        badges_disponibles['mathematicien'] = {'seuil': 50, 'nom': '🧮 Mathématicien'}
        badges_disponibles['genie'] = {'seuil': 100, 'nom': '🔬 Génie des Maths'}
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
        color: #FF6B6B;    }    
    .success-box {        
        padding: 20px;        
        border-radius: 10px;        
        background-color: #D4EDDA;        
        border: 2px solid #28A745;        
        margin: 10px 0;    }    
    .error-box {        
        padding: 20px;        
        border-radius: 10px;        
        background-color: #F8D7DA;        
        border: 2px solid #DC3545;        
        margin: 10px 0;    }    
    .info-box {        
        padding: 15px;       
        border-radius: 10px;        
        background-color: #D1ECF1;        
        border: 2px solid #17A2B8;        
        margin: 10px 0;    }    
    .badge {        
        display: inline-block;        
        padding: 5px 10px;        
        margin: 5px;        
        border-radius: 15px;        
        background-color: #FFD700;        
        font-weight: bold;    }    
    /* Ajouter ces styles pour le crédit */    
    .footer-credit {        
        text-align: center;        
        color: #888;        
        font-size: 12px;        
        margin-top: 30px;        
        padding: 20px;        
        border-top: 1px solid #e0e0e0;    }    
    .footer-credit strong {       
        color: #333;    }    
    .footer-credit p {        
        margin: 5px 0;    }    
    </style>    """, 
    unsafe_allow_html=True)

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
            ["CE1", "CE2", "CM1", "CM2"]
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
        st.markdown("---")
        st.markdown("""
        <div style='text-align: center; color: #888; font-size: 12px; margin-top: 30px;'>
        <p>✨ <strong>MathCopain</strong></p>
        <p>Développé par <strong>Pascal Dao</strong></p>
        <p>Avec ❤️ pour l'éducation</p>
        <p style='font-size: 10px; margin-top: 10px; color: #aaa;'>v1.0.0 | Octobre 2025</p>
        </div>
        """, unsafe_allow_html=True)

    st.title("🎓 MathCopain")
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
    # Créer une clé unique basée sur l'exercice actuel
            exercise_key = f"answer_{id(st.session_state.current_exercise)}"
    
            user_answer = st.number_input(
                "Ta réponse :",
                min_value=0,
            max_value=1000000,
            value=None,  # ← Champ vide
        step=1,
        format="%d",
        key=f"input_{st.session_state.exercices_totaux}",
        disabled=st.session_state.show_feedback
    )
        with col_btn:
            st.write("")
            st.write("")
            # Désactiver le bouton si pas de réponse
            disabled_button = st.session_state.show_feedback or user_answer is None

            if st.button("✅ Valider", disabled=disabled_button):
                st.session_state.exercices_totaux += 1
                correct = verifier_reponse(ex, user_answer)
                
                if correct:
                    st.session_state.exercices_reussis += 1
                    pts = attribuer_points(True, ex['type'])
                    st.session_state.points += pts
                    st.session_state.feedback_correct = True
                    nouveaux = verifier_badges(st.session_state.points,
                                              st.session_state.exercices_reussis,
                                              st.session_state.badges,
                                              st.session_state.niveau)
                    st.session_state.badges.extend(nouveaux)
                else: # Correction de l'indentation
                    st.session_state.feedback_correct = False # Correction de l'indentation
                st.session_state.show_feedback = True # Correction de l'indentation
                st.rerun() # Correction de l'indentation
        if st.session_state.show_feedback:
            if st.session_state.feedback_correct:
                pts = attribuer_points(True, ex['type']) # Correction de l'indentation
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
                st.session_state.show_feedback = False # Correction de l'indentation
                # st.session_state.answer_input = 0 # Cette ligne est inutile et peut être supprimée
                st.session_state.feedback_correct = False # Réinitialiser le feedback
                st.rerun()

if __name__ == "__main__":
    main()
