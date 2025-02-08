import streamlit as st

# スコア計算関数
def calculate_result(answers, label1, label2):
    score1 = sum(1 for ans in answers if ans == '〇')
    score2 = sum(1 for ans in answers if ans == '×')

    if score1 > score2:
        return label1
    elif score2 > score1:
        return label2
    else:
        return f"{label1}, {label2}"

# Streamlit UI
st.title("性格診断アプリ")

st.write("各質問に対して「〇」または「×」を選んでください。")

# ユーザーの回答を取得
questions = [
    ("質問 1", "質問 2", "質問 3"),
    ("質問 4", "質問 5", "質問 6"),
    ("質問 7", "質問 8", "質問 9"),
    ("質問 10", "質問 11", "質問 12"),
]

responses = []
for i, group in enumerate(questions):
    st.subheader(f"カテゴリー {i+1}")
    group_responses = [st.radio(q, ["〇", "×"], key=f"q{i}{j}") for j, q in enumerate(group)]
    responses.append(group_responses)

if st.button("診断を実行"):
    result_I_E = calculate_result(responses[0], "I", "E")
    result_S_N = calculate_result(responses[1], "S", "N")
    result_T_F = calculate_result(responses[2], "T", "F")
    result_J_P = calculate_result(responses[3], "J", "P")

    final_result = f"あなたの診断結果は: {result_I_E}{result_S_N}{result_T_F}{result_J_P} です！"
    
    st.success(final_result)
