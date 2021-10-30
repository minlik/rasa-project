### A rasa project
- custom component: `sentiment.py`
- form action
- retrieval intent: chitchat


### How to use
1. setup
```buildoutcfg
pip install rasa
pip install rasa-x
pip install spacy
python -m spacy download zh_core_web_sm
pip install jieba
```
2. train rasa model
```buildoutcfg
rasa train
```
3. run action server

```buildoutcfg
rasa run actions
```
4. use rasa x to test 

```buildoutcfg
rasa x
```