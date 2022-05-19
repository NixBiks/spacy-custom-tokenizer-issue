from spacy.util import registry
from spacy_html_tokenizer import create_html_tokenizer

@registry.callbacks("customize_tokenizer")
def make_customize_tokenizer():
    def customize_tokenizer(nlp):
        nlp.tokenizer = create_html_tokenizer()(nlp)

    return customize_tokenizer