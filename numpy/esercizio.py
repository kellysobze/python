#caricare i dati grezzi,
# pulire i campi
# recuperare quelli recuperabili,
# engignerring

from __future__ import annotations
import re
from dataclasses import dataclass #consente di creare delle classi come se fossero delle entià
from typing import Any,Dict,List,Optional,Tuple

import numpy as np

RAW_RECORDS: List[Dict[str, Any]]= [
{"age": " 25", "income": "€30.000", "debts": "2",   "credit_score": "650", "approved": "yes"},
{"age": "45",  "income": "80000",   "debts": "1",   "credit_score": "720", "approved": "1"},
{"age": "N/A", "income": "€50.000", "debts": "5",   "credit_score": "580", "approved": "no"},
{"age": "23",  "income": " 25k ",   "debts": "3",   "credit_score": "600", "approved": "0"},
{"age": "52",  "income": "120000",  "debts": "0",   "credit_score": "800", "approved": "yes"},
{"age": "40",  "income": "70k",     "debts": "4",   "credit_score": "610", "approved": "no"},
{"age": "??",  "income": "40000",   "debts": "",    "credit_score": None,  "approved": "yes"},
{"age": "31",  "income": "€-1000",  "debts": "2",   "credit_score": "690", "approved": "no"},
{"age": "34 ", "income": "45000",   "debts": "two", "credit_score": "710", "approved": "yes"},
{"age": "29",  "income": " 60000 ", "debts": "1",   "credit_score": "680", "approved": "YES"}, ]

@dataclass #aggiunge i metodi direttamente alla classe, crea un modello dati con le regole che deve rispettare il modello
class CleanRecord: #indica come il record pulito deve essere formato
    age: int
    income: float
    debts: int
    credit_score: int
    approved: int

#creo una classe che analizza il dato e controlla cosa potrebbe essere inoltre se il dato può essere pulito, lo pulisce
class FieldParsers: #classe per la sanificazione, coneverte il dato e se non può restituisce None
    def parse_int(self,value:Any) ->Optional[int]: #tipo di valore che voglio che mi restituisca
        if value is None:
            return None

        if isinstance(value,str):
            txt = value.strip()
            if txt == '' or txt.lower() in {'n/a','na', '??'}:
               return None

            txt = re.sub(r'[^\d-]', '',txt) #tieni solamente le cifre e il segno meno
            if txt =='' or txt == '-':
               return None
        #converto in intero
            try:
               return int(txt)
            except ValueError:
               return None
        if isinstance(value, (int, np.integer)):
               return int(value)
        return None

    def parse_income(self,value:Any) ->Optional[float]:
        if value is None:
            return None
        if isinstance(value, (int, float, np.integer, np.floating)):
            income = float(value)
            return income
        if not isinstance(value, str):
            return None
            #ho escluso tutti i possibili casi tranne la stringa
        txt = value.strip().lower()
        # sanificazione
        if txt in {'','n/a', 'na', '??'}:
            return None
        k_match = re.fullmatch(r'([-+]?\d+)\s*k',txt) #se l'ultima lettera è una k
        if k_match:
            return float(k_match.group(1)) * 1000.0 #moltipiìlica per 1000
        #rimuoviamo simboli dell'euro, evnetuali spazi e punti
        txt= txt.replace('€','').replace(' ','').replace('.','')
        try:
            return float(txt)
        except ValueError:
            return None

    def parse_approved(self,value:Any) ->Optional[int]:
        if value is None:
            return None
        if isinstance(value, (int, np.integer)):
            if int(value) in (0,1):
                return int(value)
            return None
        if not isinstance(value, str):
            return None
        txt = value.strip().lower()
        if txt in {'1','yes', 'y', 'si','sì','t','true'}:
            return 1
        if txt in {'0','no', 'n', 'false','f'}:
            return 0
        return None

#validatore
class RecordValidator:
    #diciamo alla classe di decidere se un dato è pulito
    def is_valid(self,rec:CleanRecord) -> bool: #qualsiasi elemento inizi con 'is' deve restituire un booleano
       if rec.age < 18 or rec.age >99:
           return False
       if rec.income <= 0:
           return False
       if rec.debts < 0 or rec.debts > 50:
           return False
       if rec.credit_score <= 300 or rec.credit_score > 850:
           return False
       if rec.approved not in (0,1):
           return False
       return True

#pipeline
#trasformare il record in una matrice
class PrepocessingPipeline:
    def __init__(self,parsers:FieldParsers,validator:RecordValidator):
        self.parsers = parsers
        self.validator = validator
        self.dropped_recordsn: int = 0
        self.kept_record:int= 0

    def clean_records(self,raw_records:List[Dict[str,Any]]) -> List[CleanRecord]:
        cleaned: List[CleanRecord] = []
        for row in raw_records:
            age = self.parsers.parser_int(row.get('age'))
            income = self.parsers.parse_income(row.get('income'))
            debts=self.parser.parse_debts(row.get('debts'))
            credit_score=self.parser.parse_credit_score(row.get('credit_score'))
            approved=self.parser.parse_approved(row.get('approved'))

            if None in (age,income,debts,credit_score,approved):
                self.dropped_recordsn += 1
                continue
            rec=CleanRecord(
                age=int(age),
                income=float(income),
                debts=int(debts),
                credit_score=int(credit_score),
                approved=int(approved))
            if not self.validator.is_valid(rec):
                self.dropped_record += 1
                continue
            cleaned.append(rec)
            self.kept_record += 1
        return cleaned

    def build_xy(self, cleaned: List([CleanRecord])) -> Tuple[np.array, np.array]:
        x = np.array([[r.age, r.income, r.debts, r.credit_score] for r in cleaned], dtype=float)
        y = np.array([r.approved for r in cleaned], dtype=int)
        return x, y

    def add_featurres(selfself, x: np.array) -> np.array:
        income = x[:, 1]
        debts = x[:, 2]
        debts_to_income = debts / income
        debts_to_income = debts_to_income.reshape(-1, 1)
        x_enhanced = np.hstack((x, debts_to_income))
        return x_enhanced

    # normalizzazione
    def minmax_normalize(self, x: np.array) -> np.array:
        min_col = np.min(x, axis=0)
        max_col = np.max(x, axis=0)
        denom = (max_col - min_col)
        denom[denom == 0] = 1.0  # se il denominatore è 0 lo forziamo a 1
        x_norm = (x - min_col) / denom

    def train_test_split(self, x: np.array, y: np.array, train_ratio: float = 0.8,
                         seed: int = 42) -> Tuple[np.array, np.array, np.array, np.array, np.array]:
        idx = np.arange(len(x))
        rng = np.random.default_rng(seed)
        rng.shuffle(idx)

        train_size = int(len(idx) * train_ratio)
        train_idx = idx[:train_size]
        test_idx = idx[train_size:]
        x_train = x[train_idx]
        x_test = x[test_idx]
        y_train = y[train_idx]
        y_test = y[test_idx]

        return x_train, y_train, x_test, y_test















