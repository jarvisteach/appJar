import sys
sys.path.append("../../")

corpora = ['a', 'b', 'c', 'd', 'e']

from appJar import gui


def update_corpora(value):
    if value is "add_corpus":
        name = app.entry("corpus_name")
        corpora.append(app.entry("corpus_name"))
        app.option("corpora", value=corpora, mode='replace') #Here, I'd like to update the values
        app.option("corpora", selected=name) #Here, I'd like to select the new entry
    elif value is "remove_corpus":
        corpora.remove(app.option("corpora"))
        app.option("corpora", value=corpora, mode='replace', selected=0) #Here, I'd like to update the values

with gui("MyGUI", bg="lightblue") as app:
    app.option("corpora", value=corpora, label="Corpora", change=update_corpora, colspan=2)
    app.entry("corpus_name", label="Corpus Name:", colspan=2)
    app.button("add_corpus", update_corpora, label="Add Corpus")
    app.button("remove_corpus", update_corpora, label="Remove Corpus", row=2, column=1)
