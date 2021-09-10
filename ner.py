import spacy
import truecase
from spacy import *
import html,re ,contractions,emoji,unidecode
from textblob import TextBlob
from google_trans_new import google_translator
import nltk
nltk.download('punkt')

nlp = spacy.load('en_core_web_sm')

def normalization_(sentence,tokenize=True):
   sentence = truecase.get_true_case(sentence)
   sentence = html.unescape(sentence)
   regex = re.compile(r'[\n\r\t]')
   sentence = regex.sub(" ", sentence)
   sentence = re.sub(r'http\S+', '', sentence)
   sentence = re.sub('@[^\s]+','',sentence)
   try:
          lang = detect(sentence)
          if lang != 'en':
              translator = google_translator()
              sentence = translator.translate (sentence,lang_tgt='en')
   except :
          try:
              translator = google_translator()
              sentence = translator.translate (sentence,lang_tgt='en')
          except:
              pass
   sentence = contractions.fix(sentence)
   sentence = unidecode.unidecode(sentence)
   return sentence

def tags(sentence):
    sentence=normalization_(sentence)
    doc = nlp(sentence)
    res=[]
    Cardinal = []
    Date = []
    Event = []
    Fac = []
    Gpe = []
    Language = []
    Law = []
    Loc = []
    Money = []
    Norp = []
    Ordinal = []
    Org = []
    Percent = []
    Person = []
    Product = []
    Quantity = []
    Time = []
    Work_of_art = []
    for ent in doc.ents:
        res.append(ent.text)
        res.append(ent.label_)
    for i in range(1,len(res)):
        if res[i] == "CARDINAL":
            Cardinal.append(res[i-1])
        elif res[i]== "DATE":
            Date.append(res[i-1])
        elif res[i]=="EVENT":
            Event.append(res[i-1])
        elif res[i]=="FAC":
            Fac.append(res[i-1])
        elif res[i]=="GPE":
            Gpe.append(res[i-1])
        elif res[i]=="LANGUAGE":
            Language.append(res[i-1])
        elif res[i]=="LAW":
            Law.append(res[i-1])
        elif res[i]=="LOC":
            Loc.append(res[i-1])
        elif res[i]=="MONEY":
            Money.append(res[i-1])
        elif res[i]=="NORP":
            Norp.append(res[i-1])
        elif res[i]=="ORDINAL":
            Ordinal.append(res[i-1])
        elif res[i]=="ORG":
            Org.append(res[i-1])
        elif res[i]== "PERCENT":
            Percent.append(res[i-1])
        elif res[i]== "PERSON" :
            Person.append(res[i-1])
        elif res[i]=="PRODUCT":
            Product.append(res[i-1])
        elif res[i]=="QUANTITY":
            Quantity.append(res[i-1])
        elif res[i]=="TIME":
            Time.append(res[i-1])
        elif res[i]=="WORK_OF_ART":
            Work_of_art.append(res[i-1])
        i+=1
    result={"CARDINAL":Cardinal,"DATE":Date,"EVENT":Event,"FAC":Fac,"GPE":Gpe,"LANGUAGE":Language,"LAW":Law,"LOC":Loc,"MONEY":Money,"NORP":Norp,"ORDINAL":Ordinal,"ORG":Org,"PERCENT":Percent,"PERSON":Person,"PRODUCT":Product,"QUNATITY":Quantity,"TIME":Time,"WORK_OF_ART":Work_of_art}
    return result
