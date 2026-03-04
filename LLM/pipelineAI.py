class PipelineAI:
    def __init__(self,llm_model,embedding_model):
        self._ll_mdodel=llm_model
        self._embedding_model=embedding_model
    def esegui(self,testo):
        embedding=self._embedding_model.genera_embedding(testo)
        risposta=self._ll_mdodel.risposta(embedding)
        return {
            'embedding':embedding,
            'risposta':risposta
        }