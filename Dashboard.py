import pandas
import streamlit
import plotly.express

if __name__=="__main__":
    streamlit.set_page_config(layout="wide") #widens dashboard
    # test this file with "Banco Vtimas de Homicdio Consumado - Atualizado 11 - Novembro.xlsx"
    dt = pandas.read_excel("C:\\Users\\Administrator\\PycharmProjects\\Exercises\\Banco Vtimas de Homicdio Consumado - Atualizado 11 - Novembro.xlsx", decimal=",", sheet_name="População - Municipio") #replace path to xml file, if decimal is ., replace that too
    dt = dt.sort_values(by="MUNICÍPIO")
    municipio = streamlit.multiselect("MUNICÍPIO", dt["MUNICÍPIO"]) #creates select box
    filtered = dt[dt["MUNICÍPIO"].isin(municipio)] #filters selection to selected municipio
    filtered
    coluna1, coluna2 = streamlit.columns(2)
    coluna3, coluna4 = streamlit.columns(2)
    figure_1 = plotly.express.bar(filtered, x="MUNICÍPIO", y=[2009, 2010, 2011, 2012], title="MUNICÍPIOxPOPULAÇÃO - ANO", color=2009) #plots graph
    coluna1.plotly_chart(figure_1) #add figure to coluna 1
    dt #plots table
