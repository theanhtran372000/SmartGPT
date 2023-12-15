import os
from loguru import logger

from loader import WebLoader
from splitter import CharacterSplitter
from store import build_faiss_store, save_faiss_store, load_faiss_store
from model import get_emb, get_llm
from chatbot import build_chain

if __name__ == '__main__':
    
    os.environ["OPENAI_API_KEY"] = open('/home/asus/work/SmartGPT/server/save/keys/openai.txt', 'r').read().strip()
    
    savepath = '/home/asus/work/SmartGPT/server/save/tmps/test_faiss'
    urls = [
        'https://vietnamnet.vn/eu-ra-quyet-dinh-lich-su-dong-y-mo-dam-phan-ket-nap-ukraine-2227186.html',
        'https://vietnamnet.vn/qua-bong-vang-viet-nam-2023-kem-vui-vi-chi-dua-song-ma-2227082.html',
        'https://vietnamnet.vn/psg-muon-chieu-mo-casemiro-mu-mung-tham-2227142.html'
    ]
    
    # Get llms and embs
    logger.info('Get ChatGPT model...')
    emb = get_emb()
    llm = get_llm('gpt-3.5-turbo', temperature=0, streaming=True)
    
    # Load web content
    if not os.path.exists(savepath):
        logger.info('Load data...')
        loader = WebLoader()
        data = loader.load_urls(urls)
        
        # Split content into docs
        logger.info('Split data...')
        splitter = CharacterSplitter()
        docs = splitter.split(data)
    
        # Build FAISS store
        logger.info('Build FAISS store...')
        store = build_faiss_store(docs, emb)
        save_faiss_store(store, savepath)
        logger.success('Save to {}!'.format(savepath))
    
    # Load store and predict
    logger.info('Load FAISS store...')
    store = load_faiss_store(savepath, emb)
    
    # Build chain
    logger.info('Build chatbot...')
    chain = build_chain(llm, store)
    
    # Try answer
    question = "Ứng cử viên nặng ký cho quả bóng vàng 2023 là ai? Trả lời bằng tiếng Việt."
    logger.info('Anwering question "{}"...'.format(question))
    output = chain(
        {
            "question": question,
            "chat_history": []
        }, 
        return_only_outputs=False
    )
    logger.info(output)
    logger.success('Answer: {}'.format(output['answer']))
    # logger.success('Source: {}'.format(output['sources']))
    
    
    
    
    