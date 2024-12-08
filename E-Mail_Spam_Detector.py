
import streamlit as st
import pickle

model = pickle.load(open('spam.pkl','rb'))
cv = pickle.load(open('vec.pkl','rb'))

def main():
	st.title("E-Mail Spam Detector")
	#st.write("This E-Mail Spam Detector Tool has been Developed by Implementing the Natural Language Processing & Machine Learning which helps in Determining the E-Mail whether it's Spam or not.")
	#st.write("This is a Machine Learning application to classify emails as spam or ham.")
	#st.subheader("Classification")
	st.subheader("Made By :- Dinesh Kumar Sahoo")
	user_input=st.text_area("Enter an E-Mail to Check" ,height=200)
	if st.button("Check"):
		if user_input:
			data=[user_input]
			print(data)
			vec=cv.transform(data).toarray()
			result=model.predict(vec)
			if result[0]==0:
				st.success("This isn't A Spam E-Mail")
			else:
				st.error("This is A Spam E-Mail")
		else:
			st.write("Please Enter an E-Mail to Check whether it's a Spam E-Mail or Not")
main()
