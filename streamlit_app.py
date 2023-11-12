import streamlit as st
from faker import Faker
from prisma_client import Prisma

fake = Faker()

# set basic page config
st.set_page_config(page_title="Streamlit Prisma ORM",
                    page_icon='💎',
                    layout='centered',
                    initial_sidebar_state='expanded')

# apply custom css if needed
# with open('assets/styles/style.css') as css:
#     st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

@st.cache_resource(ttl=3600, show_spinner=False)
def get_database():
    db = Prisma()
    return db


@st.cache_data(show_spinner=False)
def build_streamlit_header():
    st.title('💎 Streamlit Prisma ORM Example 💎')
    st.markdown("""
        This app is only a simple example of how to use the Prisma Python Client with Streamlit. <br>
        It uses the Prisma ORM to connect to a SQLite database.
        """, unsafe_allow_html=True)
    st.write("---")


@st.cache_data(show_spinner=False)
def build_streamlit_post(post):
    st.write(f"## {post.title}")
    st.write(post.content)
    st.write(f"### Author: {post.author}")
    st.write(f"### ID: {post.id}")
    st.write(f"### Created at: {post.created_at}")
    st.write(f"### Updated at: {post.updated_at}")
    st.write("---")


def get_all_posts(db):
    posts = db.post.find_many()
    return posts


def get_all_posts_sorted(db):
    posts = db.post.find_many(order={"created_at": "desc"})
    return posts


def get_single_post(db, post_id):
    post = db.post.find_first(where={"id": post_id})
    return post


def generate_fake_post(db):
    db.post.create({
        "title": fake.sentence(nb_words=5),
        "content": fake.paragraph(nb_sentences=5),
        "author": fake.name()
    })


def delete_single_post(db, post_id):
    db.post.delete(where={"id": post_id})


def clear_table(db):
    db.post.delete_many()


if __name__ == "__main__":
    db = get_database()
    if not db.is_connected():
        db.connect()
    build_streamlit_header()
    st.write(get_all_posts(db))
    if db.is_connected():
        db.disconnect()
    st.balloons()
