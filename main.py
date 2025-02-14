from core.config import settings
import os
import vertexai
from IPython.display import Markdown
from vertexai.preview import rag
from vertexai.preview.generative_models import GenerativeModel, Tool

'''Initialize the Vertex AI client'''
vertexai.init(project=settings.GOOGLE_CLOUD_PROJECT, location=settings.GOOGLE_CLOUD_REGION)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = settings.GOOGLE_APPLICATION_CREDENTIALS

# '''Create RAG Corpus'''
# # Currently supports Google first-party embedding models
# EMBEDDING_MODEL = "publishers/google/models/text-embedding-004"  # @param {type:"string", isTemplate: true}
# embedding_model_config = rag.EmbeddingModelConfig(publisher_model=EMBEDDING_MODEL)

# rag_corpus = rag.create_corpus(
#     display_name="my-rag-corpus3", embedding_model_config=embedding_model_config
# )

# '''Check if corpus is created'''
# print(rag.list_corpora())

# print(rag_corpus.name)
# print(type(rag_corpus))
# print(type(rag_corpus.name))


'''Upload a local file to the corpus'''
rag_file = rag.upload_file(
    corpus_name="projects/kundan-nanubala/locations/us-central1/ragCorpora/4611686018427387904",
    path="D:/W3SaaS/vertexRagEngine/test.txt",
    display_name="test.txt",
    description="my test file",
)