import streamlit as st
import pandas as pd
import plotly.express as px
st.title("India Census Data of 2011")
df=pd.read_csv("India.csv")
st.sidebar.title("India Map")
list_of_states=df["State"].unique().tolist()
list_of_states.insert(0,"Overall India")

selected_states=st.sidebar.selectbox("Select State",list_of_states)
primary=st.sidebar.selectbox("Select Primary Parameter",sorted(df.columns[4:]))
secondary=st.sidebar.selectbox("Select Secondary Parameter",sorted(df.columns[4:]))
plot=st.sidebar.button("Plot Graph")
if plot:
    st.text("Size Represent Primary Parameter")
    st.text("Color Represent Secondary Parameter")
    if selected_states=="Overall India":
         fig=px.scatter_mapbox(df,lat="Latitude", lon="Longitude",size=primary,color=secondary,mapbox_style="carto-positron"
                        , zoom=6,size_max=35,width=1200,height=700,hover_name="District")
         st.plotly_chart(fig,use_container_width=True)

    else:
      state_df=df[df["State"]==selected_states]
      fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary,
                              mapbox_style="carto-positron"
                              , zoom=6, size_max=35, width=1200, height=700, hover_name="District")
      st.plotly_chart(fig,use_container_width=True)


