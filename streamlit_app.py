import streamlit as st

from utils import database

# set basic page config
st.set_page_config(page_title="Streamlit Prisma",
                    page_icon=':dvd:',
                    layout='wide',
                    initial_sidebar_state='expanded')

# apply custom css styles
with open('assets/styles/style.css') as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)


@st.cache_resource(ttl=3600, show_spinner=False)
def get_database_session():
    return database.init_connection()


@st.cache_resource(show_spinner=False, experimental_allow_widgets=True)
def build_streamlit_header() -> None:
    st.title(body='Streamlit Prisma Database ORM Example :dvd:')
    st.markdown("""
        This Streamlit app is only a simple example of how to use Prisma Database ORM with Streamlit.
        It uses a local SQLite database to store the data. <br>
        This app is a simple post generator with fake data.
        Random posts are generated with the `Faker` library and the `py-avataaars` library is used to generate avatars.
        You can add random posts, delete posts and delete all posts.
        """, unsafe_allow_html=True)


@st.cache_resource(show_spinner=False, experimental_allow_widgets=True)
def build_sidebar() -> None:
    st.sidebar.header(body='About :eyeglasses:', divider='blue')
    st.sidebar.markdown("""
                        Streamlit example app with Prisma Database ORM.
                        """)
    st.sidebar.header(body='GitHub :cd:', divider='blue')
    st.sidebar.markdown("""- [Streamlit-SQLAlchemy](https://github.com/Franky1/Streamlit-SQLAlchemy)""")
    st.sidebar.header(body='Libraries :books:', divider='blue')
    st.sidebar.markdown("""
                        Used Python Libraries in this app:
                        - [Streamlit](https://docs.streamlit.io/)
                        - [Faker](https://faker.readthedocs.io/en/master/)
                        - [Pillow](https://pillow.readthedocs.io/en/stable/)
                        - [py-avataaars](https://github.com/kebu/py-avataaars)
                        """)
    st.sidebar.header(body='Resources :link:', divider='blue')
    st.sidebar.markdown("""
                        - Prisma
                            - <https://www.prisma.io/>
                            - <https://www.prisma.io/ecosystem>
                            - <https://github.com/prisma/prisma>
                        - Prisma Client Python
                            - <https://prisma-client-py.readthedocs.io/en/stable/>
                            - <https://github.com/RobertCraigie/prisma-client-py>
                        """)
    st.sidebar.write("<br><br>", unsafe_allow_html=True)
    st.sidebar.image(image='assets/images/database3.png', output_format='PNG')


@st.cache_data(show_spinner=False, hash_funcs={database.Post: lambda post: post.uuid})
def get_avatar_from_post(post: database.Post) -> bytes:
    return post.avatar.decode()


@st.cache_data(show_spinner=False, hash_funcs={database.Post: lambda post: post.uuid})
def get_content_from_post(post: database.Post) -> str:
    return post.content


# FIXME: cache doesn't work with this function, image is not shown
# @st.cache_data(show_spinner=False, experimental_allow_widgets=True, hash_funcs={database.Post: lambda post: post.uuid})
def build_streamlit_post(post: database.Post) -> None:
    posts_container = st.container()
    posts_columns = posts_container.columns(spec=[1, 11], gap="large")
    posts_columns[0].image(image=get_avatar_from_post(post), caption=post.author, output_format='PNG')
    posts_columns[1].subheader(body=post.title, divider=True)
    posts_columns[1].markdown(body=get_content_from_post(post))
    posts_columns[1].text(body=f"Created: {post.created}  |  ID: {post.id}  |  UUID: {post.uuid}")
    posts_container.markdown(body="---")


if __name__ == "__main__":
    if 'dbsession' not in st.session_state:
        st.session_state.dbsession = database.get_database_session()

    build_streamlit_header()
    build_sidebar()

    st.header(body="Actions :arrow_forward:", divider='blue')
    st.write("<br>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5, gap="large")
    with col1:
        button1 = st.button(label='Generate new post', use_container_width=True)
    with col2:
        button2 = st.button(label='Delete latest post', use_container_width=True )
    with col3:
        button3 = st.button(label='Delete oldest post', use_container_width=True)
    with col4:
        button4 = st.button(label='Delete random post', use_container_width=True)
    with col5:
        button5 = st.button(label='Delete all posts', use_container_width=True)
    placeholder_success = st.container()
    st.write("<br>", unsafe_allow_html=True)

    st.subheader(body="SQLite Database Stats :bar_chart:", divider='orange')
    placeholder_stats = st.container()

    st.header(body="Posts :pencil2:", divider='green')
    st.write("<br>", unsafe_allow_html=True)

    success = False
    if button1:
        success = database.generate_fake_post(st.session_state.dbsession)
    if button2:
        npost = database.get_newest_post(st.session_state.dbsession)
        if npost:
            success = database.delete_post(st.session_state.dbsession, npost.id)
    if button3:
        opost = database.get_oldest_post(st.session_state.dbsession)
        if opost:
            success = database.delete_post(st.session_state.dbsession, opost.id)
    if button4:
        rpost = database.get_random_post(st.session_state.dbsession)
        if rpost:
            success = database.delete_post(st.session_state.dbsession, rpost.id)
    if button5:
        success = database.clear_table(st.session_state.dbsession)
        get_avatar_from_post.clear()  # clear streamlit cache for this function
        get_content_from_post.clear()  # clear streamlit cache for this function

    if success:
        placeholder_success.success(body="Database action was successful!")
    else:
        placeholder_success.error(body="Database action was NOT successful! Rollback was performed!")

    posts = database.get_all_posts_sorted_desc(st.session_state.dbsession)
    count = database.get_post_count(st.session_state.dbsession)
    placeholder_stats.markdown(body=f":orange[Total Posts: {count}]")

    with st.container():
        for po in posts:
            build_streamlit_post(po)
