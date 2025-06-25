from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import plotly.express as px
import os
from openai import OpenAI

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# --- Sidebar ---
st.sidebar.title('💸 BudgetBuddy')
st.sidebar.markdown('**AI-Powered Spending Insights**')
st.sidebar.info('Upload your expense CSV to get started.\n\nAsk questions about your spending and get smart insights!')
st.sidebar.markdown('---')
st.sidebar.markdown('Made with ❤️ by Swetha')

st.title('💸 BudgetBuddy – AI-Powered Spending Insights')
st.markdown('---')

uploaded_file = st.file_uploader('**Upload your expense CSV**', type='csv', help='CSV should have columns: Date, Category, Amount')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('Preview of Uploaded Data')
    st.dataframe(df.head(), use_container_width=True)
    st.markdown('---')

    # --- KPIs ---
    st.subheader('📊 Key Metrics')
    total_spent = df['Amount'].sum()
    most_freq_category = df['Category'].mode()[0]
    day_highest_spend = df.groupby('Date')['Amount'].sum().idxmax()
    avg_spend_per_day = df.groupby('Date')['Amount'].sum().mean()

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric('Total Spent', f"${total_spent:,.2f}")
    kpi2.metric('Most Frequent Category', most_freq_category)
    kpi3.metric('Day with Highest Spend', day_highest_spend)
    kpi4.metric('Avg Spend/Day', f"${avg_spend_per_day:,.2f}")
    st.markdown('---')

    # --- Visuals ---
    st.subheader('📈 Visualizations')
    pie = px.pie(df, names='Category', values='Amount', title='Spending Breakdown')
    st.plotly_chart(pie, use_container_width=True)

    df_by_date = df.groupby('Date', as_index=False)['Amount'].sum()
    line = px.line(df_by_date, x='Date', y='Amount', title='Spending Over Time')
    st.plotly_chart(line, use_container_width=True)

    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    df_by_month = df.groupby('Month', as_index=False)['Amount'].sum()
    bar = px.bar(df_by_month, x='Month', y='Amount', title='Monthly Spending Comparison')
    st.plotly_chart(bar, use_container_width=True)
    st.markdown('---')

    # --- Insights ---
    def generate_insights(df):
        insights = []
        food_total = df[df['Category'] == 'Food']['Amount'].sum()
        if food_total > 200:
            insights.append(f"🍔 You spent ${food_total:.2f} on Food. Consider cooking more often!")
        if df['Amount'].max() > 100:
            insights.append('💸 Big spender alert! You had a high single transaction.')
        if len(df['Category'].unique()) < 3:
            insights.append('🧐 Most of your spending is concentrated in a few categories.')
        if df['Amount'].mean() < 20:
            insights.append('👏 Great job keeping your average transaction low!')
        return insights

    with st.expander('🔎 Insights', expanded=True):
        for insight in generate_insights(df):
            st.write(insight)

    # --- AI Q&A ---
    with st.expander('🤖 Ask BudgetBuddy (AI Q&A)', expanded=False):
        st.info('Set your OpenAI API key in a .env file. Your key is not stored in the app.')
        user_question = st.text_input('Ask BudgetBuddy a question about your spending:')
        if user_question:
            if not openai_api_key:
                st.warning('Please set your OpenAI API key in a .env file and restart the app.')
            else:
                client = OpenAI(api_key=openai_api_key)
                # More context for the AI
                category_totals = df.groupby('Category')['Amount'].sum().to_dict()
                monthly_totals = df.groupby('Month')['Amount'].sum().to_dict()
                prompt = (
                    "This is the user's expense summary by category: "
                    f"{category_totals}\n"
                    "And by month: "
                    f"{monthly_totals}\n"
                    "Please answer the user's question in a friendly, concise, and actionable way.\n"
                    f"Question: {user_question}"
                )
                try:
                    response = client.chat.completions.create(
                        model='gpt-3.5-turbo',
                        messages=[
                            {"role": "system", "content": "You're a financial advisor analyzing personal expense data. Be friendly and actionable."},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    st.success(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {e}")

    st.markdown('---')
    st.caption('💡 Tip: Use the sidebar for instructions and credits.')
    st.caption('Made with Streamlit • 2024')
else:
    st.info('👆 Upload a CSV file to get started!') 