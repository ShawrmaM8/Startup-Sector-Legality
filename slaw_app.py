import streamlit as st
from slaw_nlp_processing import process_idea
from slaw_classifier import predict_sector, train_classifier
from slaw_compliance_checker import check_compliance
from slaw_config import SECTORS, DATA_PATH, MODEL_PATH
import os

def main():
    st.title("Qatar Business Idea Legality Checker")
    st.title("مدقق شرعية أفكار الأعمال في قطر")
    
    st.write("Enter a business idea to predict its sector and check compliance with Qatari laws.")
    st.write("أدخل فكرة عمل للتنبؤ بقطاعها والتحقق من توافقها مع القوانين القطرية")
    
    # Input form
    idea_text = st.text_area("Business Idea فكرة عمل ", placeholder="e.g., Blockchain-based micro-investment app")
    sector = st.selectbox("Or Select Sector (optional) او اختر القطاع ", [""] + SECTORS)
    
    if st.button("Check Legality تحقق من الشرعية "):
        if idea_text or sector:
            # Use selected sector or predict from idea
            if sector:
                selected_sector = sector
            else:
                keywords = process_idea(idea_text)
                selected_sector = predict_sector(keywords)
                st.write(f"Predicted Sector: **{selected_sector}**")
                st.write(f"Keywords: {keywords}")
            
            # Check compliance
            result = check_compliance(selected_sector)
            st.success(f"Legal Viability Score: **{result['score']}/100**")
            st.subheader(f"Notes: \n {result['notes']}")
        else:
            st.error("Please enter a business idea or select a sector.")
    
    # Train classifier if not exists
    if not os.path.exists(MODEL_PATH):
        st.info("Training classifier...")
        train_classifier()
        st.success("Classifier trained!")

if __name__ == "__main__":

    main()
