from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=10, unique=True)
    idade = models.PositiveIntegerField()
    curso = models.CharField(max_length=100)
    data_matricula = models.DateField()

    def __str__(self):
        return f"{self.nome}"