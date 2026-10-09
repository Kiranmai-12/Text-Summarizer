import streamlit as st, re
from collections import Counter
st.title("Extractive Text Summarizer")
text=st.text_area("Paste an article",height=220); n=st.slider("Summary sentence count",1,8,3)
if st.button("Summarize"):
 sentences=[s.strip() for s in re.split(r'(?<=[.!?])\s+',text) if s.strip()]
 words=re.findall(r"\b[a-zA-Z]{3,}\b",text.lower()); freq=Counter(words)
 if not sentences: st.warning("Enter some text.")
 else:
  ranked=sorted([(sum(freq[w] for w in re.findall(r"\b[a-zA-Z]{3,}\b",s.lower()))/max(len(s.split()),1),i,s) for i,s in enumerate(sentences)],reverse=True)[:n]
  st.write(" ".join(x[2] for x in sorted(ranked,key=lambda x:x[1])))
st.caption("Selects sentences from the original text; it does not write new text.")
