'''
history.py: Modulo para definir el modelo Historia Clinica
'''
from mongoengine import Document, StringField, DateTimeField, IntField


class History(Document):
    '''
    Clase que define el modelo historia clinica
    '''
    history_number = IntField()
    patient_name = StringField(required=True, default='')
    patient_dni = StringField(required=True, default='')
    patient_birth_date = DateTimeField(required=False)
    patient_age = IntField(required=False)
    patient_sex = StringField(required=False, default='')
    medic_name = StringField(required=True, default='')
    diagnostic = StringField(required=True, default='')
    admision_date = DateTimeField(required=True)


    def to_json(self):
        '''
        Metodo que devuelve los atributos de la clase en formato json
        '''
        history_dict = {
            "history_id": str(self.pk),
            'history_number': self.history_number,
            "patient_name": self.patient_name,
            "patient_dni": self.patient_dni,
            "patient_birth_date": self.patient_birth_date,
            "patient_age": self.patient_age,
            "patient_sex": self.patient_sex,
            "medic_name": self.medic_name,
            "diagnostic": self.diagnostic,
            "admision_date": self.admision_date,
        }
        return history_dict