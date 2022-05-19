from pathlib import Path
from spacy.tokens import DocBin
from spacy.util import load_config, load_model_from_config


def apply_before_init(nlp):
    import functions
    from spacy.schemas import ConfigSchemaInit
    from spacy.util import registry

    config = nlp.config.interpolate()
    # These are the settings provided in the [initialize] block in the config
    I = registry.resolve(config["initialize"], schema=ConfigSchemaInit)
    before_init = I["before_init"]
    if before_init is not None:
        before_init(nlp)


def convert():
    nlp = load_model_from_config(load_config("config.cfg"))
    apply_before_init(nlp)
    train, dev = DocBin(), DocBin()

    doc = nlp.make_doc("<h1>Hello World</h1>")
    doc.cats = {"TEST": 1.0}
    train.add(doc)

    doc = nlp.make_doc("<h1>Hello John Doe</h1>")
    doc.cats = {"TEST": 0.0}
    dev.add(doc)

    train.to_disk(Path("train.spacy"))
    dev.to_disk(Path("dev.spacy"))
    
if __name__ == "__main__":
    convert()
