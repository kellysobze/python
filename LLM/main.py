from LLM.gptmdodel import Gptmdodel
from LLM.openAI import OpenAIEmbeddingModel
from LLM.pipelineAI import PipelineAI

pipeline1=PipelineAI(Gptmdodel(),OpenAIEmbeddingModel())
pipeline2=PipelineAI(Gptmdodel(),LocalEmbedding(()))

result_1=pipeline1.esegui("Cos'è il ML?")
result_2=pipeline2.esegui("Cos'è il ML?")
