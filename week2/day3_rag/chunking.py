from pypdf import PdfReader

reader=PdfReader("sample.pdf")

text=""

for page in reader.pages:

    text += page.extract_text()


chunk_size=100

chunks=[]

for i in range(
0,
len(text),
chunk_size
):

    chunks.append(
        text[i:i+chunk_size]
    )

for chunk in chunks:

    print("\n-----")

    print(chunk)