import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns

ok = False
Link ='https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href

def main():
    
    

    st.title('Analise seu _dataset_:')
    st.subheader('Analise os dados de um **_dataset_** de maneira mais rápida, ao fim da análise, faça download do arquivo modificado :sunglasses:')
    st.markdown('Opçao 1 (Arquivo .csv): **Arraste o arquivo** no formato .csv para a barra, ou clique em browse files:\n')
    st.markdown('Opção 2 (Url): **Cole o link no código fonte**, na variável Link')
    st.image('https://media.giphy.com/media/d6Qu527yhIxA2tYtZb/giphy.gif', width=200)
    entrada = st.selectbox('Selecione o tipo de entrada:',['Arquivo .csv','Link'])
    if entrada =='Arquivo .csv':
        file  = st.file_uploader('Escolha a base de dados que deseja analisar (.csv)', type = 'csv')
        if file is not None:
            df = pd.read_csv(file)
            ok = True
        else:
           st.markdown('None')
    if entrada == 'Link':
        if Link != '':
            df = pd.read_csv(Link)
            ok = True
        else:
            st.markdown('Atribua um link válido no código fonte !')

    if ok :  
        st.subheader('Analisando os dados')
        
        st.markdown('**Número de linhas:**')
        st.markdown(df.shape[0])
        st.markdown('**Número de colunas:**')
        st.markdown(df.shape[1])
        st.markdown('**Visualizando o dataframe**')
        number = st.slider('Escolha o numero de linhas que deseja ver', min_value=1, max_value=200, value = 10, step = 1)
        st.dataframe(df.head(number))
        st.markdown('**Nome das colunas:**')
        st.markdown(list(df.columns))   
        exploracao = pd.DataFrame({'nomes' : df.columns, 'tipos' : df.dtypes, 'NA #': df.isna().sum(), 'NA %' : (df.isna().sum() / df.shape[0]) * 100})
        st.markdown('**Contagem dos tipos de dados:**')
        st.write(exploracao.tipos.value_counts())
        st.markdown('**Nomes das colunas do tipo int64:**')
        st.markdown(list(exploracao[exploracao['tipos'] == 'int64']['nomes']))
        st.markdown('**Nomes das colunas do tipo float64:**')
        st.markdown(list(exploracao[exploracao['tipos'] == 'float64']['nomes']))
        st.markdown('**Nomes das colunas do tipo object:**')
        st.markdown(list(exploracao[exploracao['tipos'] == 'object']['nomes']))
        st.markdown('**Categorias da coluna escolhida:**')
        option = st.selectbox( 'Selecione uma das colunas categóricas',list(exploracao[exploracao['tipos'] == 'object']['nomes']))
        st.write(df[option].unique())
        st.markdown('**Tabela com coluna e percentual de dados faltantes :**')
        st.table(exploracao[exploracao['NA #'] != 0][['tipos', 'NA %']])
        st.markdown('**Matriz de correlação do _target_ com as demais variáveis:**')
        agree = st.checkbox('Desejo ver:')
        if agree:
            sns.heatmap(df.corr(),annot = False,)
            st.pyplot()
        st.subheader('Inputaçao de dados númericos :')
        percentual = st.slider('Escolha o limite de percentual faltante limite para as colunas vocë deseja inputar os dados', min_value=0, max_value=100)
        lista_colunas = list(exploracao[exploracao['NA %']  < percentual]['nomes'])
        select_method = st.radio('Escolha um metodo abaixo :', ('Média', 'Mediana'))
        st.markdown('Você selecionou : ' +str(select_method))
        if select_method == 'Média':
            df_inputado = df[lista_colunas].fillna(df[lista_colunas].mean())
            exploracao_inputado = pd.DataFrame({'nomes': df_inputado.columns, 'tipos': df_inputado.dtypes, 'NA #': df_inputado.isna().sum(),
                                       'NA %': (df_inputado.isna().sum() / df_inputado.shape[0]) * 100})
            st.table(exploracao_inputado[exploracao_inputado['tipos'] != 'object']['NA %'])
            st.subheader('Dados Inputados faça download abaixo : ')
            st.markdown(get_table_download_link(df_inputado), unsafe_allow_html=True)
        if select_method == 'Mediana':
            df_inputado = df[lista_colunas].fillna(df[lista_colunas].mean())
            exploracao_inputado = pd.DataFrame({'nomes': df_inputado.columns, 'tipos': df_inputado.dtypes, 'NA #': df_inputado.isna().sum(),
                                       'NA %': (df_inputado.isna().sum() / df_inputado.shape[0]) * 100})
            st.table(exploracao_inputado[exploracao_inputado['tipos'] != 'object']['NA %'])
            st.subheader('Dados Inputados faça download abaixo : ')
            st.markdown(get_table_download_link(df_inputado), unsafe_allow_html=True)


if __name__ == '__main__':
	main()
