import streamlit as st
import plotly.express as px
from pyXSteam.XSteam import XSteam
import pandas as pd

def calculate_turbine_performance(p1, p2, cycle_type):
    steam = XSteam(XSteam.UNIT_SYSTEM_MKS)  
    
    if cycle_type == "Rankine":
        T1 = steam.tsat_p(p1)  
        s1 = steam.sL_p(p1)  
        h1 = steam.hL_p(p1)  
        
        T2 = steam.tsat_p(p2)  
        s2 = steam.sL_p(p2)  
        h2 = steam.hL_p(p2)  
        
        rendement = (h1 - h2) / h1 * 100  
        travail_turbine = h1 - h2  
        travail_pompe = (h2 - h1) * 0.05  
    
    elif cycle_type == "Carnot":
        T1 = steam.tsat_p(p1)  
        T2 = steam.tsat_p(p2)  
        rendement = (1 - (T2 / T1)) * 100 
        travail_turbine = (T1 - T2) * 10  
        travail_pompe = (T2 - T1) * 0.05  
        s1, s2, h1, h2 = None, None, None, None  
    
    return {
        "Température initiale (°C)": T1,
        "Température finale (°C)": T2,
        "Entropie initiale (kJ/kg.K)": s1,
        "Entropie finale (kJ/kg.K)": s2,
        "Enthalpie initiale (kJ/kg)": h1,
        "Enthalpie finale (kJ/kg)": h2,
        "Rendement thermique (%)": rendement,
        "Travail de la turbine (kJ/kg)": travail_turbine,
        "Travail de la pompe (kJ/kg)": travail_pompe,
    }

def plot_ts_diagram(p1, p2, cycle_type):
    steam = XSteam(XSteam.UNIT_SYSTEM_MKS)
    T = [steam.tsat_p(p) for p in [p1, p2]]
    S = [steam.sL_p(p) for p in [p1, p2]]
    
    fig = px.line(x=S, y=T, markers=True, labels={'x': "Entropie (kJ/kg.K)", 'y': "Température (°C)"}, title=f"Diagramme T-s ({cycle_type})")
    fig.update_traces(mode='markers+lines')
    st.plotly_chart(fig)

st.title("Calculateur de Turbine à Vapeur")

cycle_type = st.selectbox("Type de cycle", ["Carnot", "Rankine"], index=1)

if cycle_type == "Rankine":
    p2 = st.number_input("Pression Basse (bar)", min_value=0.03, max_value=0.5, value=0.1)
    p1 = st.number_input("Pression Haute (bar)", min_value=10.0, max_value=300.0, value=10.0)
else:
    p2 = st.number_input("Pression Basse (bar)", min_value=0.06, max_value=0.5, value=0.1)
    p1 = st.number_input("Pression Haute (bar)", min_value=10.0, max_value=300.0, value=10.0)

if st.button("Calculer"):
    results = calculate_turbine_performance(p1, p2, cycle_type)
    df_results = pd.DataFrame(results.items(), columns=["Paramètre", "Valeur"])
    st.table(df_results)
    plot_ts_diagram(p1, p2, cycle_type)
    
    csv = df_results.to_csv(index=False).encode('utf-8')
    st.download_button("Télécharger les résultats en CSV", data=csv, file_name="resultats_turbine.csv", mime='text/csv')
