echo "# streamlit-to-heroku-tutorial" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/your_username/your_repo_name.git
git push -u origin master

import streamlit as st
st.write('# Sum of Two Numbers')
#get input
# input 1
num1 = st.number_input(label="Enter first number")
# input 2
num2 = st.number_input(label="Enter second number") 

ans = 0
def calculate():
    ans = num1 + num2
    st.success(f"Answer = {ans}")
if st.button("Calculate result"):
    calculate()
