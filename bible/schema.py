import graphene
from django.conf import settings
from bible.learning_models.specs import ModelSpecifications
from bible.tools import load_model, sample


class GeneratedText(graphene.ObjectType):
    model_version = graphene.String(description='Dumped generator model version.')
    about = graphene.String(description='Short descriptionabout the model version.')
    text = graphene.String(description='Generated text.')


class Query:
    version = graphene.String(description='Returns the service version.')

    def resolve_version(self, info, **kwargs):
        return settings.VERSION

    generated_text = graphene.Field(
        GeneratedText,
        model_version=ModelSpecifications(description='foo'),
        description='Generates text based on a versioned dumped model. default -> SATANIC_II'
    )

    def resolve_generated_text(self, info, **kwargs):
        model_version = kwargs.get('model_version', ModelSpecifications.SATANIC_II.value)

        with open('anton/corpora/satanic_samples.txt', 'r') as samples:
            data = samples.read()
        data = data.lower()

        chars = list(sorted(set(data)))
        chars_to_idx = {ch:i for i, ch in enumerate(chars)}
        idx_to_chars = {i:ch for ch, i in chars_to_idx.items()}

        model = load_model(model_version['fpath'])
        version = model_version['model']
        about = model_version['about']
        text = sample(model, idx_to_chars, chars_to_idx, 1000)

        return GeneratedText(model_version=version, about=about, text=text)
