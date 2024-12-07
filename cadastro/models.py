from django.db import models

HORA_AGENDAMENTO = (
    ('07:30','07:30'),
    ('08:00','08:00'),
    ('08:30','08:30'),
    ('09:00','09:00'),
    ('09:30','09:30'),
    ('10:00','10:00'),
    ('10:30','10:30'),
    ('11:00','11:00'),
    ('11:30','11:30'),
    ('12:00','12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:00', '16:00'),
    ('16:30', '16:30'),
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30')
)


TP_SANGUES_CHOICES = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-')
)
        
SEXO_CHOICES = (
    ('Masculino','Masculino'),
    ('Feminino','Feminino')
)

class Cadastrar(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=50)
    telefone = models.CharField(max_length=13)
    peso = models.FloatField()
    cidade = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)
    cpf = models.CharField(max_length=11, unique=True)
    sexo = models.CharField(max_length=9, choices=SEXO_CHOICES)
    tipo_sang = models.CharField(max_length=3, choices=TP_SANGUES_CHOICES)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    uf = models.CharField(max_length=255)


    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    nomeA = models.CharField(max_length=255)
    cpfA = models.CharField(max_length=11)
    agendamento_data = models.DateField()
    agendamento_hora = models.CharField(max_length=8, choices=HORA_AGENDAMENTO)

    def __str__(self):
        return self.nomeA
