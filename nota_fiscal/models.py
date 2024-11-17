from django.db import models

class NotaFiscal(models.Model):
    id = models.BigAutoField(primary_key=True)
    cliente = models.CharField(max_length=150, default='')
    data_emissao = models.DateTimeField(auto_now_add=True)
    produtos = models.CharField(max_length=150, default='')
    valor_total = models.FloatField(default=0.0)  # Pode ser calculado dinamicamente

    def __str__(self):
        return f'Nota Fiscal ID: {self.id} | Data: {self.data_emissao}'
