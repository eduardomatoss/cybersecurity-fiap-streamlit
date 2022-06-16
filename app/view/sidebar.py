import streamlit as st


def sidebar():

    st.markdown(
        """ <style>
                       .css-1siy2j7 {
                          background-color: #FFF;
                          background-attachment: fixed;
                          flex-shrink: 0;
                          height: calc(-2px + 100vh);
                          top: 2px;
                          overflow: auto;
                          position: relative;
                          transition: margin-left 300ms ease 0s, box-shadow 300ms ease 0s;
                          width: 21rem;
                          z-index: 1000021;
                          margin-left: 0px;
                          border-radius: 0px 15px;
                      }
                      .css-1qrvfrg {
                          display: inline-flex;
                          -moz-box-align: center;
                          align-items: center;
                          -moz-box-pack: center;
                          justify-content: center;
                          font-weight: 400;
                          padding: 0.25rem 0.75rem;
                          margin: 0px;
                          line-height: 1.6;
                          color: inherit;
                          user-select: none;
                          border: 1px solid #FFF;
                          width: 100%;
                          background-color: #FFF;
                      }
                      .css-1qrvfrg:hover {
                          border-color: #79AFFF;
                          color: #79AFFF;
                      }
                      .css-1qrvfrg:active {
                          color: #FFF;
                          border-color: #79AFFF;
                          background-color: #79AFFF;
                      }
                      .css-1qrvfrg:focus {
                          box-shadow: #79AFFF 0px 0px 0px 0.2rem;
                          outline: #79AFFF none medium;
                      }
                      .css-1qrvfrg:focus:not(:active) {
                          border-color: #79AFFF;
                          color: #79AFFF;
                      }
                    </style>
                """,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        st.button("Dashboard", key="dashboard", on_click=None)
        st.button("Solution One", key="sol_one", on_click=None)
        st.button("Solution Two", key="sol_two", on_click=None)
        st.button("Solution Tree", key="sol_tree", on_click=None)
        st.button("Track Delivery", key="Track", on_click=None)
