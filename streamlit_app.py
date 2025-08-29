import streamlit as st
import pandas as pd

# -------------------------------
# Load the allocations CSV
# -------------------------------
allocations_df = pd.read_csv("final_allocation.csv")

# Ensure UniqueID is string to avoid commas
allocations_df["UniqueID"] = allocations_df["UniqueID"].astype(str)

# -------------------------------
# Streamlit Dashboard UI
# -------------------------------
st.set_page_config(page_title="🎓 Student College Allocation Dashboard", layout="centered")

st.title("🎓 Student College Allocation System")
st.write("Enter your **UniqueID** below to check your college allocation.")

# Input box for UniqueID
unique_id = st.text_input("🔑 Enter Your UniqueID:")

if unique_id:
    result = allocations_df[allocations_df["UniqueID"] == unique_id]

    if not result.empty:
        st.success("✅ Allocation Found!")

        # Extract details
        name = result.iloc[0]["Name"]
        college_id = result.iloc[0]["CollegeID"]
        institution = result.iloc[0]["Institution"]
        caste = result.iloc[0]["Caste"]
        gender = result.iloc[0]["Gender"]
        pref = result.iloc[0]["PrefNumber"]

        # Show details neatly
        st.subheader("📋 Allocation Details")
        st.markdown(
            f"""
            - 🆔 **UniqueID**: `{unique_id}`
            - 👤 **Name**: {name}
            - 🏫 **College ID**: {college_id}
            - 🏛️ **Institution**: {institution if pd.notna(institution) else 'N/A'}
            - 🧬 **Caste**: {caste}
            - 🚻 **Gender**: {gender}
            - 🔢 **Preference Used**: {pref if pd.notna(pref) else 'N/A'}
            """
        )

        # Highlight main result
        st.info(f"🎯 You have been allocated to **{institution} (College ID: {college_id})**")

        # Optionally download allocation result
        csv = result.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="⬇️ Download Your Allocation Result",
            data=csv,
            file_name=f"allocation_{unique_id}.csv",
            mime="text/csv",
        )
    else:
        st.error("❌ No allocation found for this UniqueID. Please try again.")
else:
    st.info("ℹ️ Please enter your UniqueID above to search.")

# Footer
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit")

